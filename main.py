import tkinter as tk
import Library as lib

# window configuration
root = tk.Tk()
root.overrideredirect()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width - 10, height - 10))
root.state("zoomed")
root.winfo_toplevel().title("Music Library")

header = tk.Frame(root)
header.grid(row=0, column=0)

body = tk.Frame(root, highlightbackground="black", highlightthickness=1)
body.grid(row=1, column=0, pady=40)

menu_label = tk.Label(header, text="Your Collection", font=("Arial", 25))
menu_label.pack(anchor=tk.CENTER, pady=(50, 0), ipadx=100)

lib.init(body)

# launch application
root.grid_columnconfigure(0, weight=1)
root.mainloop()
