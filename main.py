from stats import word_count
from stats import letter_count

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents
    
def main():
    book_text=get_book_text("books/frankenstein.txt")
    num_words = word_count(book_text)
    num_letters = letter_count(book_text)
    print(f"{num_words} words found in the document")
    print(num_letters)
main()