import numpy as np
'''a=np.array([1,2,3,4,5,6,3,5,3])
print(a)
#using buildin function
print(np.zeros((2,3)))
#identity matrix
print(np.eye(3))
#filled with specific value
print(np.full((1,3),5))
#empty
print(np.empty((1,3)))
#using range and linespace
print(np.arange(0,10,2))
print(np.linspace(0,1,5))'''


'''#Random 
#random value between 0 and 1
print(np.random.random((2,3)))
#array with random integer
print(np.random.randint(1,10,(2,3)))'''
'''#creating array from string
num_string="1,2,3,4,5,7,8,6,4,2"
num_array=np.array(num_string.split(','),dtype=int)
print("numeric array",num_array)'''

#dimension
'''#1
print(np.array([1,2,3,4]))
#2
print(np.array([[1,2,3],[2,5,8]]))'''
'''#3
print(np.array([[[1,2,3],[2,3,4]],[[6,7,8],[4,6,8]]]))
array=np.array([[[1,2,3],[2,3,4]],[[6,7,8],[4,6,8]]])
print("array:\n",array)
print("Shape:\n",array.shape)
print("number of dimension:\n",array.ndim)
print("size:\n",array.size)
print("datatype:\n",array.dtype)
print("item size:\n",array.itemsize)
twod=np.array([[1,2,3],[2,5,8]])
transpose=twod.T
print(transpose)
'''
'''
array=np.array([1,2,3,4,5])
array1=np.array([1.2,2.4,3.6,4.9,5.9])
print(array.dtype)
print(array1.dtype)
'''
'''

#indexing 
#1D
array1=np.array([1,2,3,4,5])
print("1d array",array1)
print("first element",array1[0])
print("last emement",array1[-1])
#2d
array2=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print("2d array",array2)
print("element at (0,1)",array2[0,1])
print(" emement at (1,3)",array2[1,3])
#3d
array3=np.array([
    [[1,2,3,4,5],[6,7,8,9,10]],
    [[11,12,13,14,15],[16,17,18,19,20]]
    ])
print("3d array",array3)
print("element at (0,1,2)",array3[0,1,2])
print(" emement at (1,0,1)",array3[1,0,1])

#slicing
#1d
print("first three element",array1[:3])
print("element from index 2 to end",array1[2:])
print("every 2nd element",array1[::2])
#2d
print("first row",array2[0,:])
print("first column",array2[:,0])
print("subarray",array2[0:2,1:3])
#3d
print("first block",array3[0,:,:])
print("second row in each block",array3[:,1,:])
print("third column in each row\n",array3[:,:,2])
'''
'''
#original
original = np.array([1,2,3,4,5])
copy= original.copy()
copy[0]=10
print("original::",original)
print("copy::",copy)

#view
original = np.array([1,2,3,4,5])
view_copy= original.view()
view_copy[0]=10
print("original::",original)
print("viewcopy::",view_copy)

#logspace
array_logspace=np.logspace(1,6,12)
print("array using logspace::",array_logspace)


#array brodcasting
array_2d=np.array([[1,2,3],[4,5,6]])
array_1d=np.array([1,32,4])
print("after broadcasting and adding:",array_1d+array_2d)


#iteration in 2D
array_2d=np.array([[2,3,4,5,6],[3,6,8,6,2]])
for row in array_2d:
    for i in row:
        print(i)

        
#using nditer foe multi dimension
ayyay_3d=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])        
for i in np.nditer(ayyay_3d):
    print(i)
    

#modifying array during interation
array_2d=np.array([[2,3,4,5,6],[3,6,8,6,2]])
for element in np.nditer(array_2d,op_flags=["readwrite"]):
    element[...]=element*3
    print("modified array is::",array_2d)
    '''



#sorting
'''
array=np.array([2,44,6,34,5,89,0,54,678])
array.sort() #or np.sort()
print("element after sort:",array)
#in 2d
array_2d=np.array([[2,3,43,5,6],[3,6,8,6,2]])
sorted_element_row=np.sort(array_2d,axis=1)
print("origin :",array_2d)
print("after sorted:",sorted_element_row)
'''
#argsort
'''array=np.array([2,44,6,34,5,89,0,54,678])
sorted_index=np.argsort(array)
sorted_array_by_indics=array[sorted_index]
print("original array",array)
print("indices that would sort array",sorted_index)
print("array sorted by indices",sorted_array_by_indics)'''

#lexsort
'''names=np.array(["ram","hari","arjun","pradip","laxmi"])
ages=np.array([39,30,22,34,20])
sorted_index=np.lexsort((names,ages))
sorted_names=names[sorted_index]
sorted_ages=ages[sorted_index]
print("Names:",names)
print("ages:",ages)
print("sorted index:",sorted_index)
print("sorted names",sorted_names)
print("sorted ages:",sorted_ages)'''


#searching
'''array=np.array([2,44,6,34,5,89,0,54,678])
indices=np.where(array>10)
print("array",array)
print("Indices of elements greater than 10 is:",indices)
print("array greater than 10 are:",array[indices])'''


#searchsorted
'''sorted_array=([3,98,234,678,1234,5678,98765])
indices=np.searchsorted(sorted_array,[5,676,3456])
print("sorted array:",sorted_array)
print("sorted :",indices)'''

#numpy.any and numpy.all
#---------

#Statistic 
'''array=np.array([2,44,6,34,5,89,0,54,678])
print("mean:",np.mean(array))
print("median:",np.median(array))
print("standatd deviatioin:",np.std(array))
print("variance",np.var(array))
print("persintile:",np.percentile(array,25))#Q25'''



#histogram
'''data=np.random.randn(1000)
hist,bin_edges=np.histogram(data,bins=10)
print("histogram:",hist)
print("bin_edges:",bin_edges)'''

##correlation coefficient
x=np.array([1,2,3,4,5,56])
y=np.array([3,4,6,7,4,22])
print("correlation coffecient is:",np.corrcoef(x,y))
