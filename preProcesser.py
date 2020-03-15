import re

# Trata do preprocessamento


def preprocess_remove_pages(text):
    """
    Tira as notaçoes das páginas no texto
    >>> preprocess_remove_pages("abc Page | 3 asb")
    "abc  "
    """
    split_by_pages = re.split(r"(Page \| [0-9]+\s.*)", text)
    return " ".join(split_by_pages[::2])


def preprocess_remove_newlines(text):
    "Remove all newlines from the text"
    return text.replace("\n", " ")


def preprocess_text(text):
    without_pages = preprocess_remove_pages(text)
    without_newlines = preprocess_remove_newlines(without_pages)
    return without_newlines
