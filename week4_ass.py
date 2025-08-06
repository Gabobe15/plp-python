# try:
#     with open('./data/examples.txt', 'r') as file:
#         content = file.read()
#         print(content)
# except  Exception as e:
#     print('Error type:', type(e).__name__)
#     # print('File does not exist') 
# finally:
#     print('Finished attempting to read the file.')
    
try:
    with open('./data/parent_consent_form.docx', 'r') as file:
        content = file.read()
        print(content)
except  Exception as e:
    print('Error type:', type(e).__name__)
    # print('File does not exist') 
finally:
    print('Finished attempting to read the file.')

    
# try:
#     with open('./data/output.txt', 'w') as file:
#         content = file.write('Hello, world!')
#         print(content)
# except:
#     print('something went wrong') 
