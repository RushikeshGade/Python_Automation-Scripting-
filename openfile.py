import os

def main():
    print("Enter the name of file that you want to open :")
    Fname = input()

    if os.path.exists(Fname):
       fobj = open(Fname,"r")
       print("file is succusfully opened")
       print(fobj)

    else:

       open(Fname, "x")
       print("Unable to create file as file is not present in the current directry")


if __name__=="__main__"  :
    main() 

 