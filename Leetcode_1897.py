from collections import defaultdict

def makeEqual(words: list[str]):
    characterMap = defaultdict(int)

    for w in words:
        for c in w:
            characterMap[c] += 1

    for c in characterMap:
        if characterMap[c] % len(words):
            print("bhai false he")
            return False
    print("bhai true he")
    return True 
            

makeEqual(["ab","a"])