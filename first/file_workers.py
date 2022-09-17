def read_from_file(name):
    with open(name, "r") as file:
        return file.readlines()

print(read_from_file("prodfile.txt"))