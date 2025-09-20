from stats import get_num_words, char_frequency, sort_char_counts

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(text)
    # Call your new function and store the result
    char_counts = char_frequency(text)
    sorted_chars = sort_char_counts(char_counts)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    # Print the character counts dictionary as per assignment
    print("--------- Character Count -------")
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()