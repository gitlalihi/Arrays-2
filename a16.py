#Write a Python program to find a pair with the highest product from a given array of integers.
def max_product_pair(arr):
    n = len(arr)
    if n < 2:
        print("Array should have at least two elements.")
    arr.sort()
    return arr[-1], arr[-2]


arr = [1, 3, 5, 2, 9, -6, -4]
result = max_product_pair(arr)
print("Pair with the highest product:", result)
print("Product:", result[0] * result[1])
