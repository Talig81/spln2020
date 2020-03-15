import re

def preprocess_into_phrases(text):
    "Split the text into a list of phrases"

    split_by_phrases = re.split(r"(\s[^A-Z][a-z]+[\.!?])", text)

    # These are the phrases
    even_elements = split_by_phrases[::2]

    # These are the end of phrases including their punctuation
    odd_elements = split_by_phrases[1::2]

    return ["".join([phrase, end]).strip() for phrase, end in zip(even_elements, odd_elements)]


def extract_names_from_phrases(text):
    # Let's start by downcasing some parts
    word0, rest = text.split(" ", maxsplit=1)
    text1 = " ".join([word0.lower(), rest])

    # Now let's grab any uppercase consecutive names
    pattern = r"\b(?:[A-Z][a-z]*\b\s*)+"
    names = [name.strip() for name in re.findall(pattern, text1)]

    return names

def preprocess_names(text):
    text.strip()

    with open("characters_names.txt", encoding="utf-8") as file:
        text = file.read()
    text1 = text.split("\n")
    for line in text1:
        char = line.split(" ")
        char = line.split(",")
