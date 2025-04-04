import string
import re

symbols = re.sub('[-.+()]','',string.punctuation)

class PhoneNumber:
    def __init__(self, number):

        phoneNumberCleaned = []

        for char in number:
            
            if char.isalpha():
               raise ValueError("letters not permitted")
            if char in symbols:
               raise ValueError("punctuations not permitted")
                
            if char.isdigit():
                phoneNumberCleaned.append(char);
            
        # if a phone number has less than 10 digits.        
        if len(phoneNumberCleaned) < 10:
            raise ValueError("must not be fewer than 10 digits")
        # if a phone number has more than 11 digits.
        if len(phoneNumberCleaned) > 11:
            raise ValueError("must not be greater than 11 digits")
            
        # if a phone number has 11 digits, but starts with a number other than 1.
        if len(phoneNumberCleaned) == 11: 
            if phoneNumberCleaned[0] != '1':
                raise ValueError("11 digits must start with 1")
            phoneNumberCleaned.remove('1')

        # if a phone number has an area code that starts with 0.
        if phoneNumberCleaned[0] == '0':
            raise ValueError("area code cannot start with zero")
        # if a phone number has an area code that starts with 1.
        if phoneNumberCleaned[0] == '1':
            raise ValueError("area code cannot start with one")
        # if a phone number has an exchange code that starts with 0.
        if phoneNumberCleaned[3] == '0':
            raise ValueError("exchange code cannot start with zero")
        # if a phone number has an exchange code that starts with 1.
        if phoneNumberCleaned[3] == '1':
            raise ValueError("exchange code cannot start with one")

        self.number = ''.join(phoneNumberCleaned)
        self.area_code = self.number[:3]
        
    def pretty(self):
        prettyNumber = self.number
        return f"({prettyNumber[0:3]})-{prettyNumber[3:6]}-{prettyNumber[6:]}"