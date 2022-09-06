from random import shuffle
from os import path, makedirs
import glob
from shutil import copy2, rmtree

WORKING_DIR = r'C:/Users/Andrew/repos/name-randomizer/'
CLEAR_OUTPUT = True

output_dir = path.join(WORKING_DIR, 'output')
input_dir = path.join(WORKING_DIR, 'input')
glob_dir = input_dir + "/**/*.*"

if __name__ == "__main__":
    if CLEAR_OUTPUT:
        rmtree(output_dir)
        makedirs(output_dir)

    files = glob.glob(glob_dir, recursive=True)
    filenames = [str(i) for i in range(1, len(files) + 1)]
    shuffle(filenames)

    for source_path in files:
        file_extension = path.splitext(source_path)[1]
        file_name = filenames.pop(-1)

        output_name = file_name + file_extension
        output_path = path.join(output_dir, output_name)

        print(f"{source_path} => {output_path}")
        copy2(source_path, output_path)
