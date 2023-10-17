import subprocess
def install_libraries(library_list):
    for library in library_list:
        try:
            subprocess.check_call(['pip', 'install', library])
            print(f"Successfully installed: {library}")
        except subprocess.CalledProcessError:
            print(f"Failed to install: {library}")

if __name__ == "__main__":
    libraries_to_install = ["torchinfo", "torchmetrics", "torchmetrics[detection]", "lightning", "albumentations"]  # Add the list of libraries you want to install here
    install_libraries(libraries_to_install)