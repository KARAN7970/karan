def create_ascii_dict():
    ascii_dict = {}
    for i in range(97, 123):  # ASCII codes for lowercase letters 'a' to 'z'
        ascii_dict[chr(i)] = i
    return ascii_dict

# Creating the ASCII dictionary
ascii_dict = create_ascii_dict()

# Printing the output
print(ascii_dict)
