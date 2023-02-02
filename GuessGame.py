import random

def generate_number(difficulty):
    print(difficulty)
    secret_number = random.randint(0, difficulty)
    print(secret_number)
    return secret_number

def get_guess_from_user(difficulty):
    num = input("Choose a Number: ")
    return num

def compare_results(secret_number, num):
    print("SN:" ,secret_number)
    print("NUM:", num)
    if secret_number == num:
        return True
    else:
        return False
