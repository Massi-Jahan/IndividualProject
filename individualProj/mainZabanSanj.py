"""We use "importlib" package for accessing the internals
of import-statments---zabanSanjGUI and plotZaban"""
import importlib
import zabanSanjGUI
import plotZaban

command = None
files = None
results = None

"""To select a function from drop-down button (Funtions) on 
ZabanSanj we create "chandCommand" which will be used later
down "zabanSanjGUI.combo.bind...."""


def changeCommand(event):
    commandName = zabanSanjGUI.comboStringVar.get()
    global command
    command = importlib.import_module("Commands." + commandName)


"""excuteCommand() is for: 
1- to link both entries (path_to_file and file_names) and the
text box (The Output) on Zaban Sanj with their code files so
that the users can type in the paths and names of the files
on the app.
2- To print the result/output on "The Output" box.  """


def executeCommand():
    filePath = zabanSanjGUI.path_to_files.get()
    fileNames = zabanSanjGUI.file_names.get("1.0", "end")
    global files, results
    files, results = command.execute(filePath, fileNames)
    zabanSanjGUI.output_box.delete("1.0", "end")
    for i in range(len(files)):  # starts with 0
        lineNumber = i + 1
        zabanSanjGUI.output_box.insert("end", files[i] + " " + str(results[i]) + "\n")


"""The purpose of "plot()" is to use "plotZaban" for  plotting
 the output in the "The Output" box"""


def plot():
    plotZaban.plotBarchartOfWordcountFromFiles(files, results)


# We use the functions created above to execute them.
zabanSanjGUI.buttonPlot.configure(command=plot)
zabanSanjGUI.buttonOutput.configure(command=executeCommand)
zabanSanjGUI.combo.bind("<<ComboboxSelected>>", changeCommand)


zabanSanjGUI.window.mainloop()
