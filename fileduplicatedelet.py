from sys import *
import os
import hashlib
import time

def DeleteFile(dict1):
    result = list(filter(lambda x: len(x)> 1, dict1.value()))

    icnt = 0

    if len(resuls)>0:
        for result in results:
            for subresult in result:
                icnt+ 1
                if icnt >=2:
                    os.remove(subresult)
                icnt = 0
            else:
                print("No Duplicate file found.") 

def hashfile(path, blocksize = 1024):
    afile =open(pah,'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()

    return hasher.hextdigest()

def FindDup(path):
    flag = os.path.isabs(path) 

    if flag  == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)  

    dups = {}

    if exists:
        for dirName,subdirs,fileList in os.walk(path):
            print("Current folder is :"+dirName)
            for filen in fileList:
                path = os.path.jion(dirName,filen)
                file_hash = hashfile(path)

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
        print("The following fie are identical")
        for result in results:
            for subresult in result:
                print('\t\t%s'%subresult)
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
        startTime = time.time()
        arr = findDup(argv[1])
        print(arr)
        DeleteFile(arr)
        endTime = time.time()

        print('Tool %s second to evaluate.'%(endTime - startTime))
   
    except ValueError:
        print("Error : Inalid datatype of input")

    except Exception as E:
           print("Error : Invalid input",E)    

if __name__ == "__main__":
    main()






