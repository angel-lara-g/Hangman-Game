"""
winLoseW.py
-----------
Win/Lose result window for the Hangman game.

Displays the outcome image (win or lose) and provides buttons
to return to the menu or replay the current game.
"""

import tkinter as tk


# Result constants for clarity
RESULT_LOSE = 0
RESULT_WIN = 1

# Maps result code to its corresponding image path
_RESULT_IMAGES = {
    RESULT_WIN:  'views\WIN.PNG',
    RESULT_LOSE: 'views\LOSE.PNG',
}


class WinLose:
    """
    Result screen shown at the end of a Hangman game session.

    Displays a win or lose image and offers navigation options
    to go back to the menu or retry the current game.
    """

    def __init__(self, runningGameW, result):
        """
        Initialize and display the result window.

        Args:
            runningGameW (RunningGameW): Reference to the active game window.
            result (int): Game outcome — use RESULT_WIN (1) or RESULT_LOSE (0).
        """
        self.runningGameW = runningGameW
        self.result = result
        self.window = tk.Toplevel()
        self.window.state('zoomed')
        self.window.title("Hangman")
        self.window.configure(background='#7c1324')
        self.init()
        self.window.mainloop()

    def init(self):
        """Build and place all widgets on the result screen."""
        # Display win or lose image based on result
        image_path = _RESULT_IMAGES.get(self.result)
        if image_path:
            self.im = tk.PhotoImage(file=image_path)
            self.label = tk.Label(self.window, image=self.im)
            self.label.place(relx=0.5, rely=0.5, anchor='center')

        self.bttnMenuW = self._make_button("Menú", self.menu)
        self.bttnMenuW.place(relx=0.9, rely=0.3, anchor='center')

        self.bttnGoBack = self._make_button("Regresar", self.goBack)
        self.bttnGoBack.place(relx=0.9, rely=0.1, anchor='center')

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

    def menu(self):
        """Destroy the result and game windows, and return to the menu screen."""
        self.window.destroy()
        self.runningGameW.window.destroy()
        self.runningGameW.menuW.window.deiconify()
        self.runningGameW.menuW.window.state('zoomed')

    def goBack(self):
        """Close the result window and resume the current game screen."""
        self.window.destroy()
        self.runningGameW.window.deiconify()
        self.runningGameW.window.state('zoomed')
