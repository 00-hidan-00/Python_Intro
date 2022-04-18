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

print(result_2)