import re

class PhoneNumber:
    def __init__(self, number):

        self.phoneNumberCleaned = number \
            .replace("+1","")\
            .replace("1 ","")\
            .replace("(","")\
            .replace(")","")\
            .replace("-","")\
            .replace(".","")\
            .replace(" ","")
        
        # if a phone number has less than 10 digits.        
        if len(self.phoneNumberCleaned) < 10:
            raise ValueError("must not be fewer than 10 digits")
            
        # if a phone number has more than 11 digits.
        if len(self.phoneNumberCleaned) > 11:
            raise ValueError("must not be greater than 11 digits")
            
        # if a phone number has 11 digits, but starts with a number other than 1.
        if len(self.phoneNumberCleaned) == 11 and self.phoneNumberCleaned[0] != 1:
            raise ValueError("11 digits must start with 1")

        # if a phone number has valid size/
        if len(self.phoneNumberCleaned) == 10:
            # if a phone number has an exchange code that starts with 0.
            if self.phoneNumberCleaned[4] == 0:
                raise ValueError("exchange code cannot start with zero")
            # if a phone number has an exchange code that starts with 1.
            if self.phoneNumberCleaned[4] == 1:
                raise ValueError("exchange code cannot start with one")
            # if a phone number has an area code that starts with 0.
            if self.phoneNumberCleaned[0] == 0:
                raise ValueError("area code cannot start with zero")
            # if a phone number has an area code that starts with 1.
            if self.phoneNumberCleaned[0] == 1:
                raise ValueError("area code cannot start with one")

        # if a phone number has punctuation in place of some digits.
        if re.findall(r"[^\w\s]", self.phoneNumberCleaned):
            raise ValueError("punctuations not permitted")

        # if a phone number has letters in place of some digits.
        if re.findall(r"[^\d]", self.phoneNumberCleaned):
            raise ValueError("letters not permitted")

phone = PhoneNumber("+1 (613)-995-0253")



print(phone.phoneNumberCleaned)