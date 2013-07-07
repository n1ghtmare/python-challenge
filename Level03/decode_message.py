def decode(encoded_message):
    decoded_message = ""
    for i, c in enumerate(encoded_message):
        if c.islower() and i < len(encoded_message) - 4:
            if encoded_message[i+1:i+4].isupper() and encoded_message[i+4].islower() and encoded_message[i-3:i].isupper() and encoded_message[i-4].islower():
                decoded_message += c
    return decoded_message

def get_string(file_name):
    with open(file_name, mode="r") as input_file:
        return input_file.read().replace('\n', '')

if __name__ == "__main__":
    content = get_string("input.txt")
    print decode(content)