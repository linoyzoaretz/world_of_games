from GuessGame import generate_number, get_guess_from_user, compare_results
from MemoryGame import generate_sequence, get_list_from_user, is_list_equal
from CurrencyRouletteGame import get_money_interval, get_guess_from_user

difficulty = 5
secret_number = generate_number(difficulty)
num = get_guess_from_user(difficulty)
compare = compare_results(secret_number, num)
print(compare)