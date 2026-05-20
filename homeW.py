"""
homeW.py
--------
Home screen window for the Hangman game.

Displays the main title, a decorative image, and a Start button
that transitions the player to the word-length selection menu.
"""

import tkinter as tk
from menuW import MenuW


class HomeW:
    """
    Home screen of the Hangman game.

    Shows the game title, a cover image, and a Start button.
    Serves as the entry point of the UI flow.
    """

    def __init__(self):
        """Initialize and display the home window."""
        self.window = tk.Tk()
        self.window.state('zoomed')
        self.window.title("Hangman")
        self.window.configure(background='#7c1324')
        self.init()
        self.window.mainloop()

    def init(self):
        """Build and place all widgets on the home screen."""
        self.lbl = tk.Label(
            text="HANGMAN",
            relief='flat',
            justify='center',
            width=0,
            font=('Monofonto', 45)
        )
        self.lbl.place(relx=0.5, rely=0.15, anchor='center')
        self.lbl.config(background="#7c1324", fg="white")

        self.im = tk.PhotoImage(file='views\HangMan.PNG')
        self.label = tk.Label(image=self.im)
        self.label.place(relx=0.5, rely=0.5, anchor='center')

        self.bttnStart = self._make_button("Start", self.start)
        self.bttnStart.place(relx=0.5, rely=0.8, anchor='center')

    def _make_button(self, text, command):
        """
        Create a styled button with the game's default appearance.

        Args:
            text (str): Label displayed on the button.
            command (callable): Function called when the button is clicked.

        Returns:
            tk.Button: Configured button widget (not yet placed).
        """
        btn = tk.Button(
            text=text,
            relief='flat',
            justify='center',
            width=0,
            font=('Monofonto', 18),
            command=command
        )
        btn.configure(background='black', fg="white")
        return btn

    def start(self):
        """Destroy the home window and open the menu screen."""
        self.window.destroy()
        MenuW(self)
