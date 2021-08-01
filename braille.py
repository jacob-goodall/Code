import time
print("Welcome to the Braille Encoder")
print("+-----------------------------+")
#time.sleep(2)
message = input("Please enter your message: ")
encoded = ""
for char in message:
    if char == "a" or char == "A":
        encoded += "⠁"
    elif char == "b" or char == "B":
        encoded += "⠃"
    elif char == "c" or char == "C":
        encoded += "⠉"
    elif char == "d" or char == "D":
        encoded += "⠙"
    elif char == "e" or char == "E":
        encoded += "⠑ "
    elif char == "f" or char == "F":
        encoded += "⠋"
    elif char == "g" or char == "G":
        encoded += "⠛"
    elif char == "h" or char == "H":
        encoded += "⠓"
    elif char == "i" or char == "I":
        encoded += "⠊"
    elif char == "j" or char == "J":
        encoded += "⠚"
    elif char == "k" or char == "K":
        encoded += "⠅"
    elif char == "l" or char == "L":
        encoded += "⠇"
    elif char == "m" or char == "M":
        encoded += "⠍"
    elif char == "n" or char == "N":
        encoded += "⠝"
    elif char == "o" or char == "O":
        encoded += "⠕"
    elif char == "p" or char == "P":
        encoded += "⠏"
    elif char == "q" or char == "Q":
        encoded += "⠟"
    elif char == "r" or char == "R":
        encoded += "⠗"
    elif char == "s" or char == "S":
        encoded += "⠎"
    elif char == "t" or char == "T":
        encoded += "⠞"
    elif char == "u" or char == "U":
        encoded += "⠥"
    elif char == "v" or char == "V":
        encoded += "⠧"
    elif char == "w" or char == "W":
        encoded += "⠺"
    elif char == "x" or char == "X":
        encoded += "⠭"
    elif char == "y" or char == "Y":
        encoded += "⠽"
    elif char == "z" or char == "Z":
        encoded += "⠵"
    else:
        encoded += char
print("Encoding message...")
print(encoded)

