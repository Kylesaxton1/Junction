import time

userName = input("What is your name?")
print("This is a Junction Program, you will input two strings and we will return to you the shared characters, or junction between them")

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
NUMBERS = "1234567890"
VOWELS = "AEIOUaeiou"

METRICS = [LETTERS,VOWELS,NUMBERS]

time.sleep(1)
inputOne = input("What is the first string that you want to enter?")
inputTwo = input("What is the secod=nd string that you want to enter?")

junct = ''

for c in inputOne:
  if c in inputTwo and c not in junct:
    junct += c
    
print(junct)
vowels = 0
letters = 0
numbers = 0

for i in junct:
  if i in LETTERS:
    letters += 1
    if i in VOWELS:
      vowels += 1
   if i in NUMBERS:
    numbers += 1
    
print("of the characters that the two share,", vowels, "of them are vowels")
print("of the characters that the two share,", numbers, "of them are numbers")
