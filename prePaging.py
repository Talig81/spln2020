import re

# Trata do preprocessamento


def preprocess_remove_pages(text):
    """
    Tira as notaçoes das páginas no texto
    >>> preprocess_remove_pages("abc Page | 3 asb")
    "abc  "
    """
    split_by_pages = re.split(r"(Page \| [1-9]+\s.*)", text)
    return " ".join(split_by_pages[::2])


def preprocess_newlines(text):
    "Remove all newlines from the text"
    return text.replace("\n", " ")


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
