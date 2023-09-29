name = "help"
description = "command that shows a list of commands"

def execute(commandName = ""):
    if commandName == "":
        print ("I am helping you")
    else:
        print ("command you want help for is: " + commandName)

if __name__ == '__main__':
    execute()

    execute("plot")
