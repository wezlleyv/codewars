def to_jaden_case(string):
    list_text = []
    final_text = ""
    text_splited = string.lower().split()
    
    for word in text_splited:
        cache = ''
        for posLetter in range(len(word)):
            if posLetter == 0:
                cache += word[posLetter].upper()
            else: cache += word[posLetter]

        list_text.append(cache)

    for word in range(len(list_text)):
        if word == len(list_text): final_text += list_text[word]
        else: final_text += list_text[word] + " "

    return final_text

    

print(to_jaden_case("How can mirrors be real if our eyes aren't real"))