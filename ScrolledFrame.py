import tkinter as tk


class ScrolledFrame(tk.Frame):

    def __init__(self, parent, vertical=True, horizontal=False):
        super().__init__(parent)

        # canvas for inner frame
        self._canvas = tk.Canvas(self, height=900)
        self._canvas.grid(row=0, column=0, sticky='news')  # changed

        # create right scrollbar and connect to canvas Y
        self._vertical_bar = tk.Scrollbar(self, orient='vertical', command=self._canvas.yview)
        if vertical:
            self._vertical_bar.grid(row=0, column=1, sticky='ns')
        self._canvas.configure(yscrollcommand=self._vertical_bar.set)

        # create bottom scrollbar and connect to canvas X
        # self._horizontal_bar = tk.Scrollbar(self, orient='horizontal', command=self._canvas.xview)
        # if horizontal:
        #     self._horizontal_bar.grid(row=1, column=0, sticky='we')
        # self._canvas.configure(xscrollcommand=self._horizontal_bar.set)

        # Bind scroll wheel
        self._canvas.bind_all("<MouseWheel>", self._on_mousewheel)

        # inner frame for widgets
        self.inner = tk.Frame(self._canvas)
        self._window = self._canvas.create_window((0, 0), window=self.inner, anchor='nw')

        # autoresize inner frame
        self.columnconfigure(0, weight=1)  # changed
        self.rowconfigure(0, weight=1)  # changed

        # resize when configure changed
        self.inner.bind('<Configure>', self.resize)

        # resize inner frame to canvas size
        self.resize_width = False
        self.resize_height = False
        self._canvas.bind('<Configure>', self.inner_resize)

    def resize(self, event=None):
        self._canvas.configure(scrollregion=self._canvas.bbox('all'))

    def inner_resize(self, event):
        # resize inner frame to canvas size
        if self.resize_width:
            self._canvas.itemconfig(self._window, width=event.width)
        if self.resize_height:
            self._canvas.itemconfig(self._window, height=event.height)

    def _on_mousewheel(self, event):
        self._canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def get_canvas(self):
        return self._canvas

    def get_scrollbar(self):
        return self._vertical_bar

    def get_inner(self):
        return self.inner
