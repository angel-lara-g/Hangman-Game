"""
menuW.py
--------
Word-length selection menu window for the Hangman game.

Allows the player to choose the number of letters in the word
before starting a game session.
"""

import tkinter as tk
from functools import partial

from fAdmin import FAdmin
from runningGameW import RunningGameW


# Maps button labels to their corresponding word list files
WORD_OPTIONS = [
    ("3 LETRAS", "data\words3.txt"),
    ("4 LETRAS", "data\words4.txt"),
    ("5 LETRAS", "data\words5.txt"),
    ("6 LETRAS", "data\words6.txt"),
    ("7 LETRAS", "data\words7.txt"),
]


class MenuW:
    """
    Word-length selection menu of the Hangman game.

    Presents buttons for each available word length and a Play button
    to start the game once a length has been selected.
    """

    def __init__(self, menuW):
        """
        Initialize and display the menu window.

        Args:
            menuW: Reference to the previous window (HomeW instance).
        """
        self.menuW = menuW
        self.word = ""
        self.window = tk.Tk()
        self.window.state('zoomed')
        self.window.title("Hangman")
        self.window.configure(background='#7c1324')
        self.init()
        self.window.mainloop()

    def init(self):
        """Build and place all widgets on the menu screen."""
        self.label = tk.Label(
            self.window,
            text="Elige el tamaño de las palabras. \n Y después presiona 'Play' para comenzar a jugar ",
            relief='flat',
            justify='center',
            width=0,
            font=('Monofonto', 18)
        )
        self.label.grid(row=0, column=3, padx=400, pady=70)
        self.label.configure(background='#7c1324', fg="white")

        # Dynamically create one button per word-length option
        for row_index, (label, filepath) in enumerate(WORD_OPTIONS, start=1):
            btn = self._make_button(label, partial(self.election, filepath))
            btn.grid(row=row_index, column=3, padx=400, pady=5)

        self.bttnPlay = self._make_button("Play", self.play)
        self.bttnPlay.grid(row=len(WORD_OPTIONS) + 1, column=3, padx=400, pady=20)

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
            self.window,
            text=text,
            relief='flat',
            justify='center',
            width=0,
            font=('Monofonto', 18),
            command=command
        )
        btn.configure(background='black', fg="white")
        return btn

    def election(self, filename):
        """
        Load a random word from the selected word-length file.

        Args:
            filename (str): Path to the word list file.
        """
        self.word = FAdmin.readFile(filename)

    def play(self):
        """Hide the menu window and launch the game with the selected word."""
        self.window.withdraw()
        RunningGameW(self, self.word)
