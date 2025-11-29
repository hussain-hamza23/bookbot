from stats import number_of_words, number_of_each_character, sort_characters, sort_on
import sys

def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()

def text(book):
    #file_path = "/home/hussainhamza/Projects/python/bookbot/bookbot/books/"
    book_text = get_book_text(sys.argv[1])
    return book_text


def analysis(number_of_words,file_path):
   
    print("============ BOOKBOT ============")
    print(f"Analyzing book at: {file_path}")
    print("----------- Word Count ----------")
    print(f'Found {number_of_words} total words')
    print("--------- Character Count -------")
    sort_characters(number_of_each_character(text(file_path)))
    print("============= END ===============")

def main():
    analysis(number_of_words(text(sys.argv[1])),sys.argv[1])

print("Usage: python3 main.py <path_to_book>")
main()