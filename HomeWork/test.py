def returns___list(filename):
    with open(filename, 'r') as my_file:
        data = my_file.read()
        l_list = []
        for line in (data.split('\n')):
            if '-' in line:
                event = line.split('-')[0]
                calendar_date = line.split('-', 1)[1]
                l_list.append({event: calendar_date})
        return l_list


result_3 = returns___list('authors.txt')
