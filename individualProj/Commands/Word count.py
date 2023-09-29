# The libraries we use below in the code.
import os

"""In "getDataFromFiles(x,y)" function, we do the 
word count of the files accessed."""


def getDataFromFiles(filePath, files):
    listOfFileNames = []
    listOfWordCounts = []

    listOfFiles = files.split()

    fileExtension = ".txt"
    """Read the files from listOfFiles and do the 
    word count. Add both file names and the word 
    count result to the above list which will be
    accessed later in Zaban Sanj."""
    for file in listOfFiles:
        with open(
            os.path.join(filePath, file + fileExtension), "r", encoding="utf-8"
        ) as f:
            number_of_words = 0
            text = f.read()
            lines = text.split()
            for word in lines:
                number_of_words += 1
            listOfFileNames.append(file)
            listOfWordCounts.append(number_of_words)
            print(file + ": " + str(number_of_words))
    """Return the lists we created above (listOfFileNames and
    listOfWordCounts)to be accessed later."""
    return [listOfFileNames, listOfWordCounts]


# We execute the "getDataFromFiles(x,y) function.
def execute(filePath, fileNames):
    [fileName, wordCount] = getDataFromFiles(filePath, fileNames)
    return [fileName, wordCount]


if __name__ == "__main__":
    execute()
