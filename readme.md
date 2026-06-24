# Advanced Hangman Game

## Project Title

Advanced Hangman Game using Flask

## Description

The Advanced Hangman Game is a web-based word guessing game developed using Python Flask. The player selects a difficulty level and tries to guess the hidden word one letter at a time. The game awards points for correct guesses and deducts points for incorrect guesses. The player wins by revealing the complete word before losing all available lives.

## Objectives

* To develop an interactive web application using Flask.
* To implement session management for storing game data.
* To enhance problem-solving and logical thinking skills through gameplay.
* To provide an engaging user experience with a score-based system.

## Features

* Three difficulty levels: Easy, Medium, and Hard.
* Random word selection based on difficulty.
* Score tracking system.
* Lives counter.
* Win and loss detection.
* Play Again option.
* Attractive user interface with background image and styling.

## Technologies Used

* Python
* Flask
* HTML5
* CSS3

## Software Requirements

* Python 3.x
* Flask Library
* Visual Studio Code
* Web Browser (Chrome, Edge, Firefox, etc.)

## Project Structure

Hangman Game

* app.py (Main Flask Application)
* templates/

  * index.html (User Interface)

## Working Procedure

1. The user opens the Hangman Game in the browser.
2. The user selects a difficulty level.
3. A random word is chosen from the selected category.
4. The word is displayed as hidden characters (_ _ _).
5. The player enters one letter at a time.
6. Correct guesses reveal letters and increase the score.
7. Incorrect guesses reduce lives and deduct points.
8. The game continues until the word is guessed or all lives are lost.
9. A winning message is displayed when the word is completed.
10. A game over message is displayed when lives reach zero.
11. The player can restart the game using the Play Again button.

## Scoring System

* Correct Guess: +10 Points
* Incorrect Guess: -5 Points
* Winning Bonus: +50 Points

## How to Run the Project

1. Install Python on your system.

2. Install Flask using:

   pip install flask

3. Save app.py and index.html in the appropriate project folders.

4. Open the project folder in VS Code.

5. Run the command:

   python app.py

6. Open the browser and visit:

   http://127.0.0.1:5000

## Expected Output

The application displays a Hangman Game interface where users can select a difficulty level, guess letters, view their score, monitor remaining lives, and receive win or loss messages based on their performance.

## Result

The Advanced Hangman Game was successfully developed using Flask. The application provides an interactive and user-friendly environment for word guessing with scoring, difficulty levels, and session management features.
