# Rock, Paper, Scissors Game 🪨📜✂️

A classic Rock, Paper, Scissors game implemented in Python. Play against the computer, which makes a random choice each round.

---

## 🚀 Getting Started

### Prerequisites

You'll need Python 3 installed on your system to run this game.

### How to Run

1.  Save the complete code from the image into a file named rps.py.
2.  Open your terminal or command prompt.
3.  Navigate to the directory where you saved the file.
4.  Run the game using the Python interpreter:

    ```bash
    python rps.py
    ```
---

## 🎮 How to Play

The game will run in a loop, allowing you to play multiple rounds.

1.  When prompted, enter your choice:
    * r for Rock
    * p for Paper
    * s for Scissors
    * *You can also type out the full words (Rock, Paper, or Scissors).*
2.  The program will display both your choice and the computer's choice using emojis.
3.  The winner is determined and the result is printed: "Draw", "you win", or "you lose".
4.  After the round, you'll be asked: "Continue? (y/n)".
    * Enter **n** to exit the game.
    * Enter **y** (or any other key) to play another round.

---

## 💻 Code Structure

The game is modularized into several clear functions for readability and maintenance:

| Function | Purpose |
| :--- | :--- |
| get_user_choice() | Prompts the user for input, validates it against allowed choices, and returns the valid choice. |
| display_choices() | Prints the choices made by the user and the computer, using emojis for a visual flair. |
| determine_winner() | Contains the core game logic to check the user's choice against the computer's choice and prints the result. |
| play_game() | The main game loop that orchestrates user input, computer choice generation, display, and winner determination. |

### Core Variables

| Variable | Description |
| :--- | :--- |
| ROCK, PAPER, SCISSORS | Constants defined for the single-letter choice keys. |
| EMOJIS | A dictionary mapping the single-letter choices to fun emojis. |
| choices | A tuple containing the valid single-letter keys (r, p, s) for easy validation. |
