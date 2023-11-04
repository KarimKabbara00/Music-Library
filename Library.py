import json
from tkinter import Label, Frame
from PIL import Image, ImageTk

artist_x_pad = 100
artists_per_row = 3


def place_component(frame, image, label):
    artist_image = Label(frame, image=image)
    artist_image.image = image
    artist_image.pack()
    artist_image.bind('<Button-1>', lambda e, a=label: handle_click(e, a))

    artist_name = Label(frame, text=label, font=("Arial", 16))
    artist_name.pack()
    artist_name.bind('<Button-1>', handle_click)


def handle_click(event, artist):
    print(artist)


def init(body):
    with open('data.json', 'r') as f:
        data = json.load(f)

    artists = []
    for entry in data:
        artists.append(entry['Artist Name'])

    artists = sorted(list(set(artists)))

    row = col = 0
    for a in artists:

        # Load image
        i_name = 'logos/' + a + '.png'
        i = Image.open(i_name)
        i = i.resize((300, 250))
        i = ImageTk.PhotoImage(i)

        if col == 0:
            # Create Frame
            f = Frame(body)
            f.grid(row=row, column=col, padx=(0, artist_x_pad), pady=(20, 20))

            # Place image
            place_component(f, i, a)

            col += 1

        elif col == artists_per_row:

            # Create Frame
            f = Frame(body, padx=20, pady=20, width=300, height=300)
            f.grid(row=row, column=col, padx=(artist_x_pad, 0), pady=(20, 20))

            # Place image
            place_component(f, i, a)

            row += 1
            col = 0

        else:
            # Create Frame
            f = Frame(body)
            f.grid(row=row, column=col, padx=(artist_x_pad, artist_x_pad), pady=(20, 20))

            # Place image
            place_component(f, i, a)

            col += 1
