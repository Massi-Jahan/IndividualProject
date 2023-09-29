# The libraries we use below in the code.
import os
import nltk
from nltk.tokenize import sent_tokenize

"""In "getDataFromFiles(x,y)" function, we do the 
paragraph or verse count of the files accessed."""


def getDataFromFiles(filePath, files):
    listOfFileNames = []
    listOfParaghraphOrVerseCounts = []

    listOfFiles = files.split()

    fileExtension = ".txt"
    """Read the files from listOfFiles and do the 
    paragraph or verse count. Add both file names
    and the word count result to the above list 
    which will be accessed later in Zaban Sanj."""
    for file in listOfFiles:
        with open(
            os.path.join(filePath, file + fileExtension), "r", encoding="utf-8"
        ) as f:
            number_of_paraghraphs = 0
            text = f.read()
            paraghraphs = sent_tokenize(text)
            number_of_paraghraphs = len(paraghraphs)
            listOfFileNames.append(file)
            listOfParaghraphOrVerseCounts.append(number_of_paraghraphs)
            print(file + ": " + str(number_of_paraghraphs))
    """Return the lists we created above (listOfFileNames and
    listOfParagraphOrVerseCounts)to be accessed later."""
    return [listOfFileNames, listOfParaghraphOrVerseCounts]


# We execute the "getDataFromFiles(x,y) function.
def execute(filePath, fileNames):
    [fileName, paragraphCount] = getDataFromFiles(filePath, fileNames)
    return [fileName, paragraphCount]


if __name__ == "__main__":
    execute()
