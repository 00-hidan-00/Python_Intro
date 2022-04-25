def read_file(filename):
    with open(filename, 'r') as my_file:
        data = my_file.read()
    return data


# 1

def returns_domains(filename='domains.txt') -> list:
    domains = []
    for line in read_file(filename).split('\n'):
        if line:
            domains.append(line[1:])
    return domains


result_1 = returns_domains()


# 2

def return_surnames(filename='names.txt') -> list:
    surnames = []
    for line in read_file(filename).split('\n'):
        if line:
            surname = line.split('\t')[1]
            surnames.append(surname)
    return surnames


result_2 = return_surnames()


# 3

def return_calendar_dates(filename: str) -> list:
    calendar_dates = []
    for line in (read_file(filename).split('\n')):
        if '-' in line:
            calendar_date = line.split('-')[0]
            calendar_dates.append({"date": calendar_date})
    return calendar_dates


result_3 = return_calendar_dates('authors.txt')

print(result_3)
