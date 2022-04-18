# 1

def returns_domains_list(filename):
    with open(filename, 'r') as my_file:
        data = my_file.read()
        domains_list = []
        for line in data.split('\n'):
            if line:
                domains_list.append(line[1:])
        return domains_list


result_1 = returns_domains_list('domains.txt')
# 2

def returns_surnames_list(filename):
    with open(filename, 'r') as my_file:
        data = my_file.read()
        surnames_list = []
        for line in data.split('\n'):
            if line:
                surnames = line.split('\t')[1]
                surnames_list.append(surnames)
        return surnames_list


result_2 = returns_surnames_list('names.txt')
# 3

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

