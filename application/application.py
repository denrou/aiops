#! /usr/bin/env python

# Create a temporary folder
import os
import tempfile
from numpy.random import poisson
from random import sample
import time
from datetime import datetime

temp_dir = "tmp"
if not os.path.exists(temp_dir):
    os.makedirs(temp_dir)

# Create a temporary file with random bytes in it
def create_temp_file(size):
    temp_file = tempfile.NamedTemporaryFile(dir=temp_dir, delete=False)
    temp_file.write(os.urandom(size))
    temp_file.close()
    return temp_file.name


if __name__ == "__main__":
    i = 1
    now = datetime.now().minute
    while True:
        create_temp_file(int(poisson(1) * 1024))
        if now != datetime.now().minute:
            files = os.listdir(temp_dir)
            files_to_remove = sample(files, min(280, len(files)))
            for file in files_to_remove:
                os.remove(os.path.join(temp_dir, file))
            now = datetime.now().minute
        time.sleep(0.2)
        i += 1
