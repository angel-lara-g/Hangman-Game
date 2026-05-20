# Hangman Game 🪢

A classic Hangman word-guessing game built with Python and Tkinter. Players choose a word length, then guess letters one by one before the hangman is fully drawn. The game supports Spanish word lists out of the box, but works with any language as long as you add words to the data files.

---

## Technologies

- **Python 3**
- **Tkinter** — built-in Python GUI library
- **Pillow (PIL)** — image handling

---

## Features

- Word length selection (3 to 7 letters)
- 6-stage hangman image progression
- Full alphabet on-screen keyboard
- Win and lose result screens with navigation options
- Word reveal on game over
- Language-agnostic word lists — add any language by editing the data files

---

## The Process

The project is structured around a window-based flow where each screen is its own class:

1. **`playGame.py`** — entry point, launches the home screen
2. **`homeW.py`** — home screen with title and Start button
3. **`menuW.py`** — word-length selection menu; reads a random word from the chosen file via `FAdmin`
4. **`fAdmin.py`** — file utility that reads word lists and returns a random word as a character list
5. **`runningGameW.py`** — core gameplay: letter buttons, word slots, hangman image updates, and win/lose logic
6. **`winLoseW.py`** — result screen; offers options to return to the menu or replay

Word lists are stored as plain `.txt` files inside the `data/` folder (one word per line), grouped by letter count. Images are stored in the `views/` folder.

---

## Running the Project

### Prerequisites

Make sure you have Python 3 installed, then install the only external dependency:

```bash
pip install Pillow
```

### Launch

```bash
python playGame.py
```

---

## Project Structure

```
Hangman-Game/
│
├── data/
│   ├── words3.txt
│   ├── words4.txt
│   ├── words5.txt
│   ├── words6.txt
│   └── words7.txt
│
├── views/
│   ├── HangMan.PNG
│   ├── HM.PNG
│   ├── HM1.PNG ... HM6.PNG
│   ├── WIN.PNG
│   └── LOSE.PNG
│
├── playGame.py
├── homeW.py
├── menuW.py
├── fAdmin.py
├── runningGameW.py
├── winLoseW.py
└── README.md
```

---

## Demo





---

