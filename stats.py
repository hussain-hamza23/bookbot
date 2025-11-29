def number_of_words(text):
    words = text.split()
    return len(words)

def number_of_each_character(text):
    number_of_characters = {}

    for character in text:
        if character.lower() in number_of_characters:
            number_of_characters[character.lower()] += 1
        else:
            number_of_characters[character.lower()] = 1
    return number_of_characters

def sort_on(item):
    return item['count']

def sort_characters(character_dict):
    character_list = []
    for character, count in character_dict.items():
        if character.isalpha():
            character_list.append({'character': character, 'count': count})
     
    character_list.sort(reverse=True, key=sort_on)

    for item in character_list:
        print(f"{item['character']}: {item['count']}")