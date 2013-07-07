def get_message(file_input):
    message = ""
    for line in file_input:
        for c in line:
            if c.isalpha():
                message += c
    return message

if __name__ == "__main__":
    file_input = open("input.txt")
    print get_message(file_input)