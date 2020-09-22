# Armstrong Number
def Armstrong_YN(s):
    currSum = 0
    number_length = len(s)
    number_int = int(s)

    for char in s:
        currNbr = int(char)
        powNbr = currNbr**number_length
        currSum += powNbr

    if currSum == number_int:
        return s + ' is an Armstrong number!'
    else:
        return s + ' is not an Armstrong number.'

print(Armstrong_YN(input('Enter a number:').strip()))
