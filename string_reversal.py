*Level:1 Task-1 String Reversal

Create a Python function that takes a string as input and returns the reverse of that string. For example, if the input is "hello, " the function should return "olleh."*

def reverse_string(input_string):
    return input_string[::-1]

input_string = "Python Developer"
reversed_string = reverse_string(input_string)
print(reversed_string)
