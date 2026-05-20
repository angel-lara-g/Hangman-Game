"""
fAdmin.py
---------
File administration module for the Hangman game.

Handles reading word lists from text files and randomly
selecting a word for each game session.
"""

import random


class FAdmin:
    """Utility class for file operations related to word management."""

    @staticmethod
    def readFile(fileName):
        """
        Read a word list file and return a randomly selected word as a list of characters.

        Opens the given file, loads all words, picks one at random,
        and returns it as a list of uppercase characters for use in the game.

        Args:
            fileName (str): Path to the text file containing one word per line.

        Returns:
            list[str]: A list of individual characters from the randomly selected word.

        Example:
            >>> word = FAdmin.readFile("data/words5.txt")
            >>> print(word)  # ['G', 'A', 'T', 'O', 'S']
        """
        with open(fileName, 'r') as file:
            words = [line.strip() for line in file if line.strip()]

        word = random.choice(words)
        return list(word)
