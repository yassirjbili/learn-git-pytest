# Exercise 2: String Utilities


def reverse_string(s: str) -> str:
    reversed_str = ""
    for i in range(len(s)-1, -1, -1):
        reversed_str += s[i]
    return reversed_str


def count_vowels(s: str) -> int:
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count


def is_palindrome(s: str) -> bool:
    cleaned_str = ''.join(s.split()).lower()
    return cleaned_str == cleaned_str[::-1]


def capitalize_words(s: str) -> str:
    b = s.title()
    return b
