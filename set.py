# set={2,43,3,2,1,3,5,7}
# print(set)
#empty set
# empty_set=set()
# print(empty_set)
# s={12,2,34,2,21,3,3423,3}
# s.add(4)
# print(s)
# s.remove(12)
# s.discard(3427)
# print(s)
# s.pop()
# print(s)
# s.clear()
# print(s)

# acessing element
# myset={1,23,43,2}
# print(1 in myset)
# print(56 in myset)

# #converting a set to a list
# mylist=list(myset)
# mytuple=tuple(myset)
# print(mylist)
# print(mytuple)

# a={1,2,3,4,5}
# b={4,5,6,7}
# union=a.union(b)
# union=a|b
# intersection=a.intersection(b)
# intersection=a&b
# difference=a-b
# difference=a.difference(b)
# sym_dif=a.symmetric_difference(b)
# sym_dif=a^b
# print(union)
# print(intersection)
# print(difference)
# print(sym_dif)

#set compension
#a={1,2,3,4,3,2,3,5,7,8,97,5,43,2}
# s=set(a)
# print(s)

#frozen set
#a={2,3,4,5,6,7,8}
# frozen_set=frozenset(a)
# #frozen_set=({2,3,4,5,6,7,8})
# print(frozen_set)
# frozen_set.add(20)
# frozen_set.remove(3)
# fs1=frozenset([1,2,3,4,5])
# fs2=frozenset([4,5,6,7])
# union=fs1.union(fs2)
# ints=fs1.intersection(fs2) 
# diff=fs1.difference(fs2)
# sym_d=fs1.symmetric_difference(fs2)
# subset=fs1.issubset(fs2)
# ssubset=fs2.issuperset(fs2)
# print(union,ints,diff,sym_d,subset,ssubset)

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# print("prime number from 1 to 100 are::")
# for num in range(1, 101) :
#     if is_prime(num):
#         print(num)


for i in range(20,0,-2):
    print(i*i)
    