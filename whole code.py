import random


def get_answer ():
    answer = str(random.randint(1,9))
    while len(answer) < 4:
        a = str(random.randint(0,9))
        if a not in answer:
            answer += a
    return answer


def amount_animals(guess):
    cows = 0
    bulls = 0
    for i in range(4):
        if answer[i] == guess[i]:
            bulls += 1
        else:
            for i1 in range(4):
                if answer[i] == guess[i1]:
                    cows += 1
    return cows, bulls


answer = get_answer()
attempts = int(input("Введите число попыток: "))
print("Компьютер загадал 4-х значное число с неповторяющимися цифрами")
print(f"У вас есть {attempts} попыток, чтобы угадать его")


for k in range(attempts):
    guess = input("Введите ваше число (4-х значное): ")
    if len(guess) != 4 or not guess.isdigit() or len(set(guess)) != 4:
        print("Некорректный ввод. Убедитесь, что ввели уникальные 4 цифры")
        continue
    cows, bulls = amount_animals(guess)
    print(f"Коровы: {cows}, быки:{bulls}")
    if bulls == 4:
        print("Победа! Вы угадали число. Вы самый лучший человек на свете!")
        break
else:
    print(f"Вы исчерпали все попытки. Правильный ответ: {answer}")
