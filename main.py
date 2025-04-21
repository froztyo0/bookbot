import sys
from stats import count_words,character_count
def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
    
def main(file_path):
    book_text = get_book_text(file_path)
    num_words = count_words(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    dict = character_count(book_text)
    for x in dict:
        print(f"{x}:",dict[x])

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    file_path = sys.argv[1]
    main(file_path)