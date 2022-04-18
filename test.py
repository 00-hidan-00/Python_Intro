def returns_domains_list(filename):
    with open(filename, 'r') as my_file:
        data = my_file.read()
        domains_list = []
        for line in data.split('\n'):
            if line:
                domains_list.append(line[1:])
        return domains_list


print(returns_domains_list('domains.txt'))