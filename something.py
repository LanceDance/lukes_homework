import random
def generate_numbers():
    list_of_numbers = []
    while len(list_of_numbers) < 4:
        number = random.randint(0,9)
        if number in list_of_numbers:
            pass
        else:
            list_of_numbers.append(number)
    print(list_of_numbers)
    return list_of_numbers




def users_numbers():
    user_input = input('Send me the numbers(only 4): ')
    if len(user_input) != 4:
        user_input = input('EXACTLY 4 NUMBERS! TRY AGAIN: ')
    list_of_users_numbers = []
    for i in user_input:
        list_of_users_numbers.append(int(i))
    return list_of_users_numbers




def compare_two_list(generates_numbers, users_numbers):
    # nastaveni bulls a cows na nulu
    bulls = 0
    cows = 0
    correct_numbers = []
    guesses = 0
    # tady porovnavame oba listy
    for i, j in zip(generates_numbers, users_numbers):
        # pokud jsou na stejne pozici stejna cisla, tak zvysime bulls o 1
        if i == j:
            bulls += 1
            correct_numbers.append(i)
        # pokud jsou cisla jen stejna, tak zvysime cows o 1
        elif i in users_numbers:
            cows += 1
    # vysledek vratime v listu (pocet cows a bulls)
    return [cows,bulls]


# tady volame vsechny methody
calling_method_for_numbers = generate_numbers()
calling_method_for_users_numbers = users_numbers()
# do result si ulozime vysledek z porovnavani
result = compare_two_list(calling_method_for_numbers,calling_method_for_users_numbers)
guesses = 1
# tady projedeme loopou to, jestli se hrac trefil
while True:
    # tady zkoumame, jestli je v promenne result na 1. miste nejake jine cislo nez 0,
    #  tak je jasny, ze se uzivatel trefil, to stejne s 2. cilslem. Pokud jo, loopu muzeme ukoncit
    if result[0] >= 1 or result[1] >= 1:
        print('Hey, good job, some numbers are the same! And you got bulls ' + str(result[1]) + ' and cows '
                  + str(result[0]) + ' in the ' + str(guesses) + ' guess!')
        break

    else:
        # netrefil se, tak to bude opakovat znovu
        print('No luck, try one more time')
        other_attempt = users_numbers()
        result = compare_two_list(calling_method_for_numbers, other_attempt)
        guesses += 1
