$$ Alien Invasion: A Python Pygame Project $$

## Project Overview

Alien Invasion is a 2D space shooter game developed in Python using the Pygame library.
This project serves as a demonstration of applying advanced programming concepts and software engineering principles in a fun and engaging way.
It not only highlights proficiency in Python and Pygame but also showcases the use of object-oriented programming for game development, event handling for interactive gameplay,
collision detection for realism in game mechanics, and game state management for a seamless user experience.

## Key Concepts Used

- **Object-Oriented Programming (OOP)**: Utilized for structuring the game's architecture, promoting code reusability and scalability.
- **Event Handling**: Manages user inputs and game events, ensuring responsive gameplay.
- **Collision Detection**: Implements algorithms to detect interactions between objects, crucial for gameplay dynamics.
- **Game State Management**: Controls the flow of the game, including start, ongoing gameplay, and game over scenarios.
- **Modular Design**: Facilitates scalability and maintenance, allowing for easy addition of new features or modification of existing ones.

## File Descriptions


# alien_invasion.py
The main game file, responsible for initializing the game, creating a screen, and managing the event loop that keeps the game running.

# settings.py
Contains the `Settings` class, which stores all configurable settings for the game, including screen size, ship speed, bullet properties, and alien settings.

# ship.py
Defines the `Ship` class, representing the player's spaceship. It includes functionality for drawing the ship and updating its position.

# bullets.py
Implements the `Bullet` class for managing the bullets fired by the player's ship, including their speed, direction, and drawing on the screen.

# aliens.py
Contains the `Alien` class, representing individual aliens in the fleet. It manages their appearance and movements.

# game_stats.py
Defines the `GameStats` class, tracking various game statistics such as the player's score and the number of ships remaining.

# scoreboard.py
Manages the scoreboard, displaying the player's current score, high score, and other relevant information during gameplay.

# start_button.py
Implements a `Button` class for the game's start button, displayed on the game's main menu to initiate gameplay.


## How to install pygame library
pip install pygame





