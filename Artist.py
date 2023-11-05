import tkinter as tk


def hide_collection(canvas, inner, scrollbar):
    scrollbar.grid_forget()
    canvas.unbind_all("<MouseWheel>")
    inner.config(cursor="arrow")

    for child in inner.winfo_children():
        child.destroy()


def display_artist(scrolled_frame, artist):
    canvas = scrolled_frame.get_canvas()
    inner = scrolled_frame.get_inner()
    scrollbar = scrolled_frame.get_scrollbar()
    hide_collection(canvas, inner, scrollbar)

    artist_info = tk.Frame(scrolled_frame.inner)
    label = tk.Label(artist_info, text=artist)
    label.pack(anchor=tk.NW)
