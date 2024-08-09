import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
dir_files = [filename.lower() for filename in os.listdir(BASE_DIR)]
