# The libraries we use below in the code.
import sys
import zlib
import os

"""In "OriginalFiles(x,y)" function, we compute the
original size of the files accessed."""


def OriginalFiles(pathToFiles, files):
    listOfFileNames = []
    listOfOriginalSizes = []

    listOfFiles = files.split()
    """Read the files from listOfFiles and compute the 
    their (files) original sizes. Add both file names 
    and the output (files' original sizes) to the above
    list which will be accessed later in Zaban Sanj."""
    for file in listOfFiles:
        filePath = pathToFiles + "\\" + file + ".txt"
        with open(filePath, "r", encoding="utf-8") as f:
            text = f.read()
            listOfFileNames.append(file)
            sizeOfOriginalFiles = len(text)
            listOfOriginalSizes.append(sizeOfOriginalFiles)

            print(file + ": " + str(sizeOfOriginalFiles))
    """Return the lists we created above (listOfFileNames and
    listOfOriginalSizes)to be accessed later."""
    return [listOfFileNames, listOfOriginalSizes]


# Execute the function ---OriginalFiles(x,y)
def execute(filePath, fileNames):
    [fileName, sizeOfOriginalFiles] = OriginalFiles(filePath, fileNames)
    return [fileName, sizeOfOriginalFiles]


if __name__ == "__main__":
    execute()
