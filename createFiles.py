
import os

def create_files(num_of_copy,name):
    os.chdir('/Users/SamShamsan/Documents/Music')
    print(os.getcwd())
    counter=0
    for i in range(1,num_of_copy):
        with open('{}-{}.mp3'.format(name,counter),'w'):
            counter+=1
    for items in os.listdir():
        fiel_name, fiel_ex = os.path.splitext(items)
        print(fiel_name)
create_files(4,'#1- Scream Album - Truck ')
