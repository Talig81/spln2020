import sys
import itertools
from collections import Counter

from preProcesser import preprocess_remove_pages, preprocess_remove_newlines

from processor import (
    extract_names_from_phrases,
    preprocess_into_phrases,
    get_name_list,
)

text_filename = "full_book.txt"
names_filename = "characters_names.txt"


def get_interactions_counter(names_per_phrase):
    def mkInteractions(names):
        return (tuple(sorted(comb)) for comb in itertools.combinations(names, 2))

    interactions_counter = Counter()
    for names in [names for names in names_per_phrase if len(names) > 1]:
        for pair in mkInteractions(names):
            interactions_counter[pair] += 1

    return interactions_counter


def get_name_counter(names_per_phrase):
    names_counter = Counter()
    for names in names_per_phrase:
        for name in names:
            names_counter[name] += 1

    return names_counter


def get_interactions(character_name, interactions_counter):
    character_interaction_counter = Counter()
    character_name = character_name.lower()
    for name1, name2 in interactions_counter.keys():
        if name1.lower() == character_name or name2.lower() == character_name:
            interaction = (name1, name2)
            character_interaction_counter[interaction] = interactions_counter[
                interaction
            ]

    return character_interaction_counter


def build_graph(interactions):
    dot_body = ["graph interactions {"]

    for name1, name2 in interactions:
        dot_body.append(f"\t{name1} -- {name2};")

    dot_body.append("}")
    return "\n".join(dot_body)


def display_counter(counter):
    for key, value in counter.most_common():
        if isinstance(key, tuple):
            key = " and ".join(key)

        print(f'{value}\t{key}')


def main():
    with open(names_filename, encoding="utf-8") as file:
        list_of_names = get_name_list(file.readlines())

    with open(text_filename, encoding="utf-8") as file:
        text = file.read()
        without_pages = preprocess_remove_pages(text)
        without_newlines = preprocess_remove_newlines(without_pages)
        list_of_phrases = preprocess_into_phrases(without_newlines)

    names_per_phrase = [
        extract_names_from_phrases(phrase, allowed_names=list_of_names)
        for phrase in list_of_phrases
    ]

    if sys.argv[1] == "names":
        names_counter = get_name_counter(names_per_phrase)
        display_counter(names_counter)
    elif sys.argv[1] == "interactions":
        interactions_counter = get_interactions_counter(names_per_phrase)
        display_counter(interactions_counter)

    elif sys.argv[1] == "interactions_of":
        interactions_counter = get_interactions_counter(names_per_phrase)
        name_interactions = get_interactions(sys.argv[2], interactions_counter)
        display_counter(name_interactions)

    elif sys.argv[1] == "graph":
        interactions_counter = get_interactions_counter(names_per_phrase)
        dotgraph = build_graph(interactions_counter)
        print(dotgraph)
    else:
        raise IndexError


try:
    main()
except IndexError:
    print(
        """main.py

    # To display all the names found
    $ python main.py names

    # To display all the interactions and their respective count
    $ python main.py interactions

    # To display all the interactions of a single character
    $ python main.py interactions_of

    # To output a dot file with the interaction graph
    $ python main.py graph > graph.dot
    $ dot -Tpng graph.dot > graph.png
"""
    )
