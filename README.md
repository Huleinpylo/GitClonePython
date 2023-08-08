# GitClonePython


This project is a Python script named `GitGetter.py` that automates the process of cloning a Git repository based on the target operating system. The script detects the system type and installs Git if necessary before cloning the specified Git repository to a given destination directory.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Supported Operating Systems](#supported-operating-systems)
- [License](#license)

## Introduction

The `GitGetter.py` script checks the operating system and uses the appropriate package manager to install Git if required. It then proceeds to clone the specified Git repository to the destination directory.

## Prerequisites

To run the `GitGetter.py` script, ensure that you have the following software installed on your system:

- Python 3
- Git (optional, as the script will install it if missing)

## Usage

1. Clone this repository to your local machine:

```bash
git clone https://github.com/Huleinpylo/GitClonePython.git
```

Change directory to the project folder:
bash
Copy code
cd <project_folder>
Run the Python script with the following command:
bash
Copy code
python3 GitGetter.py --url <GIT_REPOSITORY_URL> --destination <DESTINATION_DIRECTORY>
Replace <GIT_REPOSITORY_URL> with the URL of the Git repository you want to clone and <DESTINATION_DIRECTORY> with the desired path where you want to save the cloned repository.

## Supported Operating Systems

The GitGetter.py script supports the following operating systems:

- Linux (Ubuntu, Debian, CentOS, and others using apt or yum package managers)
- macOS
- Windows


Please note that the script may need administrative privileges to install Git on certain systems, such as Windows, if it is not already installed.
