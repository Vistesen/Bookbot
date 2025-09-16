def get_book_text(file_path):
    with open(file_path) as f:
        return f.read() 

def count_words(some_text):
    parts = some_text.split()
    return len(parts)

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = count_words(text)
    print(f"{num_words} words found in the document")
    #print(text)


main()