def abbreviate(words):
    words = words.upper()
    if '-' in words:
        words = words.replace('-', ' ')
    if '_' in words:
        words = words.replace('_', ' ')

    temp_array = words.split()
    temp_str = ''
    for each_word in temp_array:
        temp_str += each_word[0]
    return temp_str


