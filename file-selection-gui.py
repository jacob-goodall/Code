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

    print(lines)

    new_list = [s.replace("\n", "") for s in lines]

    print(new_list)
    f.close()

window = tk.Tk()
window.title("File Selector")

txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="Open Files", command=open_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=0, pady=0)

fr_buttons.grid(row=0, column=0, sticky="ns")

window.mainloop()


