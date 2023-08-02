def count_upper_lower_chars(input_string):
    upper_count = sum(1 for char in input_string if char.isupper())
    lower_count = sum(1 for char in input_string if char.islower())
    return upper_count, lower_count

# Sample String
sample_string = 'The quick Brow Fox'

# Counting the number of uppercase and lowercase characters
upper_chars, lower_chars = count_upper_lower_chars(sample_string)

# Printing the output
print("No. of Upper case characters:", upper_chars)
print("No. of Lower case characters:", lower_chars)
