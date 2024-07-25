# for i in range(20,0,-2):
#     print(i*i)
empyt_dict={}
person={
    "name":"prabesh",
    "age":21,
    "adderss":"gaindakot"
    }
print(person)
'''

#acessing dictionary elements using indexing
print(person["name"])
print(person["age"])
#acessing using get
print(person.get("name"))
print(person.get("salary","not available"))
person["salary"]=2000
person["age"]=20
person["gemail"]="prabeshach@gmail.com"
print(person)
del person["salary"]
print(person)
#person.clear()
#keys(),values(),items()
person(person.keys())
person(person.values())
person(person.items())

#update
person.update({"email":"prsghjs@gmail.com"})
print(person)

#copy
person_copy=person.copy()
print(person_copy) '''

#looping through key value pairs
for key,value in person.items():
    print(f"{key}:{value}")
    

