def get_number_of_text (bookText):
    text_list = bookText.split()

    return len(text_list)

def get_character_count (book_text):
    result = {}
    for character in book_text:
        lower_case = character.lower()
        if lower_case not in result:
            result[lower_case] = 1
        else:
            result[lower_case] = result[lower_case] + 1

    return result

def sort_on (dict):
    return dict["num"]

def sort_character_count(character_count_dic):
    result = []

    for character in character_count_dic:
        count_dict = {}
        count_dict["character"] = character
        count_dict["num"] = character_count_dic[character]
        result.append(count_dict)

    result.sort(reverse=True, key=sort_on)

    return result