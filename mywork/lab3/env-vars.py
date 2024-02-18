#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3

import os

os.environ["FAVORITE_BOOK"] = input("What is your favorite book? ")
os.environ["HOMETOWN"] = input("What is your hometown? ")
os.environ["PET_NAME"] = input("What is your pet's name? ")

print("Favorite Book:", os.getenv("FAVORITE_BOOK"))
print("Hometown:", os.getenv("HOMETOWN"))
print("Pet's Name:", os.getenv("PET_NAME"))