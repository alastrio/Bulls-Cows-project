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