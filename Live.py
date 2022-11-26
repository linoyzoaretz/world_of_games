def welcome(name):
    print(f'''Hello {name} and welcome to the World of Games (WoG).
    Here you can find many cool games to play. ''')

def load_game():
    print('''
    Please choose a game to play:
    1. Memory Game - a sequence of numbers will appear for 1 second and you have to
    guess it back
    2. Guess Game - guess a number and see if you chose like the computer
    3. Currency Roulette - try and guess the value of a random amount of USD in ILS
    ''')
    game = int(input("choose game\n"))
    while game > 3:
        print("please choose a game between 1 to 3")
        game = int(input("choose game\n"))

    print("ok", game)
    difficulty = int(input("choose difficulty level from 1 to 5\n"))
    while difficulty > 5:
        print("please choose difficulty level between 1 to 5 only!\n")
        difficulty = int(input("choose difficulty level from 1 to 5\n"))

    print("you chose", difficulty)