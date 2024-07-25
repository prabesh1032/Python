'''''
#read
file=open('text.txt','r')
content=file.read()
print(content)
file.close()
'''''
'''''
file=open('text.txt','r')
content=file.readline()
print(content)
file.close()
'''''
'''''
file=open('text.txt','r')
lines=file.readlines()
for line in lines:
    print(line.strip())
file.close()
'''''
'''''
#write
file=open('newfile.txt','w')
file.write("hello dear friend.\n")
file.write(" how are you.\n")
file=open('text.txt','w')
file.write("hello dear friend.\n")
file.write(" how are you.\n")
'''''
'''''
#r+ read and write
file=open('text.txt','r+')
content=file.read()
print("current content::")
print(content)
line=input("enter the content you want to write::\n")
file.write(line)
file.seek(0)
content=file.read()
print("\nUpdated content:")
print(content)
file.close()
'''''
'''''
#reading and writing file with with statement
with open('text.txt','r') as file:
    print(file.read())

with open('text.txt','r') as file:
    print(file.readline())

with open('text.txt','r') as file:
    print(file.readlines())
'''''
'''''
with open('text2.txt','w') as file:
    line1=input("enter the content you want to write::\n")
    file.write(line1)
    line2=input("enter the content you want to write::\n")
    file.write(line2)

with open('text2.txt','r+') as file:
    content=file.read()
    file.write('\nAppending new content.\n')
    file.seek(0)
    content=file.read()
    print(content)
'''''
'''''
with open('text2.txt','w') as file:
    file.write('initial content.\n')

with open('text2.txt','a')as file:
    file.write("apending content.\n")

with open('text2.txt','r')as file:
    print(file.read())
'''''
#readbinary
'''
with open('1.png','rb')as file:
    data=file.read()
    print(data) '''
'''
#writebinary
data=b'\x48\x65\x6c\x6c\x6f' #hello
with open('output.bin','wb')as file:
    file.write(data)
datatoappend=b'\x44\x54\x7d\x33\x45' 
with open("output.bin",'ab')as file:
    file.write(datatoappend)
    '''
#binary file seek
with open('output.bin','rb')as file:
    file.seek(4,0)
    data= file.read(3)
    print(f"bytes from current postion:{data}")
    file.seek(2,1)
    data=file.read(4)
    print(f"bytes from current postion:{data}")
    file.seek(-3,2)
    data=file.read(3)
    print(f"bytes from current postion:{data}")



