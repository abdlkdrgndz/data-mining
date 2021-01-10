import numpy

# array convert and copy

myList = [1,4,5,7,8,9] # Liste oluşturduk
array = numpy.array(myList) # işte bu kadar listeden array e geçtik. çevirme tamam.

print("myArray: " , array)

print("---------------")

## array den listeye geçiş
newList = list(array)
print("newList: ", newList)