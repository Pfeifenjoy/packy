import subprocess

def install_package(package_name):
    try:
        # Execute pip command to install the package
        subprocess.check_call(['pip', 'install', package_name])
        print(f"Successfully installed {package_name}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while installing {package_name}: {e}")

# Example usage
if __name__ == '__main__':
    install_package('pygame')
    install_package('pydantic')
