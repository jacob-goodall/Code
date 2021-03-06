import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

filepath = ""
def open_file():
    global filepath
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("CSV", "*.csv*")]
    )
    if not filepath:
        return
    print(filepath)
    window.title(f"File Selector - {filepath}")

    f = open(filepath,'r')
    message = f.read()
    print(message)
    with open(filepath) as a:
        lines = a.readlines()
    new_list = [s.replace("\n", "") for s in lines]
    print(new_list)
    sorted_new_list = sorted(new_list)
    print(sorted_new_list)
    
    f.close()
    file = open(filepath,"r")
    Counter = 0
    
    # Reading from file
    Content = file.read()
    CoList = Content.split("\n")
    for i in CoList:
        if i:
            Counter += 1

    print("Number of People in List:",Counter)
    file.close()


window = tk.Tk()
window.title("File Selector")

txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="Open Files", command=open_file)
btn_open.grid(row=0, column=0, sticky="ew", padx=0, pady=0)
fr_buttons.grid(row=0, column=0, sticky="ns")

window.mainloop()