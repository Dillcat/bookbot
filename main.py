def main():

    path_to_file = "books/frankenstein.txt"

    text = get_book_text(path_to_file)

    word = word_count(text)

    return print(f"{word} words found in the document")
    #print(word_count() + "words found in the document")

def get_book_text(path_to_file):


    with open(path_to_file) as f:
        # opens the text, does something with f(file)
        file_contents = f.read()
        # stores file contents as a string

    return file_contents

def word_count(text):

    num_words = []
    num_words = text.split()
    
    
    return len(num_words)

main()