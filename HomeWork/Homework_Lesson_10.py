# 1

def returns_domains(filename: str) -> list:
    with open(filename, 'r') as my_file:
        data = my_file.read()
        domains = []
        for line in data.split('\n'):
            if line:
                domains.append(line[1:])
        return domains


result_1 = returns_domains('domains.txt')


# 2

def return_surnames(filename: str) -> list:
    with open(filename, 'r') as my_file:
        data = my_file.read()
        surnames = []
        for line in data.split('\n'):
            if line:
                surname = line.split('\t')[1]
                surnames.append(surname)
        return surnames


result_2 = return_surnames('names.txt')


# 3

def return_calendar_dates(filename: str) -> list:
    with open(filename, 'r') as my_file:
        data = my_file.read()
        calendar_dates = []
        for line in (data.split('\n')):
            if '-' in line:
                calendar_date = line.split('-')[0]
                calendar_dates.append({"date": calendar_date})
        return calendar_dates


result_3 = return_calendar_dates('authors.txt')
