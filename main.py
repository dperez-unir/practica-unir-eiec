"""
License: Apache
Organization: UNIR
"""
from googletrans import Translator
import os
import sys

DEFAULT_FILENAME = "daniel.txt"
DEFAULT_DUPLICATES = False


def sort_list(items, ascending=True):
    if not isinstance(items, list):
        raise RuntimeError(f"Error: can't order {type(items)}")

    return sorted(items, reverse=(not ascending))


def remove_duplicates_from_list(items):
    return list(set(items))

def translate_to_english(text):
    translator = Translator()
    if text:
        print(f"Original: {text}")
        translation = translator.translate(text, src='es', dest='en')
        print(f"Traducción: {translation.text}")
        return translation.text
    else:
        return ''


if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    if len(sys.argv) == 3:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
    else:
        print("The file must be indicated as the first argument")
        print("The second argument indicates whether you want to eliminate duplicates")
        sys.exit(1)

    print(f"The words from the file will be read {filename}")
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(translate_to_english(line.strip()))
    else:
        print(f"The file {filename} don't exist")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)

    print(sort_list(word_list))
