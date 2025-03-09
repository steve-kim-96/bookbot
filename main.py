from stats import *
import sys

def get_book_text (path_to_file):
    with open(path_to_file) as f:
        return f.read()
    
    
def main ():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    num_words = get_character_count(book_text)
    character_count = sort_character_count(num_words)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print("Found 75767 total words")
    print("--------- Character Count -------")
    for count_dict in character_count:
        if count_dict["character"].isalpha():
            print(f"{count_dict["character"]}: {count_dict["num"]}")

    print("============= END ===============")

main()
