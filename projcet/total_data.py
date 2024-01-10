import glob
import concurrent.futures


def file_counter(dummy):
    return 1


def count_files(path):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(file_counter, glob.glob(path))
        return sum(results)


def total_files():
    return count_files('../data/data/*.txt')
