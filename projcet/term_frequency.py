from functools import reduce
import re
from collections import Counter
import time


def clean_text(text):
    text = re.sub(r"[,.!?\n\"'“()#$@’]", ' ', text)
    return text


def text_length(collection):
    return reduce(lambda count, _: count + 1, collection, 0)


def make_tf_tuple(word_count_tuple, total_words, file_path):
    word, count = word_count_tuple
    return (file_path, word, count / total_words)


def term_frequency(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()

    text = clean_text(text)
    words = re.findall(r'\b\w+\b', text)
    total_words = text_length(words)
    word_count = Counter(words)

    tf_tuples = map(lambda word_count_tuple: make_tf_tuple(word_count_tuple, total_words, file_path), word_count.items())
    return list(tf_tuples)


if __name__ == '__main__':
    start = time.time()
    tf_result = term_frequency('../data/data/0006.txt')
    print(tf_result)
    end = time.time()
    print("Execution time: ", end - start, "seconds")
