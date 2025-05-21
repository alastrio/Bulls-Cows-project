def get_answer ():
    import random
    numbers = ["1","2","3","4","5","6","7","8","9","0"]
    answer = ""
    while len(answer) < 4:
        a = random.choice(numbers)
        if a == "0" and len(answer) == 0:
            break
        elif a not in answer:
                answer += a
    return answer