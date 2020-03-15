from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen(
    "https://www.gradesaver.com/harry-potter-and-the-philosophers-stone/study-guide/character-list"
)
soup = BeautifulSoup(html.read(), "html.parser")
unprocessed_volume = soup.findAll("h2")
characters_array = [volume.string for volume in unprocessed_volume]
with open("characters_names.txt", "w") as out:
    for char in characters_array[1:]:
        out.write(char.string + "\n")
