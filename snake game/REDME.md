# Snake Game Projext
## Overview
This project is a classic Snake game implemented in Python using the Turtle graphics library and Object-Oriented Programming (OOP) concepts. The game involves controlling a snake to eat food, grow in size, and avoid collisions with walls and itself. The player's score is tracked and stored in a text file.

## Features
Classic Snake Gameplay: Control the snake to eat food and grow in length.

Turtle Graphics: Utilizes the Turtle graphics library for visual rendering.

OOP Design: Implemented using OOP principles for modularity and readability.

Collision Detection: Handles collisions with walls and the snake's own body.

Score Tracking: Keeps track of the player's score based on the number of food items eaten and stores the results in a text file.

## Prerequistites
Python 3.x

Turtle graphics library (usually included with Python's standard library)

## Instalation
1. Clone the Repository:
    ```sh
    git clone https://github.com/yourusername/snake-game.git
    cd snake-game
    
2. Run the Game:
    ```sh
    python main.py
## How to play
1. Start the Game: Run the main.py script.
Control the Snake:
2. Use the arrow keys (Up, Down, Left, Right) to control the direction of the snake.
3. Objective: Navigate the snake to eat the food that appears randomly on the screen.
4. Avoid Collisions: Do not let the snake collide with the walls or its own body.
## Project structure
1. `main.py`: The entry point of the game. Sets up the game window and initializes the game loop.
2. `snake.py`: Contains the Snake class that handles the snake's behavior and movement.
3. `food.py`: Contains the Food class that manages the appearance and placement of food items.
4. `scoreboard.py`: Contains the Scoreboard class that tracks and displays the player's score and saves it to a text file.
5. `data.txt`: A text file to store the scores.