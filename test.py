surnames = ["Shevchenko", "Vasilenko", "Ovcharenko", "Borisenko"]
domains = ["eu", "org", "best", "beer"]


def generation_email():
    import string, random
    from random import randint, choice
    name = choice(surnames)
    domain = choice(domains)
    random_number = randint(100, 999)
    rand_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(randint(5, 7)))
    e_mail = (f'{name}.{random_number}@{rand_string}.{domain}').lower()
    return e_mail


print(generation_email())
