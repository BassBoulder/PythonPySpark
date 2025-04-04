def abbreviate(words):

    acronym = words[0].upper() if words else ""
    
    for index, char in enumerate(words):
        if char == ' ' or char == '-' or char == '_' and index + 1 < len(words):
            if words[index + 1].isalpha():
                acronym += words[index + 1].upper()

    return acronym