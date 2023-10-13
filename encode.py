def encode(message):
    first_letter = message[0]
    previous_char = first_letter
    counter = 1
    encoded_message = ""
    for i in range(1,(len(message) - 1)):
        current_char = message[i]
        if current_char == previous_char:
            counter += 1
            previous_char = current_char
        else:
            encoded_message += f"*{previous_char}{counter}*"
            counter = 1
            previous_char = current_char
    return encoded_message

