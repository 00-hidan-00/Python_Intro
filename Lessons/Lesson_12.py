# json
# csv
# assert, raise

import json
from typing import Optional, List, Dict, Union
import csv

##################### strings


test_dict = '{"to_test_dir": 123}'
data = json.loads(test_dict)
data = {'to_test_dir': 123}
data['to_test_dir'] = 321
test_dict_2 = json.dumps(data)


############################################################

def read_txt_file(filename: str) -> list:
    with open(filename, 'r') as file:
        data = file.read()  # .splitlines()
    return data


def read_json_file(filename: str) -> Union[List, Dict]:  # Optional[List]
    with open(filename, 'r') as file:
        data = json.load(file)
    return data


def write_json_file(filename: str, data: Union[List, Dict]) -> None:
    with open(filename, 'w') as file:
        json.dump(data, file, indent=2)


filename = "Lesson_12.json"
filename_out = "Lesson_12_out.json"
# data = read_txt_file(filename)
data = read_json_file(filename)
data["name"] = "123"
write_json_file(filename_out, data)
print(data, type(data))


###########################################

# csv

def read_csv_file(filename: str) -> list:
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            data.append(row)
    return data


def write_csv_file(filename, data):
    with open(filename, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(data)


filename = "test.csv"
data = read_csv_file(filename)
header = data.pop(0)
# header.append('Total')
for row in data:
    row.append(int(row[1]) + int(row[2]))

data = [header] + data
# write_csv_file("test.csv", data)


###########################################


def read_csv_file_as_dict(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data


def write_csv_file_as_dict(filename, data):
    fieldnames = ["Sum", "Price", "Month", "Total"]
    # fieldnames = data[0].keys()
    with open(filename, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


filename = "test.csv"
data = read_csv_file_as_dict(filename)
for row in data:
    row["Total"] = int(row["Price"]) + int(row["Sum"])
print(data)
# write_csv_file_as_dict("test.csv", data)


############################################################

# assert, raise

def some_func(val_1, val_2):
    if val_1 < 0 or val_2 < 0:
        raise Exception('???????????? ????????????')
    return val_1 + val_2


result = some_func(-1000, 200)

assert result > 0, '???????????? ????????????'
print("OK")
