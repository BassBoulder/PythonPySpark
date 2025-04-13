colourDict = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4, "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9}

def label(colors):
    answer = ""
    formated_answer = ""
    iter = 0
    i = 0

    colors = colors[:3]
    
    for color in colors:
        
        if color in colourDict.keys() and iter < 2:
            answer += str(colourDict.get(color))
            iter += 1

        elif iter == 2:

            for i in range(0, colourDict.get(color)):
                answer += "0"


        if len(answer) > 8:
            formated_answer = (f"{int(int(answer) / 1000000000)} gigaohms")        
        elif len(answer) > 7:
            formated_answer = (f"{int(int(answer) / 1000000)} megaohms")
        elif len(answer) > 3:
            formated_answer = (f"{int(int(answer) / 1000)} kiloohms")
        else:
            formated_answer = (f"{int(answer)} ohms")

    return formated_answer