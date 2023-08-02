def sort_by_last_element(tuples_list):
    return sorted(tuples_list, key=lambda x: x[-1])

# Sample List
sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# Sorting the list based on the last element of each tuple
result = sort_by_last_element(sample_list)

# Printing the result
print(result)
