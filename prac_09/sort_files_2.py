import os


def main():
    filetype_to_category = {}
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        file_type = filename.split('.')[-1]
        if file_type not in filetype_to_category:
            the_type = input("What category would you like to sort {} files into? ".format(file_type))
            filetype_to_category[file_type] = the_type
            try:
                os.mkdir(the_type)
            except FileExistsError:
                pass

        os.rename(filename, "{}/{}".format(filetype_to_category[file_type], filename))


main()