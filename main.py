from random import shuffle
from os import path, makedirs, mkdir
from glob import glob
from shutil import copy2, rmtree
from datetime import datetime

DIR_NAMES = ["input", "output", "logs"]
CLEAR_OUTPUT_DIR = True
LOG_FILENAME = f"logs/log-{datetime.now()}.txt".replace(":", "")
GLOB_DIR = "input/**/*.*"

if __name__ == "__main__":
    for dir in DIR_NAMES:
        if not path.exists(dir):
            mkdir(dir)

    if CLEAR_OUTPUT_DIR:
        rmtree("output")
        makedirs("output")

    f = open(LOG_FILENAME, "w")
    files = glob(GLOB_DIR, recursive=True)
    print(f"Number of files: {len(files)}")
    files = [file for file in files if 'exclude' not in file.lower()]
    print(f"Number of files after removing exclusions: {len(files)}")

    filenames = [str(i) for i in range(1, len(files) + 1)]
    shuffle(filenames)

    for source_path in files:
        file_extension = path.splitext(source_path)[1]
        file_name = filenames.pop(-1)

        output_path = "output/" + file_name + file_extension

        log_message = f"{source_path} > {output_path}"
        f.write(log_message + "\n")
        print(log_message)

        copy2(source_path, output_path)
    f.close()
