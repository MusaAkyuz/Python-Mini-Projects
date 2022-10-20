# importing zip library
import zipfile
# importing sys to take arguments from command line
import sys


# accepts only one argument
if len(sys.argv) != 2:
    print("Error, takes only 1 argument. Check zipdir --help")

else:
    # checking correct arguments which zipfile
    if zipfile.is_zipfile(sys.argv[1]):
        with zipfile.ZipFile(sys.argv[1], "r") as archiveFile:
            archiveFile.printdir()
    elif sys.argv[1] == "--help":
        print("---Usage---\n")
        print("zipdir.py [argument]\n")
        print("Argument must be zip file or zip file path")

    else:
        print("The argument must be a zip file!")

