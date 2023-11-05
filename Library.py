import json
import tkinter as tk
from tkinter import Label, Frame
from PIL import Image, ImageTk
import helper_functions as hf
from Artist import display_artist

artist_x_pad = 20


def place_component(scrolled_frame, frame, image, label):
    frame.configure(padx=5, pady=5)

    artist_image = Label(frame, image=image)
    artist_image.image = image
    artist_image.pack()
    artist_image.bind('<Button-1>', lambda e, s=scrolled_frame, a=label: handle_click(e, s, a))

    artist_name = Label(frame, text=label, font=("Arial", 16))
    artist_name.pack()
    artist_name.bind('<Button-1>', handle_click)

    frame.bind('<Enter>', lambda e, s=scrolled_frame.inner, f=frame, a=artist_name: on_enter(e, s, f, a))
    frame.bind('<Leave>', lambda e, s=scrolled_frame.inner, f=frame, a=artist_name: on_leave(e, s, f, a))


def handle_click(event, canvas, artist):
    display_artist(canvas, artist)


def on_enter(event, body, frame, label):
    body.config(cursor="hand2")
    frame.configure(bg='gray')
    label.configure(bg='gray', fg="white")


def on_leave(event, body, frame, label):
    body.config(cursor="arrow")
    frame.configure(bg='SystemButtonFace')
    label.configure(bg='SystemButtonFace', fg="black")


def init(scrollable_frame):
    # Load JSON
    with open('data.json', 'r') as file:
        data = json.load(file)

    artists = []
    for entry in data:
        artists.append(entry['Artist Name'])

    # Sort alphabetically
    artists = hf.compile_artists(artists)

    # Display artists
    for letter in artists:

        col = 0

        # Title Letter
        letter_frame = Frame(scrollable_frame.inner)
        letter_frame.pack(anchor=tk.W, fill=tk.X, padx=(50, 0), pady=(15, 5))
        letter_label = Label(letter_frame, text=letter.upper(), font=("Arial", 18))
        letter_label.pack(anchor=tk.NW)

        separator = Frame(scrollable_frame.inner, height=2, width=1800, highlightthickness=2, highlightbackground="black")
        separator.pack(anchor=tk.W, fill=tk.X, padx=(50, 0), pady=(0, 10))

        parent_frame = Frame(scrollable_frame.inner)
        parent_frame.pack(anchor=tk.W, padx=(50, 0))
        for a in artists[letter]:

            # Load image
            i_name = 'logos/' + a + '.png'
            i = Image.open(i_name)
            i = i.resize((300, 250))
            i = ImageTk.PhotoImage(i)

            # Create Frame
            f = Frame(parent_frame)
            f.grid(row=0, column=col, padx=(0, artist_x_pad))

            # Place image
            place_component(scrollable_frame, f, i, a)

            col += 1
