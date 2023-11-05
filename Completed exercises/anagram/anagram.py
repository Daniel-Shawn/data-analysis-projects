def find_anagrams(word, candidates):
    word = word.lower()
    new_candidates = []
    temp_candidates = []

    for each in candidates:
        temp_candidates.append(each.lower())

    for each in temp_candidates:
        if each == word or len(each) != len(word):
            pass
        else:
            new_candidates.append(each)

    return new_candidates


find_anagrams("diaper", ["hello", "world", "zombies", "pants"])

