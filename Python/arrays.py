print("Arrays in Python!!")
print("Python has a module 'array' which mimics the behaviour of array as programmers must have seen in other languages. List is the native array type in Python but list accepts elements of any datatype but arrays do not. Lets play around with some array methods.\n")

print("1. 'import array' module\n")
import array

print("2. To declare and initialize an array, do: 'arr = array.array('<datatype>', '[array_ele]'\n")
arr = array.array('i', [1,2,3,4])
print (arr)
print()

print("3. To append elements to the end of the array 'arr.append(<value>)'\n")

arr.append(5)
#arr.append(4, 5)
print(arr, "\n")

print("4. To insert an element at a particular position: arr.insert(<idx>,<ele>)\n")
arr.insert(2, 2)
print(arr)
print()

print("5. To remove an element from a particular index: arr.pop(idx)")
arr.pop(2)
print(arr)
print()

print("6. To remove the first occurance of an element: arr.remove(ele)")
print()
arr.remove(4)
print(arr)
print()

print("7. To reverse the array: arr.reverse()")
arr.reverse()
print(arr)
