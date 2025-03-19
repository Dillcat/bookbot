from stats import word_count
from stats import character_count
from stats import sort_on
from stats import unorganized_list
import sys

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_file = sys.argv[1]
    

    print("============ BOOKBOT ============")
    text = get_book_text(path_to_file)
    word = word_count(text)

    print("----------- Word Count ----------")
    print(f"Found {word} total words")
    dictionary = character_count(text)

    print("--------- Character Count -------")
    organized_list = unorganized_list(dictionary)
    sort_on(dictionary)    
    organized_list.sort(reverse=True, key=sort_on)

    for n in organized_list:
        org_list = []
        for k in n:
            org_list.append(n[k])
        print(f"{str(org_list[0])}: {str(org_list[1])}")

    print("============= END ===============")

    print("")

    return None

def get_book_text(path_to_file):


    with open(path_to_file) as f:
        # opens the text, does something with f(file)
        file_contents = f.read()
        # stores file contents as a string

    return file_contents

main()