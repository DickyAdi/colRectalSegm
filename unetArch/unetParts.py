import torch
import torch.nn as nn
import torch.nn.functional as F
import math

class spatialAttention(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = nn.Conv2d(2, 1, kernel_size=3, padding=1)
    def forward(self, x):
        avg = torch.mean(x, dim=1, keepdim=True)
        maxVal, _ = torch.max(x, dim=1, keepdim=True)
        cat = torch.cat((avg, maxVal), dim=1)
        x = self.conv(cat)
        return torch.sigmoid(x)

class channelAttention(nn.Module):
    def __init__(self, in_channels):
        super().__init__()
        self.in_channels = in_channels
        self.convBlock = nn.Sequential(
            nn.Conv2d(in_channels, math.ceil(in_channels//16), 1),
            nn.Conv2d(math.ceil(in_channels//16), math.ceil(in_channels//16), 3, padding=1),
            nn.Conv2d(math.ceil(in_channels//16), 1, 1)
        )
    def forward(self, x):
        avg = torch.mean(x, dim=(-1, -2), keepdim=True)
        maxVal, _ = torch.max(x.view(x.size(0), x.size(1), -1), dim=2, keepdim=True)
        maxVal = maxVal.view(x.size(0), x.size(1), 1, 1)
        outAvg = self.convBlock(avg)
        outMax = self.convBlock(maxVal)
        x = torch.add(outAvg, outMax)
        return torch.sigmoid(x)

class DoubleConv(nn.Module):
    def __init__(self, in_channels, out_channels, mid_channels=None, attention=False, residual=False):
        super().__init__()
        self.residual = residual
        self.attention = attention
        if residual:
            self.resconv = nn.Conv2d(in_channels, out_channels, 1, 1)
        if not mid_channels:
            mid_channels = out_channels
        self.double_conv = nn.Sequential(
            nn.Conv2d(in_channels, mid_channels, kernel_size=3, padding=1, bias=False),
            nn.BatchNorm2d(mid_channels),
            nn.ReLU(inplace=True),
            nn.Conv2d(mid_channels, out_channels, kernel_size=3, padding=1, bias=False),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True)
        )
        if attention:
            self.spatialAtt = spatialAttention()
            self.channelAtt = channelAttention(out_channels)
    def forward(self, x):
        if self.residual:
            residual = self.resconv(x)
        x = self.double_conv(x)
        if self.attention:
            channelAttVal = self.channelAtt(x)
            spatialAttVal = self.spatialAtt(x)
            channelAttValX = torch.mul(x, channelAttVal)
            spatialAttValX = torch.mul(x, spatialAttVal)
        if self.residual and self.attention:
            return channelAttValX + spatialAttValX + residual
        if self.residual and not self.attention:
            return x + residual
        if not self.residual and self.attention:
            return channelAttValX + spatialAttValX
        if not self.residual and not self.attention:
            return x
    
class Down(nn.Module):
    def __init__(self, in_channels, out_channels, attention=False, residual=False):
        super().__init__()
        self.maxpool_conv = nn.Sequential(
            nn.MaxPool2d(2),
            DoubleConv(in_channels, out_channels, attention=attention, residual=residual)
        )
    
    def forward(self, x):
        return self.maxpool_conv(x)
    
class Up(nn.Module):
    def __init__(self, in_channels, out_channels, attention=False, residual=False, bilinear=True):
        super().__init__()
        if bilinear:
            self.up = nn.Upsample(scale_factor=2, mode='bilinear', align_corners=True)
            self.conv = DoubleConv(in_channels, out_channels //2, attention=attention, residual=residual)
        else:
            self.up = nn.ConvTranspose2d(in_channels, in_channels//2, kernel_size=2, stride=2)
            self.conv = DoubleConv(in_channels, out_channels, attention=attention, residual=residual)
    
    def forward(self, x1, x2):
        x1 = self.up(x1)
        diffY = x2.size()[2] - x1.size()[2]
        diffX = x2.size()[3] - x1.size()[3]

        x1 = F.pad(x1, [diffX // 2, diffX - diffX // 2, diffY // 2, diffY - diffY //2])
        x = torch.cat([x2, x1], dim=1)
        return self.conv(x)
    
class OutConv(nn.Module):
    def __init__(self, in_channels, out_channels):
        super(OutConv, self).__init__()
        self.conv = nn.Conv2d(in_channels, out_channels, kernel_size=1)

    def forward(self, x):
        return self.conv(x)