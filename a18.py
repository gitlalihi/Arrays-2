#Write a Python program to get array buffer information.
from array import array

a = array("i", [12, 25])
print("Array buffer start address in memory and number of elements.")
print(a.buffer_info())

