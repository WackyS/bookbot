def main():
    path = "books/frankenstein.txt"
    file_contents = get_book_text(path)
    word_count = get_word_count(file_contents)
    character_count_dict = get_character_count_dict(file_contents)
    print_report(path, word_count, character_count_dict)


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents


def get_word_count(text):
    return len(text.split())

def get_character_count_dict(text):
    dictionary = {}
    for char in text.lower():
        if dictionary.get(char) is None:
            dictionary[char] = 1
        else:
            dictionary[char] += 1
    return dictionary

def print_report(path, word_count, character_count_dict):
    print(f"--- Begin report of {path} ---\n"
          f"{word_count} words found in the document\n")
    character_count_list = get_character_list(character_count_dict)
    for item in character_count_list:
        print(f"The '{item['char']}' character was found {item['count']} times")
    print("--- End report ---")


def get_character_list(character_count_dict):
    character_count_list = []
    for k, v in character_count_dict.items():
        if k.isalpha():
            new_item = {
                "char": k,
                "count": v
            }
            character_count_list.append(new_item)

    def sort_on(dictionary):
        return dictionary["count"]

    character_count_list.sort(reverse=True, key=sort_on)
    return character_count_list


if __name__ == "__main__":
    main()