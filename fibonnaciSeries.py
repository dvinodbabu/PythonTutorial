# Fibonacci Series using the while loop
# The sum of two elements defines the next
a, b = 0, 1  # Multiple assigments in Python
print(a, b)
# The keyword argument end can be used to avoid the newline after the output
while a < 100:
    print(a, end=',')
    a, b = b, a + b
