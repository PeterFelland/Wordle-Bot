def score(word, source) -> int:
    score = 0
    for c in word:
        score += source[c]
    return score

def uniqueWord(word) -> bool:
    letterSet = set()
    for c in word:
        letterSet.add(c)
    return len(letterSet) == 5