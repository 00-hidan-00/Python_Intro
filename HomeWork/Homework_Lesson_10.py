from datetime import datetime


def read_file(filename):
    with open(filename, 'r') as my_file:
        data = my_file.read().splitlines()
    return data


# 1

def returns_domains(filename='domains.txt') -> list:
    domains = []
    for line in read_file(filename):
        if line:
            domains.append(line[1:])
    return domains


result_1 = returns_domains()


# 2

def return_surnames(filename='names.txt') -> list:
    surnames = []
    for line in read_file(filename):
        if line:
            surname = line.split('\t')[1]
            surnames.append(surname)
    return surnames


result_2 = return_surnames()


# 3

def return_calendar_dates(filename: str) -> list:
    calendar_dates = []
    for line in (read_file(filename)):
        if ' - ' in line and line[:1].isdigit():
            calendar_date = line.split(' - ')[0]
            calendar_dates.append({"date": calendar_date})
    return calendar_dates


result_3 = return_calendar_dates('authors.txt')


# 4

def transform_date(author_date: str):
    # months_dict = {"January": "01",
    #                "February": "02",
    #                "March": "03",
    #                "April": "04",
    #                "May": "05",
    #                "June": "06",
    #                "July": "07",
    #                "August": "08",
    #                "September": "09",
    #                "October": "10",
    #                "November": "11",
    #                "December": "12"}
    # day, month, year = author_date.split()
    # day = day[:-2].zfill(2)
    # month = months_dict[month]
    # return f"{day}/{month}/{year}"

    day, month, year = author_date.split()
    day = day[:-2]
    date = f"{day} {month} {year}"
    new_date = datetime.strptime(date, "%d %B %Y").strftime("%d/%m/%Y")
    return new_date


def get_modified_dates(filename: str):
    dates = return_calendar_dates(filename)
    new_dates = []
    for author_date in dates:
        date = author_date['date']
        new_dates.append({'date_original': date, 'date_modified': transform_date(date)})
    return new_dates


result_4 = get_modified_dates('authors.txt')

print(result_1)
print(result_2)
print(result_3)
print(result_4)
