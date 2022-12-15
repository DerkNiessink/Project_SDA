"""
Download the project datafiles from Google Drive.

    -> files will be saved in a new folder: "data".
"""

import gdown
import tarfile
import os


url = "https://drive.google.com/uc?id=1aiHk8LLk_3kykeDJoCEkQQ0o81wQNTfM"

fn = "data.tar.gz"
gdown.download(url, fn)

file = tarfile.open(fn)
file.extractall(".")
os.remove("data.tar.gz")
