#Write a Python program that removes all duplicate elements from an array and returns a new array.
def remove_duplicates(input_array):
    unique_set = set()
    result_array = []
    for element in input_array:
        if element not in unique_set:
            result_array.append(element)
            unique_set.add(element)
    return result_array

input_array = [1, 2, 3, 4, 2, 5, 6, 3, 7, 8, 8]
result = remove_duplicates(input_array)
print("Original Array:", input_array)
print("Array with Duplicates Removed:", result)
