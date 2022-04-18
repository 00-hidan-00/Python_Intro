def return_calendar_dates_and_events(filename: str) -> list:
    with open(filename, 'r') as my_file:
        data = my_file.read()
        calendar_dates_and_events = []
        for line in (data.split('\n')):
            if '-' in line:
                calendar_date = line.split('-')[0]
                event = line.split('-', 1)[1]
                calendar_dates_and_events.append({calendar_date: event})
        return calendar_dates_and_events


result_3 = return_calendar_dates_and_events('authors.txt')

print(result_3)