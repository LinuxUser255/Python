#!/usr/bin/env python3


def get_language(prog_lang, type_lang):
    """Get's the formatted output"""
    full_lang = f"{prog_lang} {type_lang}"
    return full_lang.title()


while True:
    print("\nWhat programing are you learning? ")
    print("(press 'q' anytime to exit)")

prog_lang = input("Language name: ")
#formatted_language = get_formatted_language(prog_lang, type_lang)

if prog_lang == 'q'
    break
