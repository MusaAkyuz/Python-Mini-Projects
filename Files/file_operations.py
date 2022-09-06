def create_file_w_mode(text):
    # if file.txt file exist, does not matter
    # w modes write on file
    # every time creates new file.txt
    file_desc = open("file.txt", "w")

    # writes something in file
    file_desc.write(text)

    file_desc.close()


def create_file_r_mode():
    # r mode read only
    file_desc2 = open("file.txt", "r")

    # prints line by line
    # every read command includes last \n character
    print(file_desc2.readline())
    print(file_desc2.readline())

    file_desc2.close()

    print("------")

    # use rstrip() function to delete last char \n
    file_desc2 = open("file.txt", "r")
    print(file_desc2.readline().rstrip("\n"))
    print(file_desc2.readline().rstrip("\n"))

    file_desc2.close()

    print("------")

    # prints all file
    file_desc2 = open("file.txt", "r")
    print(file_desc2.read().rstrip("\n"))


def create_file_a_mode(text):
    # a mode for append
    # if file already exist, write operation appends the file
    file_desc2 = open("file.txt", "a")

    file_desc2.write(text)

    file_desc2.close()


def read_file_with_loop():
    file_desc4 = open("file.txt", "r")

    line = file_desc4.readline().rstrip("\n")
    while line != "":
        print(line)
        line = file_desc4.readline().rstrip("\n")


def read_file_with_loop_easy_way():
    file_desc5 = open("file.txt", "r")

    for line in file_desc5:
        print(line.rstrip("\n"))
