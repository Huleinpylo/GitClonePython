import platform
#import distro
import subprocess
import argparse
import os

def install_git(url, destination):
    system = platform.system()

    if system == "Linux":
        if os.path.exists("/usr/bin/apt"):
            package_manager = "apt"
        elif os.path.exists("/usr/bin/yum"):
            package_manager = "yum"
        else:
            print("Unsupported Linux distribution. Please install Git manually.")
            return

        subprocess.run([package_manager, "install", "-y", "git"])
    elif system == "Darwin":
        try:
            subprocess.run(["brew", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        except FileNotFoundError:
            subprocess.run(['/bin/bash', '-c', "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"])

        subprocess.run(["brew", "install", "git"])

    elif system == "Windows":
        try:
            subprocess.run(["git", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        except FileNotFoundError:
            try:
                subprocess.run(["choco", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            except FileNotFoundError:
                subprocess.run(["powershell", "-Command", "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))"], shell=True, text=True)
                subprocess.run(["choco", "install", "-y", "git"])

    else:
        print(f"Unsupported operating system: {system}")

    result = subprocess.run(['git', 'clone', url, destination], stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
    print(result)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clone a Git repository.")
    parser.add_argument("-u", "--url", help="URL of the Git repository to clone", type=str, required=True, action="store")
    parser.add_argument("-d", "--destination", help="Destination directory for the clone", type=str, required=True, action="store")
    args = parser.parse_args()
    install_git(args.url, args.destination)
