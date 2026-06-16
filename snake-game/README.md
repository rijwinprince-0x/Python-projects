# 🐍 Rijwin's Snake Game

A classic Snake game built with Python's `turtle` module — featuring persistent high score tracking across sessions.

## 🎮 How to Play

- Use **Arrow Keys** to move the snake
- Eat the 🟢 **green food** to grow and earn points
- Game resets if you hit a **wall** or your own **tail**
- Your **High Score** is saved automatically and persists between sessions!

## 🚀 How to Run

```bash
python main.py
```

## 📁 Project Structure
snake-game/

├── main.py          # Game loop and collision detection

├── snake.py         # Snake class — movement and growth

├── food.py          # Food class — random placement

├── scoreboard.py    # Score display and high score saving

├── data.txt         # Stores the persistent high score

└── README.md        # This file
