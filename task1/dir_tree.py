from os import listdir, path
from argparse import ArgumentParser


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
    parser = ArgumentParser(description="Prints directory tree specified.")
    parser.add_argument("path", type=str, nargs='?', default='.',
                        help="Path to directory (default = '.').")
    args = parser.parse_args()
    print_dir_tree(args.path)
