def num2bin(number):
    binary_number = bin(number)
    return binary_number

def checkInput(inputNumber, binary):
    new_binary = binary << inputNumber
    return(new_binary % 2)