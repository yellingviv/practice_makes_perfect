# challenge: https://gist.github.com/seemaullal/eab0853325b70aa41d211cdf7259ddc9

def check_similarity(word1, word2):
    """check if word1 and word2 are only one character different"""

    similar = False
    counter = 0
    range_len = 0

    if len(word1) - len(word2) not in (-1, 1, 0):
        return similar
    elif len(word1) > len(word2):
        range_len = len(word2)
        counter += 1
    elif len(word1) < len(word2):
        range_len = len(word1)
        counter += 1
    elif len(word1) == len(word2):
        range_len = len(word1)

    for i in range(range_len):
        if word1[i] != word2[i]:
            if counter >= 1:
                return similar
            counter += 1

    similar = True

    return similar

# test cases I used:
# nifty, nifto
# nifty, nofto
# howdy, hellothere
# asks, ask
# asta, ask 
