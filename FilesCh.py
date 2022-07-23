# ! important libaries
import os
from os import path
def main():
    # If the directory already exist, prevents an error from showing up and instead prints the exception
    try:
        # create the path to the named folder using this file's path
        src = path.realpath("Results")

        # create the directory using source path
        os.makedirs(src)

        # creates the file in the specified path
        pat = os.path.join(src, "result.txt")
        myfile = open(pat, "a+")

        # loop to get the byte size of each file in the current directory
        t = 0 # counter variable
        for filename in os.listdir():
            fsize = os.stat(filename) # gets the files states
            t = t + int(f'{fsize.st_size}') # converts the file stat to a string then an int

        myfile.write("Total Bytecount: " + str(t) + "\nFiles list:\n---------------\n")

        # loop to get the file names and write them into myfile
        for filename in os.listdir():
            if path.isfile(filename):
                myfile.write(filename + "\n")
        myfile.close() # closing the file
    except: # in case the directory already exists
        print("Oops, something went wrong")

if __name__ == "__main__":
    main()