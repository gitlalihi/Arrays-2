#Write a Python program to find the missing number in a given array of numbers between 10 and 20.
def find_missing_number(input_array):
    all_numbers_set = set(range(10,21))
    input_set = set(input_array)
    missing_number = list(all_numbers_set - input_set)[0]
    return missing_number


input_array = [10, 11, 12, 14, 15, 16, 17, 18, 19, 20]
missing_number = find_missing_number(input_array)
print("Original Array:", input_array)
print("Missing Number:", missing_number)
