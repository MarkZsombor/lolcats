import os
import platform
import subprocess

import cat_service


def main():
    print_header()
    folder = get_or_create_output_folder()
    download_cats(folder)
    display_cats(folder)


def print_header():
    print('Lolcat Factory')


def get_or_create_output_folder():
    # __file__ will return the current file with location
    # so dirname(__file__) will return current folder
    base_folder = os.path.dirname(__file__)
    folder = 'cat_pictures'
    full_path = os.path.join(base_folder, folder)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('Creating new directory at {}'.format(full_path))
        os.mkdir(full_path)

    return full_path


def download_cats(folder):
    print('Connecting to server')
    cat_count = 8
    # basic loop
    for i in range(1, cat_count+1):
        name = 'lolcat {}'.format(i)
        print('Downloading {}'.format(name))
        cat_service.get_cat(folder, name)

    print('Downloading complete')


def display_cats(folder):
    # open folder, open in an image browser
    print('Displaying cat images')
    if platform.system() == 'Darwin':
        subprocess.call(['open', folder])
    if platform.system() == 'Linux':
        subprocess.call(['xdg-open', folder])
    if platform.system() == 'Windows':
        subprocess.call(['start', folder])


if __name__  == '__main__':
    main()
