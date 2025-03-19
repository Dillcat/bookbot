
def word_count(text):

    num_words = []
    num_words = text.split()
    
    
    return len(num_words)

def character_count(text):
    
    characters = []
    char_dict = {}
    count = 0

    characters = list(text.lower())

    character_type = set(characters)

    character_type_list = list(character_type)

    for c in character_type_list:
        count = 0
        for character in characters:

            if character == c:
                count += 1
        char_dict[c] = count
    
    return char_dict


def unorganized_list(dictionary):
    
    unorg_list = []
    
    for c in dictionary:
        n = dictionary[c]
        unorg_list.append({"c": c,"n": n})

    return unorg_list

def sort_on(dictionary):
    return dictionary["n"]


    