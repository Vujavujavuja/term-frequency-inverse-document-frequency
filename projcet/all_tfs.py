from term_frequency import term_frequency
import glob
import time
from functools import reduce
import concurrent.futures
import json


def concatenate(acc, item):
    acc.extend(item)
    return acc


def all_tfs():
    file_paths = glob.glob('../data/data/*.txt')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = map(lambda file_path: executor.submit(term_frequency, file_path), file_paths)
        results = map(lambda future: future.result(), concurrent.futures.as_completed(futures))
        all_tf_tuples = reduce(concatenate, results, [])
    return all_tf_tuples


if __name__ == '__main__':
    start = time.time()
    tf_tuples = all_tfs()
    print(tf_tuples)
    end = time.time()
    print("Execution time: ", end - start, "seconds")

    # with open('log_tf.json', 'w', encoding='utf-8') as file:
    #     json.dump(tf_tuples, file, ensure_ascii=False, indent=4)

    # print("IDF values written to log.json")
