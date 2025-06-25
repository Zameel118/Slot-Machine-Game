# Slot Machine Game 🎰

A simple command-line slot machine game built in Python. Test your luck and see if you can hit the jackpot!

## Features

- **Interactive Gameplay**: Command-line interface with user input validation
- **Customizable Betting**: Choose how many lines to bet on (1-3) and your bet amount ($1-$100)
- **Multiple Symbols**: Four different symbols (A, B, C, D) with varying rarities and payouts
- **Balance Management**: Deposit money, track winnings/losses, and manage your balance
- **Winning Detection**: Automatic detection of winning lines with payout calculation

## How to Play

1. **Start the Game**: Run the program and make an initial deposit
2. **Choose Lines**: Select how many lines (1-3) you want to bet on
3. **Place Your Bet**: Enter your bet amount per line ($1-$100)
4. **Spin**: The slot machine will generate a random 3x3 grid
5. **Check Results**: See if you have any winning lines and collect your winnings
6. **Continue Playing**: Keep playing until you quit or run out of money

## Game Rules

### Symbols and Payouts
- **A**: Rarest symbol (2 in the pool) - 5x payout multiplier
- **B**: Rare symbol (4 in the pool) - 4x payout multiplier  
- **C**: Common symbol (6 in the pool) - 3x payout multiplier
- **D**: Most common symbol (8 in the pool) - 2x payout multiplier

### Winning Conditions
- You win when all symbols in a line (horizontal row) are the same
- Winnings = Symbol multiplier × Bet amount per line
- You can win on multiple lines simultaneously

### Betting Limits
- **Minimum bet**: $1 per line
- **Maximum bet**: $100 per line
- **Maximum lines**: 3 lines
- **Total bet**: Bet per line × Number of lines

## Installation and Setup

### Prerequisites
- Python 3.x installed on your system

### Running the Game
1. Clone this repository:
   ```bash
   git clone <your-repo-url>
   cd <repo-name>
   ```

2. Run the game:
   ```bash
   python main.py
   ```

## Example Gameplay

```
How much would you like to deposit: $50
Current balance is $50
Press enter to play (q to quit): 
Enter how many Lines (1-3): 2
What would you like to bet? $5
You are betting $5 on 2 Lines. Total bet is equal to: $10

A | B | C
A | A | D
C | B | A

You won $10
You won on 1
Current balance is $50
```

## Code Structure

- `deposit()`: Handles initial money deposit with input validation
- `num_of_lines()`: Gets user's choice of betting lines (1-3)
- `get_bet()`: Gets bet amount with validation ($1-$100)
- `get_slot_machine_spin()`: Generates random slot machine results
- `print_slot_machine()`: Displays the slot machine grid
- `check_winnings()`: Calculates winnings and identifies winning lines
- `spin()`: Main game logic for a single spin
- `main()`: Game loop and balance management

## Configuration

You can easily modify the game settings by changing these constants in `main.py`:

```python
MAX_LINES = 3      # Maximum betting lines
MAX_BET = 100      # Maximum bet per line
MIN_BET = 1        # Minimum bet per line
ROWS = 3           # Slot machine rows
COLS = 3           # Slot machine columns
```

### Symbol Configuration
Modify `symbol_count` to change symbol frequency:
```python
symbol_count = {
    "A": 2,  # 2 A's in the symbol pool
    "B": 4,  # 4 B's in the symbol pool
    "C": 6,  # 6 C's in the symbol pool
    "D": 8   # 8 D's in the symbol pool
}
```

Modify `symbol_value` to change payout multipliers:
```python
symbol_value = {
    "A": 5,  # 5x multiplier for A
    "B": 4,  # 4x multiplier for B
    "C": 3,  # 3x multiplier for C
    "D": 2   # 2x multiplier for D
}
```

## Contributing

Feel free to fork this project and submit pull requests for improvements such as:
- Adding more symbols or betting options
- Implementing bonus rounds
- Adding sound effects or better graphics
- Creating a GUI version


## Disclaimer

This is a game for entertainment purposes only. Please gamble responsibly in real life! 🎲
