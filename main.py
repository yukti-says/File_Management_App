import os

# a function that will help user to create a file
def create_file(filename):
    try:
        with open(filename,'x') as f: #'x' will create file if not exists and fails if exists
            print(f"File Name {filename}: created successfully.")
    #two type of error can be occure here: file already exists or unexpected error        
    
    except FileExistsError:
        print(f"File Name {filename} already exists.")

    except Exception as e:
        print("an error occured. ")    


#a function to viewing files
def view_all_files():
    files = os.listdir() #will list all the files and directories in current directory
    if not files:
        print("NO file found. ")
    else:
        print("Files in directory.") 
        for file in files:
            print(file)

#delete file
def delete_file(filename):
    try:
        os.remove(filename)  #this methode will remove the file from machine
        print(f"{filename} deleted successfully!")

    except FileNotFoundError:
        print("File not Found.")

    except Exception as e:
        print("An unwanted error occured.")

# to reading a file
def read_file(filename):
    try:
        with open('sample.txt','r') as f:
            content=f.read()
            print(f"Content of '{filename}' :\n {content}")

    except FileNotFoundError:
        print("File does not exist.")

    except Exception as e:
        print("An unwanted error occured.")

# to edit a file
def edit_file(filename):
    try:
        with open('sample.txt','a') as f:
            content=input("Enter data to add: ") 
            f.write(content + "\n")
            print(f"Content added to {filename} successfully!") 

    except FileNotFoundError:
        print("File does not exits.")

    except Exception as e:
        print("An unwanted error occured.")

# main function and options for users
def main():
    while True:
        print(".............FILE MANAGEMENT APP..............")
        print('1: Create File: ')
        print('2: View ALL File: ')
        print('3: Delete File: ')
        print('4: Read File: ')
        print('5: Edit File: ')
        print('6: Exit! ')


        choice=input("Enter your choice b/w(1-6) = ")

        if choice=='1':
            filename=input("Enter the file name to create: ")
            create_file(filename)

        elif choice=='2':
            view_all_files()

        elif choice=='3':
            filename=input("Enter the name of file you want to delete= ")
            delete_file(filename)

        elif choice=='4':
            filename=input("Enter file name to read= ")
            read_file(filename)

        elif choice=='5':
            filename=input("Enter the file name to edit= ")
            edit_file(filename)

        elif choice=='6':
            print("............CLOSING THE APP.............")
            break

        else:
            print("invalid ")
            exit

if __name__=="__main__":
    main()

