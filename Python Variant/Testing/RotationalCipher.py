def rotate(text, key):

    plain = "abcdefghijklmnopqrstuvwxyz"
    cipher = "nopqrstuvwxyzabcdefghijklm"
    answer = ""

    if 0 < key <=26:
        for char in text:
            index = cipher.index(char) + key
            answer += cipher[index]
            
    return answer

print(rotate("a", 0))