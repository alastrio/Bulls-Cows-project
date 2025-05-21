def random_num ():
    import random
    numbers = ["1","2","3","4","5","6","7","8","9","0"]
    num = ""
    while len(num) < 4:
        a = random.choice(numbers)
        if a not in num:
            num += a
    return num
random_num()