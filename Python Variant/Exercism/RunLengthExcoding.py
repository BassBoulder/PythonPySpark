def decode(string):
    decodedString = ''
    count = ''

    for char in string:
        if char.isdigit():
            count += char  # Keep building the number if it's multi-digit
        else:
            volumeOfChar = int(count) if count else 1
            decodedString += char * volumeOfChar
            count = ''  # Reset count for the next group

    return decodedString
    

def encode(string):
    encodedString = ''
    volumeOfChar = 1

    if string == "":
        return ""

    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            volumeOfChar += 1
        else:
            if volumeOfChar == 1:
                encodedString += string[i - 1]
            else:
                encodedString += str(volumeOfChar) + string[i - 1]
            volumeOfChar = 1

    if volumeOfChar == 1:
        encodedString += string[-1]
    else:
        encodedString += str(volumeOfChar) + string[-1]

    return encodedString