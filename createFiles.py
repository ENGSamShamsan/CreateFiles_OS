
import os

def create_files(num_of_copy,name):
#     First set up you current directory
    os.chdir('/Users/SamShamsan/Documents/Music')
    # You can print the current directory here to verify you have the correct one
    print(os.getcwd())
    # Set up a counter to add thier values to the tail of the file name as an index    
    counter=0
    # create x amount of files
    for i in range(1,num_of_copy):
        # with the context manager the file will be closed automatically
        # Also set up the schema to the write mode as we creating the files
        with open('{}-{}.mp3'.format(name,counter),'w'):
            counter+=1
   # iterate through the current working dirctory and print out all files names 
    for items in os.listdir():
        # This splitext function in path help us seprate the name from the extention
        fiel_name, fiel_ex = os.path.splitext(items)
        print(fiel_name)
create_files(4,'#1- Scream Album - Truck ')



