"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import os


def main():
    """Change filenames to consistent"""

    # Change to desired directory
    os.chdir('Lyrics/Christmas')
    for directory_name, subdirectories, filenames in os.walk('.'):
        for filename in filenames:
            new_name = get_fixed_filename(filename)
            print("Renaming {} to {}".format(filename, new_name))

            old_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, get_fixed_filename(filename))
            os.rename(old_name, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")

    if "_" not in new_name:
        new_name = list(new_name)
        for i in range(len(new_name)):
            if i == 0:
                pass
            elif new_name[i].isupper():
                new_name[i - 1] += "_"
        new_name = "".join(new_name)

    return new_name


main()
