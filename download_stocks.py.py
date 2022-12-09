"""
Download the project datafiles from Google Drive.

    -> files will be saved in a new folder: "data".
"""

import gdown
import tarfile
import os


url = "https://drive.google.com/uc?id=1V3EY5weHjTZN-oEcdu6b90X4-SHCJRk3"

fn = "data.tar.gz"
gdown.download(url, fn)

file = tarfile.open(fn)
file.extractall(".")
os.remove("data.tar.gz")
