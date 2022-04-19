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

print(result_3)
