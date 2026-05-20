"""
runningGameW.py
---------------
Main gameplay window for the Hangman game.

Handles letter guessing, word display, hangman image progression,
and win/lose condition checking during an active game session.
"""

import tkinter as tk
from functools import partial

from winLoseW import WinLose


# Alphabet layout: first row (A-S) and second row (T-Z)
_ROW1_LETTERS = list("ABCDEFGHIJKLMNOPQRS")
_ROW2_LETTERS = list("TUVWXYZ")

# Horizontal positions for each word length (3–7 letters)
_LABEL_POSITIONS = {
    3: [0.4, 0.5, 0.6],
    4: [0.35, 0.45, 0.55, 0.65],
    5: [0.3, 0.4, 0.5, 0.6, 0.7],
    6: [0.25, 0.35, 0.45, 0.55, 0.65, 0.75],
    7: [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8],
}


class RunningGameW:
    """
    Active game window for the Hangman game.

    Displays the hangman image, letter buttons, and word slots.
    Tracks errors and matches, and triggers win/lose screens accordingly.
    """

    def __init__(self, menuW, word):
        """
        Initialize and display the game window.

        Args:
            menuW (MenuW): Reference to the menu window, used for navigation.
            word (list[str]): The target word as a list of characters.
        """
        self.error = 0
        self.match = 0
        self.menuW = menuW
        self.word = word
        self.lWord = len(self.word)

        self.window = tk.Toplevel()
        self.window.state('zoomed')
        self.window.title("Hangman")
        self.window.configure(background='#7c1324')
        self.init()
        self.window.mainloop()

    def init(self):
        """Build and place all widgets for the game screen."""
        # Warning label
        self.lbl = tk.Label(
            self.window,
            text="Es posible presionar el mismo \nbotón más de una vez. \n\n ¡Ten mucho cuidado!",
            relief='flat',
            justify='center',
            width=0,
            font=('Monofonto', 15)
        )
        self.lbl.place(relx=0.2, rely=0.3, anchor='center')
        self.lbl.config(background="#7c1324", fg="white")

        # Word slot labels — one per letter
        self.letter_labels = []
        positions = _LABEL_POSITIONS.get(self.lWord, [])
        for relx in positions:
            lbl = tk.Label(
                self.window,
                text="   ",
                relief='flat',
                justify='center',
                width=0,
                font=('Monofonto', 18)
            )
            lbl.place(relx=relx, rely=0.6, anchor='center')
            self.letter_labels.append(lbl)

        # Menu button
        self.bttnMenuW = self._make_button("Menú", self.menu)
        self.bttnMenuW.place(relx=0.9, rely=0.1, anchor='center')

        # Alphabet buttons — Row 1 (A–S)
        for i, letter in enumerate(_ROW1_LETTERS):
            relx = 0.05 + i * 0.05
            btn = self._make_button(letter, partial(self.verify, letter))
            btn.place(relx=relx, rely=0.75, anchor='center')

        # Alphabet buttons — Row 2 (T–Z)
        for i, letter in enumerate(_ROW2_LETTERS):
            relx = 0.35 + i * 0.05
            btn = self._make_button(letter, partial(self.verify, letter))
            btn.place(relx=relx, rely=0.85, anchor='center')

        # Hangman images (HM = no errors, HM1–HM6 = progressive errors)
        self.images = [
            tk.PhotoImage(file='views\HM.PNG'),
            tk.PhotoImage(file='views\HM1.PNG'),
            tk.PhotoImage(file='views\HM2.PNG'),
            tk.PhotoImage(file='views\HM3.PNG'),
            tk.PhotoImage(file='views\HM4.PNG'),
            tk.PhotoImage(file='views\HM5.PNG'),
            tk.PhotoImage(file='views\HM6.PNG'),
        ]

        self.label = tk.Label(self.window, image=self.images[0])
        self.label.place(relx=0.5, rely=0.3, anchor='center')

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

    def verify(self, letter):
        """
        Check whether the guessed letter exists in the target word.

        Updates the word slots if the letter matches, increments the
        error counter if it doesn't, updates the hangman image, and
        checks for win/lose conditions.

        Args:
            letter (str): The letter guessed by the player.
        """
        previous_match = self.match

        for i, char in enumerate(self.word):
            if char == letter:
                self.letter_labels[i].config(text=f" {letter} ")
                self.match += 1

        if self.match == previous_match:
            self.error += 1

        # Update hangman image based on error count
        if self.error <= 6:
            self.label.configure(image=self.images[self.error])
            self.label.place(relx=0.5, rely=0.3, anchor='center')

        # Check win condition
        if self.match >= self.lWord:
            self.win()
            return

        # Check lose condition — reveal the full word
        if self.error >= 6:
            for i, char in enumerate(self.word):
                self.letter_labels[i].config(text=f" {char} ")
            self.lose()

    def win(self):
        """Hide the game window and display the win screen."""
        self.window.withdraw()
        WinLose(self, 1)

    def lose(self):
        """Hide the game window and display the lose screen."""
        self.window.withdraw()
        WinLose(self, 0)

    def menu(self):
        """Destroy the game window and return to the menu screen."""
        self.window.destroy()
        self.menuW.window.deiconify()
        self.menuW.window.state('zoomed')
