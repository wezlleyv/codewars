def remove_char(s):
    text = ''
    for letter in range(len(s)):
        if letter == 0 or letter == len(s)-1:pass
        else: text += s[letter]
    return text

print(remove_char("abcde"))