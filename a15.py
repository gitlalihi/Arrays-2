#Write a Python program to check whether it follows the sequence given in the patterns array.
def follows_pattern(sequence, patterns):
    return len(sequence) == len(patterns) and len(set(patterns)) == len(set(sequence))

# Example usage:
sequence_to_check = [1, 2, 3, 4, 5]
pattern_array = ['A', 'B', 'C', 'D', 'E']

if follows_pattern(sequence_to_check, pattern_array):
    print("The sequence follows the specified pattern.")
else:
    print("The sequence does not follow the specified pattern.")
