# Cycle
Cycle is a game where the players try to cut each other off using cycles that leave a trail behind them.

# Rules
Players can move up, down, left and right...
Player one moves using the W, S, A and D keys.
Player two moves using the I, K, J and L keys.
Each player's trail grows as they move.
Players try to maneuver so the opponent collides with their trail.

If a player collides with their opponent's trail...
    A "game over" message is displayed in the middle of the screen.
    The cycles turn white.
    Players keep moving and turning but don't run into each other.

## Getting Started
Make sure you have Python 3.8.0 or newer installed and running on your machine. Open a terminal and browse to the project's root folder. Start the program by running the following command.
```
python3 cycle
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the project folder. Select the main module inside the cycle folder and click the "run" icon.

## Project Structure
The project files and folders are organized as follows:
```
root                              (project root folder)
+-- greed                        (source code for game)
  +-- game 
    +-- casting
        +-- actor                    (specific classes)
        +-- cast                     (specific classes)
        +-- cycle                    (specific classes)
        +-- game_over_action         (specific classes)
        +-- score                    (specific classes)
    +-- directing
        +-- director                 (specific classes) 
    +-- scripting
        +-- action                   (specific classes)
        +-- control_actors_action    (specific classes)
        +-- draw_actors_action       (specific classes)
        +-- handle_collisions_action (specific classes)
        +-- move_actors_action       (specific classes)
        +-- script                   (specific classes)
    +-- services
       +-- keyboard_service          (specific classes)
       +-- video_service             (specific classes)
    +-- shared
        +-- color                    (specific classes)
        +-- point                    (specific classes) 
  +-- __main__.py                 (program entry point)
+-- README.md                            (general info)
```

## Required Technologies
* Python 3.8.0

## Authors
* Bright Yasefi
* Daniel Muzo
* Ricardo Rivas
* Shaira Silos
* George Blanchard