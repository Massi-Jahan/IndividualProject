import sys
import zlib
import os


def OriginalFiles(pathToFiles, files):
    listOfOriginalSizes = []
    listOfFileNames = []

    listOfFiles = files.split()

    for file in listOfFiles:
        filePath = pathToFiles + "\\" + file + ".txt"
        with open(filePath, "r", encoding="utf-8") as f:
            text = f.read()
            # compressedData = zlib.compress(text.encode("utf-8"))

            sizeOfOriginalData = len(text)
            listOfFileNames.append(file)
            listOfOriginalSizes.append(sizeOfOriginalData)
            print(file + ": " + str(sizeOfOriginalData))

    return [listOfFileNames, listOfOriginalSizes]


def execute():
    filePath = input(
        "Type in a file path: "
    )  # how to close if the user no longer use the app?

    while not os.path.exists(filePath):
        print("Path of the file is Invalid")
        filePath = input("Please type in a valid path! ")

    files = input("Type in files: ")
    [fileName, sizeOfOriginalFiles] = OriginalFiles(filePath, files)
    return [fileName, sizeOfOriginalFiles]


if __name__ == "__main__":
    execute()
