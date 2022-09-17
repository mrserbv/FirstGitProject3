from first.file_workers import read_from_file


def create_text_data(test_data):
    with open("testfile.txt", "a") as file:
        file.writelines(test_data)


# Вариант 1
def test_read_from_file2():
    test_data = ['one\n', 'two\n', 'three\n']
    create_text_data(test_data)
    assert test_data == read_from_file("testfile.txt")


# Вариант 2
def test_read_from_file():
    test_data = ['one\n', 'two\n', 'three\n', 'four\n']
    create_text_data(test_data)
    assert test_data == read_from_file("testfile.txt")
