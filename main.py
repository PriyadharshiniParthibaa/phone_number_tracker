import phonenumbers
from phonenumbers import geocoder
a = input('enter the phonenumber: ')
phonenumber = phonenumbers.parse(a)
print(geocoder.description_for_number(phonenumber, "en" ))