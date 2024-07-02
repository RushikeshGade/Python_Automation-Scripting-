from sys import *
import os
import hashlib

def hashfile(path, blocksize = 1024):
    fd =open(pah,'rb')
    hasher = hashlib.md5()
    buf = fd.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)
        buf = fd.read(blocksize)

    fd.close()

    return hasher.hextdigest()

def FindDuplicate():
    flag = os.path.isabs(path) 

    if flag  == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)  

    dups = {}
    if exists:
        for dirName,subdirs,file  in os.walk(path):
            for filen in fileList:
                path = os.path.jion(dirName,filen)
                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                        dups[file_hash] = [path]

        return dups 
    else:
        print("Invalide path")    
        
def printDuplicate(dict1):
    result = list(filter(lambda x: len(x) > 1,dict1.values())) 

    if len(resilts) > 0:
        print("Duplicate Found:")       

        print("The following fie are identical.")

        icnt = 0
        for result in results:
            for subresult in result:
                icnt+1
                if icnt >=2:
                    print('\t\t%s'%subresult)
                icnt = 0

            

            else:
                print("No Duplicate file found.") 

def main():


    print("Application name :" +argv[0])    

    if(len(argv) !=2):
        print("Error : Invalid number of arguments")
        exit()    

    if(argv[1] == "-h") or (argv[1] == "-H"):
       print("This script is used traverse specific directory and display size of files")
       exit()

    if(argv[1] == "-u") or (argv[1]== "-U"):
       print("Usage : Application Absolutepath_of_Directory Exteention")
       exit()   

    try:
        arr = {}
        arr = FindDuplicate(argv[1])
        printDuplicate(arr)

    except ValueError:
        print("Error : Inalid datatype of input")

if __name__ == "__main__":
    main()






