# The libraries we use below in the code.
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


window = tk.Tk()
window.title("Zaban Sanj")
# Turn on min/max buttons
window.attributes("-toolwindow", False)
frame = tk.Frame(window)
frame.pack()

# Window where users type in file path and the file names.
user_info_window = tk.LabelFrame(
    frame,
    text="File Information",
    foreground="red",
    font=("Times", 10),
)
user_info_window.grid(row=0, column=0, padx=20, pady=10)

"""Entries for file paths or directory and file names to be 
typed in by users."""
first_name_label = tk.Label(user_info_window, text="Path to Files", font=("Times", 10))
first_name_label.grid(row=0, column=0)
last_name_label = tk.Label(user_info_window, text="File Name", font=("Times", 10))
last_name_label.grid(row=1, column=0)

path_to_files = tk.Entry(user_info_window, width=54, font=("Times", 10), border=3)
path_to_files.grid(row=0, column=1)

file_names = fileBox = tk.Text(
    user_info_window,
    height=3,
    width=40,
    background="white",
    foreground="blue",
    border=5,
)
file_names.grid(row=1, column=1)
"""Drop-down buttions (Functions) which has functions on it that
the users should select for computing/calculating their files"""

title_label = tk.Label(user_info_window, text="Functions", font=("Times", 12))
title_label.grid(row=0, column=2)
# Add style and colors to the drop-down buttons (functions)
combostyle = ttk.Style()
combostyle.theme_create(
    "combostyle",
    parent="alt",
    settings={
        "TCombobox": {
            "configure": {
                "selectbackground": "#6495ED",
                "fieldbackground": "#6495ED",
                "background": "green",
            }
        }
    },
)

combostyle.theme_use("combostyle")

combo = ttk.Combobox(
    user_info_window,
    values=[
        "",
        "Original size",
        "Character count",
        "Word count",
        "Paragraph count",
        "Compression",
    ],
    font=("Times", 10),
)
combo["state"] = "readonly"
combo.grid(row=0, column=3)


# combo stringvar
comboStringVar = tk.StringVar()
combo.configure(textvariable=comboStringVar)

"""The Output button which will execute the function selected 
by users"""
buttonOutput = tk.Button(
    user_info_window, text="Output", font=("Times", 10), width=10, border=5
)
buttonOutput.grid(row=2, column=3, pady=3)
# Output window, where the result of the files will be displayed

output_window = tk.LabelFrame(
    frame, text="The Output:", foreground="black", font=("Times", 10)
)
output_window.grid(row=1, column=0, sticky="news", padx=20, pady=10)

output_label = tk.Label(output_window, text="                     ")
output_label.grid(row=0, column=0)
output_box = tk.Text(
    output_window,
    height=5,
    width=45,
    background="white",
    foreground="blue",
    border=5,
)
output_box.grid(row=0, column=1)


output_label = tk.Label(output_window, text="              ")
output_label.grid(row=0, column=2)
buttonPlot = tk.Button(
    output_window, text="Plot", font=("Times", 10), width=10, border=5
)
buttonPlot.grid(row=1, column=3, padx=3, pady=3)
"""Help window where users can access the instruction 
on how to use the app"""


def create_help_window():
    help_window = tk.Toplevel()
    help_window.title("Help")
    help_window.geometry("400x300")
    tk.Label(
        help_window,
        text="Instructions:",
        font=("Times", 8, "bold"),
        border=5,
        fg="red",
    ).pack(anchor=tk.NW, padx=10, pady=2)
    tk.Label(
        help_window,
        text="1. Type in the path to the files you are aiming to access correctly.",
        font=("Times", 8),
        border=5,
    ).pack(anchor=tk.NW, padx=10, pady=2)
    tk.Label(
        help_window,
        text="2. Type in correct file names.",
        font=("Times", 8),
        border=4,
    ).pack(anchor=tk.NW, padx=10, pady=2)
    tk.Label(
        help_window,
        text="3. Select 'Functions' before pushing the 'Output' button.",
        font=("Times", 8),
        border=4,
    ).pack(anchor=tk.NW, padx=10, pady=2)
    tk.Label(
        help_window,
        text="4. To exhibit the output in a bar chart, push 'Plot' button.",
        font=("Times", 8),
        border=4,
    ).pack(anchor=tk.NW, padx=10, pady=2)
    tk.Button(
        help_window,
        text="Close",
        background="light blue",
        bd=5,
        command=help_window.destroy,
    ).pack(padx=10, pady=10, anchor=tk.SE, expand=True)


# Help button which is linked with the information window "Help window"
buttonHelp = tk.Button(
    frame,
    text="Help?",
    font=("Times", 10),
    width=10,
    border=5,
    command=create_help_window,
)
buttonHelp.place(x=20, y=340)

""" "yesNoMessegeBox" linked to the close button which will ask 
confirmation on closing button."""


def yes_no():
    yesNo = messagebox.askyesno(
        title="Confirmation", message="Are you sure that you want to quit?"
    )
    if yesNo:
        window.destroy()


# Clsoe button
buttonClose = tk.Button(
    frame, text="Close", font=("Times", 10), width=10, border=5, command=yes_no
)
buttonClose.grid(row=2, column=1, sticky="n", padx=20, pady=10)

if __name__ == "__main__":
    window.main()
