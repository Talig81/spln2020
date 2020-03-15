import fileinput
import re


def getTexto():
    texto = ""

    for line in fileinput.input():
        texto += line

    return texto


def entidades(texto):
    maius = r"(?:[A-Z]\w+(?:[-\']\w+)*|[A-Z]\.|[IVXLCDM]+)"
    de = r"(?:de|da|dos|das)"
    # ent = '(' + maiuscula + '(?: ' + maiuscula + '| ' + de + ' ' + maiuscula + ')*' + ')'

    s = r"\s+"
    ent = f"([^@\w])({maius}(?:{s}{maius}|{s}{de}{s}{maius})*)"

    texto = re.sub(ent, r"\1{\2}", texto)
    return texto


def frases(texto):
    exp1 = r"(\n\n+\s*)([A-Z])"
    exp2 = r"([a-z][.?!]+[\s]*)([A-Z])"

    texto = re.sub(exp1, r"\1@\2", texto)
    texto = re.sub(exp2, r"\1@\2", texto)

    return texto


print(entidades(frases(getTexto())))
