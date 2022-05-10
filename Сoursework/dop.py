# data = read_json_file("config.json")
# data["actual_course_key"] = actual_course
# write_json_file("config.json", data)


# def actual_exchange_rate(course, delta):
#     new_course = round(random.uniform(course - delta, course + delta), 2)
#     return new_course
# actual_course = actual_exchange_rate(read_json_file_list['initial_course'], read_json_file_list["delta"])

# def add_course_to_data(actual_course):
#
#     for row in read_csv_file_list:
#         row["Course"] = + actual_course
#     write_csv_file_as_dict('data.csv', read_csv_file_list)


# def write_json_file(filename: str, data: Union[List, Dict]) -> None:
#     with open(filename, 'w') as file:
#         # file.seek(0, 2)
#         json.dump(data, file, indent=2)


# def write_json_file(filename: str, data: Union[List, Dict]) -> None:
#     with open(filename, 'w') as file:
#         json.dump(data, file, indent=2)
