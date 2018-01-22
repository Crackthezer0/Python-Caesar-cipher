# Ask the user to enter a string to encrypt
regularString = input("Please input a string to encode: ")

# Ask by how many spaces they would like to shift the alphabet
shiftAmount = input("Please enter a value between -25 and 25: ")
# Ask if the user would like to shift left or right by the above amount
#direction = input("Would you like to shift right or left? ")

coded_string = ""

# when a letter is shifted it will sometimes exceeds the range of letters in the alphabet
# if this happens the shift will start from the beginning of the alphabet and continue from there
def uperRangeCorr(upper):
    if upper > 90:
        upper -= 26
        return upper
    elif upper < 65:
        upper += 26
        return upper
    else:
        return upper

def lowerRangeCorr(lower):
    if lower > 122:
        lower -= 26
        return lower
    elif lower < 97:
        lower += 26
        return lower
    else:
        return lower

# Shift the alphabet according to the number provided by the user
for char in regularString:

    if char.isalpha() is True:
        if (char.isupper()) is True:
            unicode = ord(char)
            uppershift = unicode + int(shiftAmount)

            coded_string += chr(uperRangeCorr(uppershift))

        elif (char.isupper()) is False:
            unicode = ord(char)
            lowershift = unicode + int(shiftAmount)

            coded_string += chr(lowerRangeCorr(lowershift))
    else:
        coded_string += char


print(coded_string)


decipheredString = ""

# Unscramble the text by shifting the letters the opposite way they were scrambled
for char in coded_string:

    if char.isalpha() is True:
        if (char.isupper()) is True:
            unicode = ord(char)
            uppershift = unicode - int(shiftAmount)

            decipheredString += chr(uperRangeCorr(uppershift))

        elif char.isupper() is False:
            unicode = ord(char)
            lowershift = unicode - int(shiftAmount)

            decipheredString += chr(lowerRangeCorr(lowershift))
    else:
        decipheredString += char

print(decipheredString)

