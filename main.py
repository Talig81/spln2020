import prePaging
import preSetence

nameFile = "notVeggies.txt"

def main():
    newVar = prePaging.prePage(nameFile)
    newArray = preSetence.preSetence(newVar)
    

main()