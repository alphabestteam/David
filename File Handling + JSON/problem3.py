def read_file(file_name: str) -> str:
    file = open(file_name, "r")
    file_info = file.read()
    file.close()
    return file_info


def write_to_file_new_line(file_name: str) -> None:
    user_input = input(f"Enter what you want to write to file - {file_name}: ")
    file = open(file_name, 'w')
    file.writelines(user_input)
    file.close()


if __name__ == '__main__':
    print(read_file("readAndWriteFile.txt"))
    write_to_file_new_line("readAndWriteFile.txt")

