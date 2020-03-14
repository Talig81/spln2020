import re



def setenceGen():
    with open("leguminous.txt",encoding="utf-8") as file:
        text = file.read()
    setenceArray = re.split(r"(\s[^A-Z][a-z]+\.)", text)
    print(setenceArray[6]  + setenceArray[7])
    
    

setenceGen()
    
