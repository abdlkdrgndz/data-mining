import numpy

arr = numpy.array([ [1,3,5], [4,6,7] ])
arr2 = numpy.array([ [2,4,11] , [8,0,3] ] )

#vertical birleştirme  - dikey
print("Dikey Stacking: " , numpy.vstack((arr,arr2)))
print("Yatay Stacking: " , numpy.hstack((arr,arr2)))