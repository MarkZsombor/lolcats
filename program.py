import os

def main():
    print_header()
    folder = get_or_create_output_folder()
    # download cat
    # display cats


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

if __name__  == '__main__':
    main()
