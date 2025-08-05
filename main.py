import sys 

from stats import get_num_words, get_chars_dict


def main():
    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print(f"Found {num_words} total words")
    get_report(chars_dict)
    


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_report(chars_dict):
    sorted_dict = dict(sorted(chars_dict.items(), key=lambda item: item[1], reverse=True))
    # Got help here: https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
    for i in sorted_dict:
        if i.isalpha():
            print(f"{i}: {sorted_dict[i]}")


main()
