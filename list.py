# empty_list=[]
# numbers=[1,32,4,3,2,5,6]
# mixed_list=[1,3,2,"aakriti",[4,6,]]
# print(empty_list)
# print(numbers)
# print(mixed_list)
# print(mixed_list[3])
#slicing
# 

# mutability
# num=[2,3,4,5,6,7,8]
# num.append(9)
# print(num)
# num.pop()
# print(num)
# num.remove(5)
# print(num)
# num.extend([35,200,44,15,78,98,76])#or list1+list2
# print(num)
# num.insert(3,10000)
# print(num)
# num.pop(3)
# print(num)
# #acending order
# num.sort()
# print(num)
# #decending order
# num.sort(reverse=True)
# print(num)


num=[0,1,3,2,2,11]
# for index,number in enumerate(num):
#     print(f"Index:{index},value:{number}")
# #shallow copy
# shallow_copy=num[:]
# print(shallow_copy)
# shallow_copy2=list(num)
# print(shallow_copy2)
# shallow_copy3=num.copy()
# print(shallow_copy3)

# #deep copy
# import copy
# numm=[[1,2],[2,5],[5,3,7]]
# deep_copy=copy.deepcopy(numm)
# print(deep_copy)


# #list comprehensions
# num=[1,3,4,6,7,5,3,5,3,56,4,2]
# square=[num2**2 for num2 in num]
# print(square)

# #nested list comprenhensions
# matrix=[
#     [1,2,3],[34,5,3],[3,6,21,7]
# ]
# flattened=[num for row in matrix for num in row]
# print(flattened)

# a=['apple','ball','cat','dog']
# b=[i.upper() for i in a]
# print(b)

#sorting by length of string
a=['prabesh','pradip','ram','aakriti','lamsal']
print(a.sort())

