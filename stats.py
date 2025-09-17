def get_num_words(some_text):
    parts = some_text.split()
    return len(parts)

def char_frequency(some_text):
    freq = {}
    for char in some_text:
        char = char.lower()
        freq[char] = freq.get(char, 0) + 1
    return freq