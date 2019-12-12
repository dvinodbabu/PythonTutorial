words=['cat', 'dog', 'tiger', 'lion']
for w in words:
    print(w, len(w))# iterates the list and prints the list of the elements in the list

for i in range(100): # If you do need to iterate over a sequence of numbers, the built-in function range() comes in handy
    print(i)

a = ['mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print (i,a[i])

print(range(10))
print(sum(range(10)))