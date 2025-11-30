import sys
from stats import count_words,count_letters,sort_dictionary

def get_book_text(filepath:str) -> str:
   with open(filepath) as f:
      file_contents = f.read()
      return file_contents

def main(args) -> None:
    """Entry point for the script."""
    # Use a relative path to locate the file within the repository
    if len(args) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)    
    
    book_path = args[1]
    
    # Read the entire book into a string
    book_text = get_book_text(book_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    num_words = count_words(book_text)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sorted = sort_dictionary(count_letters(book_text))
    for s in sorted:
        if s["char"].isalpha():
            print(f"{s['char']}: {s['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main(sys.argv)