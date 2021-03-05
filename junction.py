import time

userName = input("What is your name?")
print("This is a Junction Program, you will input two strings and we will return to you the shared characters, or junction between them")

time.sleep(1)
inputOne = input("What is the first string that you want to enter?")
inputTwo = input("What is the secod=nd string that you want to enter?")

junct = ''

for c in inputOne:
  if c in inputTwo and c not in junct:
    junct += c
    
print(junct)
