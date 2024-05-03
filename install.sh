#!/bin/bash
#
# Script to Install
# Linux System Tools and
# Basic Python Components
# GENERAL LINUX
apt-get update  # updates the package index cache
apt-get upgrade -y  # updates packages
apt install lsb-core -y


# installs system tools
apt-get install -y bzip2 gcc git  # system tools
apt-get install -y htop screen vim wget  # system tools
apt-get upgrade -y bash  # upgrades bash if necessary
apt-get clean  # cleans up the package index cache

# INSTALL MINICONDA
# downloads Miniconda
# For x86_64
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O Miniconda.sh
# For Apple Silicon
# wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-aarch64.sh -O Miniconda.sh
bash Miniconda.sh -b  # installs it
rm -rf Miniconda.sh  # removes the installer
export PATH="/root/miniconda3/bin:$PATH"  # prepends the new path

# Running cells with 'Python 3.12.2 ('base')' requires ipykernel package.
conda install -y -n base ipykernel --update-deps --force-reinstall



# INSTALL PYTHON LIBRARIES
# NumPy comes already installed with Miniconda
conda install -y pandas  # installs pandas
conda install -y lxml # this is optional if we want to work with webpages scraping or reading from HTML pages.
conda install numba




pip install --upgrade pip  # upgrading the package manager
pip install fastapi uvicorn[standard]
pip install q  # logging and debugging