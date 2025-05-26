def flatten(iterable):
    
    flat_list = []

    for i in iterable:
        
        try:
            flat_list += flatten(i)
            
        except:
            if i is not None:
                flat_list.append(i)

    return flat_list