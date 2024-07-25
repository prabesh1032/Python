# name=str(input("enter your name:"))
# def ivowel(name):
#     v=0
#     for word in name:
#         if word == 'a' or word == 'e' or word == 'i' or word == 'o' or word == 'u':
#             v=v+1 
#     return v
# result=ivowel(name)        
# print("the number of  vowel in given name is",result)

#create a simple contact book application using python dictyionaries.
#the application should allow users to add, update,delete,and search for contacts.

def add_contact():
    name=str(input("enter name"))
    age=int(input("enter age"))
    
    