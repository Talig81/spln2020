import re


def preprocess_into_phrases(text):
    "Split the text into a list of phrases"

    split_by_phrases = re.split(r"(\s[^A-Z][a-z]+[\.!?])", text)

    # These are the phrases
    even_elements = split_by_phrases[::2]

    # These are the end of phrases including their punctuation
    odd_elements = split_by_phrases[1::2]

    return [
        "".join([phrase, end]).strip()
        for phrase, end in zip(even_elements, odd_elements)
    ]


def extract_names_from_phrases(text, allowed_names):
    # Let's start by downcasing some parts
    word0, rest = text.split(" ", maxsplit=1)
    text1 = " ".join([word0.lower(), rest])

    # Now let's grab any uppercase consecutive names
    pattern = r"\b(?:[A-Z][a-z]*\b\s*)+"
    names = [name.strip() for name in re.findall(pattern, text1)]
    names = {name for name in names if name in allowed_names}

    return names


def load_name_list(namelist_filename):
    names = set()
    with open(namelist_filename, encoding="utf-8") as file:
        for line in file:
            for word in line.split():
                word = word.replace('.', ' ').replace(',', ' ').strip()
                if word in ('The', 'and', 'Professor', 'Mr', 'Mrs', 'Madam'):
                    continue

                names.add(word)

    return names
