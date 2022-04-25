DEBUG_MODE = True


def read_txt_file_as_str(filename: str) -> str:
    with open(filename, 'r', encoding='utf-8') as my_file:
        data = my_file.read()
    return data

if __name__ == "__main__":
    print('>>>>>>>>>>>', __name__)
    data = read_txt_file_as_str("test.txt")
    print('>>>>>>>>>>>', data)


