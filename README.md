# Kaooa

## How to Run the Game

1. **Navigate to the Game Directory**
   - Change your directory to the one containing the game file.

2. **Execute the Game**
   - Run the game using the following command:
     ```bash
     python3 file_name.py
     ```

## How to Play

### Game Setup
- **Crows' Turn**: The game begins with placing the crows on the board.

### Moving Pieces
- **Moving a Crow**:
  - Select the crow you wish to move.
  - Choose an empty spot on the board where you want to place the selected crow.
  - If the move is invalid, an error message will be displayed on the command-line interface (CLI).

- **Moving the Vulture**:
  - The vulture moves automatically; you only need to select a valid spot for it during its turn.
  - If no valid move is available for the vulture, the crows win the game.

### Winning Conditions
- **Crow's Victory**: The crows win if the vulture has no valid moves left.
- **Vulture's Victory**: The vulture wins if it manages to eat 4 crows.

### Game End
- When a player wins, on clicking on the screen a victory message will be displayed.
- The game screen will automatically close after 3 seconds.

## Error Handling
- Any invalid moves or errors will be indicated with messages displayed on the CLI to guide the player in making valid moves.

Enjoy the game and may the best player win!

