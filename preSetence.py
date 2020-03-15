import re


def preSetence(pageArray):
    pageDic = {}
    pageDic["1"] = pageArray[0]
    for i, string in enumerate(pageArray):
        if i % 2 == 1 and i + 1 < len(pageArray):
            pageDic[string[7]] = pageArray[i + 1]
    return pageDic
