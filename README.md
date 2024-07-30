# Dice-Roll-Game

A simple command-line dice rolling game where two players compete by rolling a die in multiple rounds. The player with the highest roll wins the round, and the player with the most round wins is the overall winner.

## Introduction

The Dice-Roll-Game is a fun and simple game where two players take turns rolling a six-sided die. Each player rolls the die, and the one with the higher roll wins the round. The game is played over a set number of rounds, and the player with the most round wins is declared the winner.

## Features

- **Two-Player Game**: Players can input their names and compete against each other.
- **Randomized Dice Rolls**: The game uses Python's random module to simulate dice rolls.
- **Round Tracking**: Keeps track of the number of rounds won by each player.
- **Winner Announcement**: Announces the winner after all rounds are completed, or declares a draw if both players win an equal number of rounds.

## Game Rules

1. **Players**: Two players input their names at the start of the game.
2. **Dice Roll**: Each player rolls a six-sided die.
3. **Round Win**: The player with the higher roll wins the round. If both players roll the same number, the round is a draw.
4. **Game Win**: The player with the most rounds won after a set number of rounds is declared the winner. If both players win an equal number of rounds, the game is declared a draw.

## Technologies Used

- **Python**: The programming language used to implement the game logic.
- **Random Module**: Used to generate random numbers simulating dice rolls.

## Setup

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/Pudamya/Dice-Roll-Game.git
   ```

2. **Navigate to the Repository Directory**:
   ```sh
   cd Dice-Roll-Game
   ```

## Usage

1. **Run the Game**:
   ```sh
   python dice_roll_game.py
   ```

2. **Gameplay**:
   - The game prompts each player to enter their name.
   - The players take turns rolling a virtual die.
   - The game displays the result of each round and the current score.
   - After the set number of rounds, the game announces the overall winner or declares a draw.

## Contributing

Contributions are welcome! Please fork this repository and submit pull requests for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

