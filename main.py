from preProcesser import (
    preprocess_text
)

from processor import (
    extract_names_from_phrases,
    preprocess_into_phrases
)

filename = "full_book.txt"


def main():

    with open(filename, encoding="utf-8") as file:
        text0 = file.read()
    text1 = preprocess_text(text0)
    list_of_phrases = preprocess_into_phrases(text1)
    for phrase in list_of_phrases:
        names = extract_names_from_phrases(phrase)
        if(names != []):
            for word in names:
                ...

main()
