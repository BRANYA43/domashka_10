"""Написати функцію, яка визначить, чи є введений текст паліндромом
(той який читається однаково з будь-якого боку), приклад:
Шалаш, зараз, Дід, Піп, 13231
Паліндром — і ні морд, ні лап"""
from string import punctuation


def delete_punctuation_from_text(text: str) -> str:
    for symbol in text:
        if symbol in punctuation:
            text = text.replace(symbol, '')
    return text


def is_palindrome(text: str) -> bool:
    text = delete_punctuation_from_text(text.lower().replace(' ', ''))
    if text == text[::-1]:
        return True
    else:
        return False


def main():
    print(is_palindrome('ШаЛаШ'))
    print(is_palindrome('Паліндром - і ні морд, ні лап'))


if __name__ == '__main__':
    main()
