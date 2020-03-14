import fileinput
import re

# Separar o texto por páginas.
def prePage(filename):
    with open(filename,encoding="utf-8") as file:
        text = file.read()
    aux = re.split(r"(Page \| [1-9]+\s.*)", text)
    return aux
    



