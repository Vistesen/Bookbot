from stats import get_num_words, char_frequency

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")

if __name__ == "__main__":
    main()q = char_frequency(text)
    #print(text)


main()