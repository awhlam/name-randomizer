from random import shuffle
from os import path, makedirs, mkdir
from glob import glob
from shutil import copy2, rmtree
from datetime import datetime

DIR_NAMES = ["input", "output", "logs"]
CLEAR_OUTPUT_DIR = True
LOG_FILENAME = f"logs/log-{datetime.now()}.txt".replace(":", "")
GLOB_DIR = "input/**/*.*"

def main():
    setup_directories()
    files, filenames = prepare_files()
    copy_with_random_names(files, filenames)

def setup_directories():
    for dir in DIR_NAMES:
        if not path.exists(dir):
            mkdir(dir)

    if CLEAR_OUTPUT_DIR:
        rmtree("output")
        makedirs("output")

def prepare_files():
    f = open(LOG_FILENAME, "a")
    files = glob(GLOB_DIR, recursive=True)

    # get file counts and exclude files
    f.write(f"Number of files: {len(files)}\n")
    files = [file for file in files if 'exclude' not in file.lower()]
    f.write(f"Number of files after removing exclusions: {len(files)}\n")

    filenames = [str(i) for i in range(1, len(files) + 1)]
    shuffle(filenames)
    f.close()
    return files, filenames

def count_digits(number):
    count = 0
    while number > 0:
        number = number // 10
        count += 1
    return count

def copy_with_random_names(files, filenames):
    f = open(LOG_FILENAME, "a")
    for source_path in files:
        file_extension = path.splitext(source_path)[1]
        file_name = filenames.pop(-1)

        # pad filenames with leading zeros
        num_digits = count_digits(len(files))
        file_name = file_name.zfill(num_digits)

        # move files and write to log
        output_path = "output/" + file_name + file_extension
        f.write(f"{source_path} > {output_path}\n")
        copy2(source_path, output_path)
    f.close()

if __name__ == "__main__":
    main()