def split_text(text):
    partitioned = text.partition("\n")
    splitted = text.split("\n")
    
    return partitioned, splitted


print(split_text("hello\nWorld!"))