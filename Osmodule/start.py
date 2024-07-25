import os
#create directory
#os.mkdir('new_directory')
'''
#nested directories
#os.makedirs('parent_directory/child_directory')
#remove
#os.rmdir('new_directory')
#os.removedirs('parent_directory/child_directory')
''''''
#list contents of directory
contents=os.listdir("new_directory")
print(contents)
#check if a file or directory exist
exist=os.path.exists("new_directory")
print(exist)
'''
#get current working directory
'''
current_directory=os.getcwd()
print(current_directory)
'''
#create an empty file
'''with open('newfile.txt','w') as f:
    f.write('hii how are')'''
#delete an empty file
'''os.remove('newfile.txt')'''
#rename a file
'''os.rename('newfile.txt','oldfile.txt')'''
#get file information
#os.remove('newfile.txt')
file_info=os.stat('oldfile.txt')
print(file_info)


#print current working directory
print("current working Directory:",os.getcwd())
#define the source and destination paths
source_path='oldfile.txt'
destination_path='hii.txt'
try:
    os.rename(source_path,destination_path)
    print("file rename sucessfully")
except FileNotFoundError:
    print(f"Error:the file {source_path} doesnot exist")
except PermissionError:
    print(f"error: PermissionError unable to rename{source_path}")    
finally:
    print('moboie harayoo')