from prePaging import (
    preprocess_remove_pages,
    preprocess_newlines,
    preprocess_into_phrases,
    extract_names_from_phrases,
)

filename = "notVeggies.txt"


def main():
    with open(filename, encoding="utf-8") as file:
        text0 = file.read()

    text1 = preprocess_remove_pages(text0)
    text2 = preprocess_newlines(text1)
    list_of_phrases = preprocess_into_phrases(text2)

    for phrase in list_of_phrases:
        names = extract_names_from_phrases(phrase)
        print(names, phrase)


main()
