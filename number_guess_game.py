import random

num_to_guess = random.randrange(1, 101)
print("Добро пожаловать в числовую угадайку!")


def is_valid(number):
    return number in range(1, 101)


user_guess = int(input("Попробуйте отгадать число! Оно может быть любым от 1 до 100: "))
counter = 1

while True:
    if not is_valid(user_guess):
        user_guess = int(input("А может быть все-таки введем целое число от 1 до 100? "))
        continue
    if user_guess == num_to_guess:
        print(f"\nВы угадали число за {counter} попыток, поздравляем!")
        break
    elif user_guess < num_to_guess:
        user_guess = int(input("Ваше число меньше загаданного, попробуйте еще разок: "))
    elif user_guess > num_to_guess:
        user_guess = int(input("Ваше число больше загаданного, попробуйте еще разок: "))

    counter += 1

print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
