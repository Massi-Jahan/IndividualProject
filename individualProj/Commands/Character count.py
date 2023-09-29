# The libraries we use below in the code.
import glob
import os

"""In "getDataFromFiles(x,y)" function, we do the 
character count of the files accessed."""


def getDataFromFiles(filePath, files):
    listOfFileNames = []
    listOfCharCounts = []

    listOfFiles = files.split()

    my_files = glob.glob(".txt")

    fileExtension = ".txt"
    """Read the files from listOfFiles and do the 
    character count. Add both file names and the
    caracter count result to the above list which
    will be accessed later in Zaban Sanj."""
    for file in listOfFiles:
        with open(
            os.path.join(filePath, file + fileExtension), "r", encoding="utf-8"
        ) as f:
            num_of_chars = 0
            text = f.read().strip().split()
            for line in text:
                num_of_chars += len(line)
            listOfFileNames.append(file)
            listOfCharCounts.append(num_of_chars)

            print(file + ": " + str(num_of_chars))
    """Return the lists we created above (listOfFileNames and
    listOfCharCounts)to be accessed later."""
    return [listOfFileNames, listOfCharCounts]


# We execute the "getDataFromFiles(x,y) function.
def execute(filePath, fileNames):
    [fileName, charsCount] = getDataFromFiles(filePath, fileNames)
    return [fileName, charsCount]


if __name__ == "__main__":
    execute()
