try:
    with open('./data/example.txt', 'r') as file:
        content = file.read()
        print(content)
except  FileExistsError:
    print('File does not exist') 
finally:
    print('Finished attempting to read the file.')

    
try:
    with open('./data/output.txt', 'w') as file:
        content = file.write('Hello, world!')
        print(content)
except:
    print('something went wrong') 
