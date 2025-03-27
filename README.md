# Floppy Bird

A Python implementation of the classic Flappy Bird game using Pygame.

## Requirements

- Python 3.6 or higher
- Pygame 2.5.2

## Installation

1. Clone this repository
```bash
git clone https://github.com/farqani9/floppy_bird.git
cd floppy_bird
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

## How to Play

1. Run the game:
```bash
python main.py
```

2. Game Controls:
- Press SPACE to make the bird flap/jump
- Press SPACE to restart when game over
- Close the window to quit

## Game Features

- Simple and intuitive controls
- Score tracking
- Randomly generated pipes
- Game over screen with restart option
- Smooth bird physics with gravity

## Game Rules

- Navigate the bird through gaps between pipes
- Each successfully passed pipe pair awards 1 point
- Game ends if the bird hits a pipe or goes off screen
- Try to achieve the highest score possible!