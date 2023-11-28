#Python program that reads a string and interprets it as an array of machine values.
import array
def interpret_string_as_array(input_string, data_type='f'):
    return array.array(data_type, bytes.fromhex(input_string))
input_string = "3f80000040490fdb"  
result = interpret_string_as_array(input_string, data_type='f')
print(result)
