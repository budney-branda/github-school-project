import random

def get_random_code():
    numbers = "1234567890"
    symbols = "@#$%^&*()_+-="
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    codes = ""
    for i in range(10):
        code = ""
        for j in range(5):
            code += random.choice(numbers)
        for k in range(3):
            code += random.choice(symbols)
        for l in range(2):
            code += random.choice(characters)
        codes += code + "\n"
    return codes
