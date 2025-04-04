##+1 (613)-995-0253
##613-995-0253
##1 613 995 0253
##613.995.0253



import re

class PhoneNumber:
    def __init__(self, number):

        self.phoneNumberSegments = re.split(r'[-, ,.]', number)


phone = PhoneNumber("+1 (613)-995-0253")



print(phone.phoneNumberSegments)