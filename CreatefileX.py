import os

def main():
    print("Enter the name of file that you want to creare :")
    Fname = input()

    if os.path.exists(Fname):
        print("Unable to create file as file is already existing")

    else:

       open(Fname, "x")
       print("file gets succesfully created")


if __name__=="__main__"  :
    main() 

# Absolute path :
# Relative path : Automation/Marvellous 