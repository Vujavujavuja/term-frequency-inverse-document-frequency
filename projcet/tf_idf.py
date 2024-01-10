from multiprocessing import Pool
from all_tfs import all_tfs
from inverse_document_frequency import calculate_idf
from total_data import total_files
import time
import json

tfs = all_tfs()
idfs = calculate_idf(tfs, total_files())


def calculate_tf_idf(tf_tuple):
    doc_path, word, tf = tf_tuple
    tf_idf = tf * idfs.get(word, 0)
    return doc_path, word, tf_idf


def tf_idf():
    with Pool() as pool:
        tf_idf_tuples = pool.map(calculate_tf_idf, tfs)
    return tf_idf_tuples


def sort_tf_idf(tf_idf_tuples):
    return sorted(tf_idf_tuples, key=lambda x: (x[0], -x[2]))


if __name__ == '__main__':
    start = time.time()
    tf_idf_tuples = tf_idf()
    sorted_tf_idf = sort_tf_idf(tf_idf_tuples)
    print(sorted_tf_idf)
    end = time.time()
    print("Execution time: ", end - start, "seconds")
    with open('log_tf_idf.json', 'w', encoding='utf-8') as file:
        json.dump(sorted_tf_idf, file, ensure_ascii=False, indent=4)

    print("IDF values written to log.json")