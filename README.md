<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->

<a name="readme-top"></a>

<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <!-- <a href="https://github.com/DickyAdi/colRectalSegm">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a> -->

<h3 align="center">Colorectal Cancer Segmentation</h3>

  <p align="center">
    Segmenting a colorectal cancer from histopathology images using UNet architecture
    <br />
    <a href="https://github.com/DickyAdi/colRectalSegm"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/DickyAdi/colRectalSegm">View Demo</a>
    ·
    <a href="https://github.com/DickyAdi/colRectalSegm/issues">Report Bug</a>
    ·
    <a href="https://github.com/DickyAdi/colRectalSegm/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#Model-Parameters-Documentation">Model Parameters Documentation</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
    <li><a href="#Reference">Reference</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

![Product Name Screen Shot][product-screenshot]

<!-- Here's a blank template to get started: To avoid retyping too much info. Do a search and replace with your text editor for the following: -->

This project uses UNet, Residual UNet, and Attention UNet with dice score and combined dice loss as below:

| Model          | Dice score | Dice loss |
| -------------- | ---------- | --------- |
| UNet           | 0.8454     | 0.1489    |
| Residual UNet  | 0.8267     | 0.1454    |
| Attention UNet | 0.9412     | 0.1817    |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

- [![Lightning][lightning-shield]][lightning-url]
- [![PyTorch][pytorch-shield]][pytorch-url]
- [![Python Version][python-shield]][python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This project requires Python 3.7 or higher

- You can download the latest Python version [here](https://www.python.org/downloads/).

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/DickyAdi/colRectalSegm.git
   ```
2. move to the colRectalSegm directory
   ```sh
   cd colRectalSegm
   ```
3. Install the **requirements.txt**
   ```sh
   pip install -r requirements.txt
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

There're 2 approaches to use this project:

1. <a href="#model-arch">Using the model architecture only</a>
2. <a href="#jupy">Using the jupyter notebook</a>

<h3 name="model-arch">Using model architecture only</h3>
Since the model is written in PyTorch nn.module, so the model can be used . In order to do that, do the follows.

1. The model is located at
   ```sh
       .
   └── unetArch/
       ├── .
       ├── .
       ├── .
       ├── unetModel.py
       └── unetParts.py
   ```
2. Import the model
   ```py
   from unetArch import UNet
   ```
3. Assign the model to a variable
   ```py
   model = UNet(n_channels=3, n_classes=5)
   ```
4. Proceed to use the model

<h3 name="jupy">Using the jupyter notebook</h3>
The provided jupyter notebook is only for a guidelines on how to use the model, make sure to modify the notebook to your specific case.

1. Open the provided jupyter notebook with the name of
   ```sh
   colorectalSegm.ipynb
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Model Parameters Documentations -->

## Model Parameters Documentations

> _unetArch.unetModel.UNet(n_channels, n_classes, residual=False, attention=False)_

- n_channels`int`: This parameter initialize the color channels of your image in your dataset. 3 for RGB, and 1 for black and white.
- n_classes`int`: This parameter initialize how many labels you have in your image in your dataset and makesure you add 1 to it because of the background.
- residual`bool`: This parameter initialize whether to use residual connection in your model or not. Default value is False.
- attention`bool`: This parameter initialize wheter to use channel and spatial attention in your model or not. Default value is False.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. As this is my first open source project, any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

Dicky Adi N.F - [Dicky Adi](https://www.linkedin.com/in/dickyadi/)

Project Link: [https://github.com/DickyAdi/colRectalSegm](https://github.com/DickyAdi/colRectalSegm)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->

## Acknowledgments

- [@milesial](https://github.com/milesial/Pytorch-UNet/tree/master)
- [@mhihsan](https://github.com/mhihsan)
- [@LSardiani](https://github.com/LSardiani)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Reference

- [ARU-Net: Research and Application for Wrist Reference Bone Segmentation](https://ieeexplore.ieee.org/abstract/document/8895740)
- [EBHI-Seg: A novel enteroscope biopsy histopathological hematoxylin and eosin image dataset for image segmentation tasks](https://www.frontiersin.org/articles/10.3389/fmed.2023.1114673/full)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/DickyAdi/colRectalSegm.svg?style=for-the-badge
[contributors-url]: https://github.com/DickyAdi/colRectalSegm/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/DickyAdi/colRectalSegm.svg?style=for-the-badge
[forks-url]: https://github.com/DickyAdi/colRectalSegm/networks/member
[stars-shield]: https://img.shields.io/github/stars/DickyAdi/colRectalSegm.svg?style=for-the-badge
[stars-url]: https://github.com/DickyAdi/colRectalSegm/stargazers
[issues-shield]: https://img.shields.io/github/issues/DickyAdi/colRectalSegm.svg?style=for-the-badge
[issues-url]: https://github.com/DickyAdi/colRectalSegm/issues
[license-shield]: https://img.shields.io/github/license/DickyAdi/colRectalSegm.svg?style=for-the-badge
[license-url]: https://github.com/DickyAdi/colRectalSegm/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/dickyadi/
[product-screenshot]: output.png
[python-shield]: https://img.shields.io/badge/Python-3.11%2B-blue.svg
[python-url]: https://www.python.org/downloads/
[opencv-shield]: https://img.shields.io/badge/OpenCV-Used-brightgreen?logo=opencv
[opencv-url]: https://pypi.org/project/opencv-python/
[pytorch-shield]: https://img.shields.io/badge/PyTorch-Used-brightgreen?logo=pytorch
[pytorch-url]: https://pytorch.org
[lightning-shield]: https://img.shields.io/badge/Lightning-Used-brightgreen?logo=lightning
[lightning-url]: https://pypi.org/project/lightning/
