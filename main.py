import tkinter as tk
import Library as lib
from ScrolledFrame import ScrolledFrame

# window configuration
root = tk.Tk()
root.overrideredirect()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width - 10, height - 10))
root.state("zoomed")
root.winfo_toplevel().title("Music Library")

header = tk.Frame(root)
header.pack(pady=(0, 30))

body = ScrolledFrame(root)
body.pack(fill=tk.BOTH, padx=(0, 0))

menu_label = tk.Label(header, text="My Collection", font=("Arial", 25))
menu_label.pack(anchor=tk.CENTER, pady=(50, 0), ipadx=100)

lib.init(body)

# launch application
root.grid_columnconfigure(0, weight=1)
root.mainloop()
