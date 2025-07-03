from pathlib import Path
import os

def readfileandfolder():
    path = Path('D:\Github\Learn-Python\Projects\File Handling')
    items = list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f"{i+1}:{items}")

def createFile():
    readfileandfolder()
    name = input('Enter your file name: ')
    p = Path(f'D:\Github\Learn-Python\Projects\File Handling\{name}')
    if not p.exists():
        with open(p,'w') as fs:
            data = input('Write Something...')
            fs.write(data)
        print('File Create Successfully')
    else:
        print('This File Already Exists')

def readFile():
    try:    
        readfileandfolder()
        name = input('Enter the File Name: ')
        p = Path(f'D:\Github\Learn-Python\Projects\File Handling\{name}')
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data = fs.read()
                print(data)
            print('Data Read Successful')
        else:
            print('This File Does not Exist')
    except Exception as e:
        print(f'An Error occurred as {e}')
        
def updateFile():
    try:
        readfileandfolder()
        name = input('Enter the File Name: ')
        p = Path(f'D:\Github\Learn-Python\Projects\File Handling\{name}')
        if p.exists() and p.is_file():
            print('Press 1 for changing file name')
            print('Press 2 for overwriting data in a file')
            print('Press 3 for appending data in a file')
        
            res = int(input('Tell Your Response: '))
        
            if res==1:
                name2 = input('Enter new File name: ')
                p2 = Path(f'D:\Github\Learn-Python\Projects\File Handling\{name}')
                p.rename(p2)
            if res==2:
                with open(p, 'w') as fs:
                    data = input('Enter the data to overwrite: ')
                    fs.write(data)
            if res==3:
                with open(p, 'a') as fs:
                    data = input('Enter the data to append: ')
                    fs.write(" " + data)
    except Exception as e:
        print(f'An Error occurred as {e}')

def deleteFile():
    try:
        readfileandfolder()
        name = input('Enter the File Name: ')
        p = Path(f'D:\Github\Learn-Python\Projects\File Handling\{name}')
        
        if p.exists() and p.is_file():
            os.remove(p)
            print('File Deleted Successfully...')
        else:
            print('No Such File Exists...')
    except Exception as e:
        print(f'An Error occurred as {e}')

print('press 1 for creating a file')
print('press 2 for reading a file')
print('press 3 for updating a file')
print('press 4 for deleting a file')

check = int(input('Enter your response: '))

if check == 1:
    createFile()
if check==2:
    readFile()
if check==3:
    updateFile()
if check==4:
    deleteFile()