import os

def main():
    print("Enter the name of file that you want to open for writing purpose :")
    Fname = input()

    if os.path.exists(Fname):
       fobj = open(Fname,"r")
       print("file is succusfully opened in write mode")


       Data = fobj.read(10)
       print(Data)

       fobj.close()
       
    else:
      print("Unable to open file as file is not present in the current directry")


if __name__=="__main__"  :
    main() 

 