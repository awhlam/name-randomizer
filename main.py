from random import randint
from os import path, makedirs, walk
from shutil import copy2, rmtree

INPUT_DIRECTORY = r'/Users/andrew/repos/name-randomizer/input'
OUTPUT_DIRECTORY = r'/Users/andrew/repos/name-randomizer/output'
CLEAR_OUTPUT = True

if __name__ == "__main__":
  if CLEAR_OUTPUT:
    rmtree(OUTPUT_DIRECTORY)
    makedirs(OUTPUT_DIRECTORY)

  for root, dirs, files in walk(INPUT_DIRECTORY):
    for source_name in files:
      source_path = path.join(INPUT_DIRECTORY, source_name)

      output_name = str(randint(0,99999)) + '.jpg'
      output_path = path.join(OUTPUT_DIRECTORY, output_name)

      print(f"{source_path} => {output_path}")
      copy2(source_path, output_path)