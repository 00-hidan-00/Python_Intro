def read_txt_file(filename):
    with open(filename, 'r') as my_file:
        data = my_file.read()
    return data

def write_txt_file(filename, data):
    with open(filename, 'w') as txt_file:
        txt_file.writelines(data)

filename = 'test.txt'

data = read_txt_file(filename)

numbers = []
for line in data.split('\n'):
    if line:
        number = line.split()[1]
        numbers.append(number)

print(numbers)










# data +='#TEST'
#
# output_filename = 'test_2.py'
# write_txt_file(output_filename, data)