import math
from functools import reduce
from collections import Counter
from all_tfs import all_tfs
import time
import json
from total_data import total_files


def add_to_set(acc, tf_tuple):
    acc.add((tf_tuple[1], tf_tuple[0]))
    return acc


def count_docs_per_word(tf_tuples):
    word_file_set = reduce(add_to_set, tf_tuples, set())
    return Counter(word for word, file in word_file_set)


def calculate_idf_word(word, total_documents, word_doc_count):
    return (word, math.log(total_documents / word_doc_count[word]))


def calculate_idf(tf_tuples, total_documents):
    word_doc_count = count_docs_per_word(tf_tuples)
    return dict(map(lambda word: calculate_idf_word(word, total_documents, word_doc_count), word_doc_count))


if __name__ == '__main__':
    tf_tuples = all_tfs()
    start = time.time()
    idf = calculate_idf(tf_tuples, total_files())
    print(idf)
    end = time.time()
    print("Execution time: ", end - start, "seconds")
    idf_values = idf

    with open('log_idf.json', 'w', encoding='utf-8') as file:
        json.dump(idf_values, file, ensure_ascii=False, indent=4)

    print("IDF values written to log.json")