# List written as a list of comma-separated values (items) between square brackets.
# Lists might contain items of different types, but usually the items all have the same type.
squares = [1, 4, 9, 16, 25, 36]
print(squares)
# Lists can be indexed and sliced:
print(squares[0])  # indexing returns the item
print(squares[-1])  # indexing returns the item
# All slice operations return a new list containing the requested elements. This means that the following slice returns a shallow copy of the list:
print(squares[:])
# Lists also support operations like concatenation
print(squares + [49])
# Unlike strings, which are immutable, lists are a mutable type, i.e. it is possible to change their content
cubes = [1, 8, 27, 65, 125]  # something's wrong here, the cube of 4 is 64 not 65
print(cubes)
print(4 ** 3)
cubes[3] = 4 ** 3
print(cubes)
# add new items at the end of the list, by using the append()
cubes.append(216)
print(cubes)
# Assignment to slices is also possible, and this can even change the size of the list or clear it entirely:
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
# replace some values
letters[2:5]= ['C','D','E']
print(letters)
# now remove them
letters[2:5]= []
print(letters)
# clear the list by replacing all the elements with an empty list
letters[:] = []
print(letters)
#It is possible to nest lists (create lists containing other lists)
a = ['a', 'b', 'c']
n = [1, 2, 3]
x=[a,n]
print(x)
print(x[0])
#First element in the first list
print(x[0][1])