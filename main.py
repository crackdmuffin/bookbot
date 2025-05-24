from stats import word_count
from stats import letter_count
from stats import report
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents
    
def main():
    if (len(sys.argv)-1) != 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text=get_book_text(sys.argv[1])
    num_words = word_count(book_text)
    num_letters = letter_count(book_text)
    book_report = report(num_letters)
    print("================ BOOKBOT ================\n")
    print("--------- Word Count ----------\n")
    print(f"Found {num_words} total words\n")
    print("------- Character Count -------\n")
    for i in book_report:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")
main()