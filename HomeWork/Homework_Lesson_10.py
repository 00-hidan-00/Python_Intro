# 1

def returns_domains(filename: str) -> list:
    with open(filename, 'r') as my_file:
        data = my_file.read()
        domains_list = []
        for line in data.split('\n'):
            if line:
                domains_list.append(line[1:])
        return domains_list


result_1 = returns_domains('domains.txt')


# 2

def return_surnames(filename: str) -> list:
    with open(filename, 'r') as my_file:
        data = my_file.read()
        surnames_list = []
        for line in data.split('\n'):
            if line:
                surnames = line.split('\t')[1]
                surnames_list.append(surnames)
        return surnames_list


result_2 = return_surnames('names.txt')


# 3

def return_calendar_dates_and_events(filename: str) -> list:
    with open(filename, 'r') as my_file:
        data = my_file.read()
        calendar_dates_and_events_list = []
        for line in (data.split('\n')):
            if '-' in line:
                calendar_date = line.split('-')[0]
                event = line.split('-', 1)[1]
                calendar_dates_and_events_list.append({calendar_date: event})
        return calendar_dates_and_events_list


result_3 = return_calendar_dates_and_events('authors.txt')
