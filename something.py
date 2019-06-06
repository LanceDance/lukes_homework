import random

def generate_numbers():
    list_of_numbers = []
    while len(list_of_numbers) < 5:
        number = random.randint(0,9)
        if number in list_of_numbers:
            pass
        else:
            list_of_numbers.append(number)

    return list_of_numbers


calling_method_for_numbers = generate_numbers()


def users_numbers():
    user_input = input('Send me the numbers(only 5): ')

    if len(user_input) != 5:
        user_input = input('EXACTLY 5 NUMBERS! TRY AGAIN: ')
    list_of_users_numbers = []
    for i in user_input:
        list_of_users_numbers.append(int(i))
    return list_of_users_numbers


calling_method_for_users_numbers = users_numbers()


def compare_two_list(generates_numbers, users_numbers):
    correct_numbers = []
    for i, j in zip(generates_numbers, users_numbers):
        if i == j:
            correct_numbers.append(i)
    if correct_numbers:
        print('Hey, good job, some numbers are the same!'+ str(correct_numbers))

    else:
        print('Pweee, you are looser! ')


compare_two_list(calling_method_for_numbers,calling_method_for_users_numbers)