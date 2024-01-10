import tarfile
import os
import shutil

tarfile_path = os.path.join(os.path.dirname(__file__), '../data.tar.gz')


def is_directory_empty(directory):
    if os.path.exists(directory) and os.path.isdir(directory):
        return not os.listdir(directory)
    else:
        print("Directory does not exist or is not a directory.")
        return None


def extract_tarfile():
    with tarfile.open(tarfile_path, 'r:gz') as tar:
        tar.extractall(path='../data')


def clear_directory(directory):
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path) or os.path.islink(item_path):
            os.unlink(item_path)
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)


if __name__ == '__main__':
    console = input('Enter extract to extract tarfile to data dir\nEnter clear to clear data dir\n')
    if console == 'extract':
        if is_directory_empty('../data'):
            extract_tarfile()
        else:
            print('Directory already contains files')
    elif console == 'clear':
        if not is_directory_empty('../data'):
            clear_directory('../data')
        else:
            print('Directory is already empty')
    else:
        print('Wrong input')