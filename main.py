import itertools
from collections import Counter

from preProcesser import preprocess_text

from processor import (
    extract_names_from_phrases,
    preprocess_into_phrases,
    load_name_list,
)

text_filename = "full_book.txt"
names_filename = "characters_names.txt"


def mkpairs(names):
    return (tuple(sorted(comb)) for comb in itertools.combinations(names, 2))


def get_name_pairs_counter(list_of_phrases, list_of_names):
    pairs_counter = Counter()
    for phrase in list_of_phrases:
        names = extract_names_from_phrases(phrase, allowed_names=list_of_names)
        if len(names) <= 1:
            continue

        for pair in mkpairs(names):
            pairs_counter[pair] += 1
    return pairs_counter


def get_name_counter(list_of_phrases, list_of_names):
    names_counter = Counter()
    for phrase in list_of_phrases:
        names = extract_names_from_phrases(phrase, allowed_names=list_of_names)

        for name in names:
            names_counter[name] += 1

    return names_counter


def main():
    list_of_names = load_name_list(names_filename)

    with open(text_filename, encoding="utf-8") as file:
        text0 = file.read()

    text1 = preprocess_text(text0)
    list_of_phrases = preprocess_into_phrases(text1)

    pairs_counter = get_name_pairs_counter(list_of_phrases, list_of_names)
    names_counter = get_name_counter(list_of_phrases, list_of_names)

    print(names_counter.most_common(20))
    print("\n")
    print(pairs_counter.most_common(20))


main()
