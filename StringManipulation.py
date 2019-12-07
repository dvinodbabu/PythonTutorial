print("Hello World")
word = "Python"
print(word)
# prints first 2 chars
print(word[0:2])
# prints the first char
print(word[0])
# cool feeature = Negative indices are allowed in python
# prints from the last
print(word[-1])
# prints first two chars
print(word[:2])
# prints the chars after first 2 position
print(word[2:])
# Concatenation
print(word[:2] + word[2:])

# This is how the String is mapped in the memory
# +---+---+---+---+---+---+
# | P | y | t | h | o | n |
# +---+---+---+---+---+---+
# 0   1   2   3   4   5   6
# -6  -5  -4  -3  -2  -1
# Python strings cannot be changed — they are immutable. You can't do this word[0]=J
print('J' + word[1:])
