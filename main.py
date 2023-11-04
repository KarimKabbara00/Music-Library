from tkinter import *

# window configuration
tk = Tk()
tk.overrideredirect()
width = tk.winfo_screenwidth()
height = tk.winfo_screenheight()
tk.geometry("%dx%d" % (width - 10, height - 10))
tk.state('zoomed')
tk.winfo_toplevel().title('Music Library')
print()
# launch application
tk.mainloop()
