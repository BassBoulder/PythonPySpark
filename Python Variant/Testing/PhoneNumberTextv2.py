##+1 (613)-995-0253
##613-995-0253
##1 613 995 0253
##613.995.0253



import re

class PhoneNumber:
    def __init__(self, number):

        self.phoneNumberSegments = number \
            .replace("+1","")\
            .replace("1 ","")\
            .replace("(","")\
            .replace(")","")\
            .replace("-","")\
            .replace(".","")\
            .replace(" ","")


phone = PhoneNumber("+1 (613)-995-0253")



print(phone.phoneNumberSegments)