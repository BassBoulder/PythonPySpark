def line_up(name, number):
    name = name
    number = number
    suffix = ""


    if 11 <= number % 100 <= 13:
        
        suffix = "th"
        
    else:
        
        if number % 10 == 1:
            suffix = "st"
    
        elif number % 10 == 2:
            suffix = "nd"
    
        elif number % 10 == 3:
            suffix = "rd"

        else: 
            suffix = "th"

    #1st, 2nd ,3rd
    #10th, 11th, 12th,
    #20th, 21st, 22nd, 23rd <<< need to break down these rules
        
    
    return (f"{name}, you are the {number}{suffix} customer we serve today. Thank you!")