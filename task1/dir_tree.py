from os import listdir, path
from sys import argv


def print_dir(dir_path, filler):
    for file_name in listdir(dir_path):
        print filler + file_name,
        file_path = dir_path + "/" + file_name
        if path.isdir(file_path):
            print "/"
            print_dir(file_path, filler + "  ")
        else:
            print


def print_dir_tree(dir_path):
    if path.isdir(dir_path):
        print "/"
        print_dir(dir_path, "  ")
    else:
        print "'" + dir_path + "' is not a valid path."


if __name__ == "__main__":
    if len(argv) > 1:
        print_dir_tree(argv[1])
    else:
        print_dir_tree(".")
