# The libraries we use below in the code.
import importlib
from matplotlib import pyplot as plt

"""In "plotBarchartOfWordcountFromFiles(x,y)" function, we plot the 
output of the files accessed."""


def plotBarchartOfWordcountFromFiles(fileNames, fileData):
    fig, ax = plt.subplots()
    for i in range(len(fileNames)):
        ax.text(
            i,
            fileData[i],
            fileData[i],
            ha="center",
            va="bottom",
            rotation="vertical",
            size=7,
        )
    ax.bar(fileNames, fileData)
    # Rotat the file names on x so that not write filenmaes on each other.
    ax.tick_params(axis="x", colors="black", rotation=40, labelsize=7)
    ax = plt.gca()
    plt.legend()
    plt.show()


if __name__ == "__main__":
    execute()
