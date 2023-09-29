# The libraries we use below in the code.
import sys
import zlib
import os

"""In "CompressFiles(x,y)" function, we compute the
compress code length using "zlib" the files accessed."""


def CompressFiles(pathToFiles, files):
    listOfSizesOfCompressedFiles = []
    listOfFileNames = []

    listOfFiles = files.split()
    """Read the files from listOfFiles and compute the 
    their (files) compress code length. Add both file 
    names and the output (files' compress code lengths) 
    to the above list which will be accessed later in 
    Zaban Sanj."""
    for file in listOfFiles:
        filePath = pathToFiles + "\\" + file + ".txt"
        with open(filePath, "r", encoding="utf-8") as f:
            text = f.read()
            compressedData = zlib.compress(text.encode("utf-8"))

            sizeOfCompressedData = sys.getsizeof(compressedData)
            listOfFileNames.append(file)
            listOfSizesOfCompressedFiles.append(sizeOfCompressedData)
            print(file + ": " + str(sizeOfCompressedData))
    """Return the lists we created above (listOfFileNames and
    listOfSizesOfCompressedFiles)to be accessed later."""
    return [listOfFileNames, listOfSizesOfCompressedFiles]


# Execute the function ---OriginalFiles(x,y)
def execute(filePath, fileNames):
    [fileName, sizeOfCompressedFiles] = CompressFiles(filePath, fileNames)
    return [fileName, sizeOfCompressedFiles]


if __name__ == "__main__":
    execute()
