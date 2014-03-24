from os import listdir, path
from argparse import ArgumentParser


def word_count(file_name):
    words = {}
    f = open(file_name)
    for line in f:
        for word in line.split():
            if word not in words:
                words[word] = 1
            else:
                words[word] += 1
    f.close()
    return words


def merge_dicts(dict1, dict2):
    new_dict = dict(dict1.items() + dict2.items())
    for i in dict1:
        for j in dict2:
            if i == j:
                new_dict[i] = dict1[i] + dict2[j]
    return new_dict


def get_dir_word_count(dir_path):
    words = {}
    for file_name in listdir(dir_path):
        file_path = dir_path + "/" + file_name
        if path.isdir(file_path):
            tmp = get_dir_word_count(file_path)
            words = merge_dicts(words, tmp)
        else:
            tmp = word_count(file_path)
            words = merge_dicts(words, tmp)
    return words


def get_dir_str(dir_path, filler):
    tmp_str = str()
    for file_name in listdir(dir_path):
        tmp_str += filler + file_name
        file_path = dir_path + "/" + file_name
        if path.isdir(file_path):
            tmp_str += '/\n'
            tmp_str += get_dir_str(file_path, filler + "  ")
        else:
            tmp_str += '\n'
    return tmp_str


def print_dir_tree(dir_path):
    if path.isdir(dir_path):
        print "/"
        print get_dir_str(dir_path, "  ")
        print
        print get_dir_word_count(dir_path)
    else:
        print "'" + dir_path + "' is not a valid path."


if __name__ == "__main__":
    parser = ArgumentParser(description="Prints directory tree"
                            " and count of all distinct words.")
    parser.add_argument("path", type=str, nargs='?', default='.',
                        help="Path to directory (default = '.').")
    args = parser.parse_args()
    print_dir_tree(args.path)
