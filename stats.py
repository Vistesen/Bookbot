def get_num_words(some_text):
    parts = some_text.split()
    return len(parts)

def char_frequency(some_text):
    freq = {}
    for char in some_text:
        char = char.lower()
        freq[char] = freq.get(char, 0) + 1
    return freq

def sort_char_counts(char_counts):
    char_list = [{"char": char, "num": count} for char, count in char_counts.items()]
    def get_num(item):
        return item["num"]
    char_list.sort(key=get_num, reverse=True)
    return char_list

