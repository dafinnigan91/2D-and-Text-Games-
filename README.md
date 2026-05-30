# Checkers AI Game

A fully-featured checkers game implementation with a minimax AI opponent, built using Python's Tkinter GUI framework. Features drag-and-drop gameplay, multiple capture sequences, and an intelligent AI that scales from beginner to expert difficulty.

## Features

### Core Gameplay
- **Drag & Drop Interface**: Intuitive piece movement with visual feedback
- **Standard Checkers Rules**: Full implementation of official checkers regulations
- **King Promotion**: Pieces automatically become kings when reaching the opposite end
- **Mandatory Captures**: Enforced capture rules with multiple capture sequences
- **Turn-based Play**: Human vs AI with clear turn indicators

### AI Opponent
- **Minimax Algorithm**: Advanced game tree search with alpha-beta pruning
- **Adjustable Difficulty**: 10-level skill slider (1 = Beginner, 10 = Expert)
- **Strategic Evaluation**: 
  - Piece value assessment (regular pieces vs kings)
  - Positional strategy (center control, advancement)
  - Threat detection and avoidance
  - King promotion prioritization
- **Multiple Capture Logic**: AI correctly handles mandatory capture sequences

### Game Features
- **Visual Board**: 8x8 checkerboard with proper square coloring
- **Piece Tracking**: Live capture counters with graveyard display
- **Game Reset**: Start new games without restarting application
- **Rule Reference**: Built-in rule guide for player reference
- **Win Detection**: Automatic game-over detection with victory messages

## Screenshot

*Insert screenshot of game interface here*

## Installation & Setup

### Prerequisites
- Python 3.6 or higher
- Tkinter (usually included with Python)

## How to Play

### Controls
- **Mouse**: Click and drag yellow pieces to move them
- **Valid Moves**: Only diagonal moves on dark squares are allowed
- **Captures**: Jump over opponent pieces to capture them
- **Multiple Captures**: Must continue capturing if additional captures are available

### Game Rules
1. **Movement**: Pieces move diagonally one square at a time
2. **Direction**: Regular pieces can only move forward (kings can move in any diagonal direction)
3. **Captures**: Jump diagonally over opponent pieces to capture them
4. **King Promotion**: Pieces reaching the opposite end become kings
5. **Mandatory Captures**: Must capture if a capture move is available
6. **Multiple Captures**: Must continue capturing with the same piece if possible
7. **Victory**: Win by capturing all opponent pieces or blocking all their moves

### AI Difficulty Levels
- **Levels 1-3**: Beginner (makes occasional suboptimal moves)
- **Levels 4-6**: Intermediate (balanced strategic play)
- **Levels 7-10**: Expert (deep calculation, strong positional play)

## Technical Implementation

### Architecture
```
CheckersBoard (Main Class)
├── GUI Management (Tkinter)
├── Game State Tracking
├── Move Validation
├── AI Engine
│   ├── Minimax Algorithm
│   ├── Alpha-Beta Pruning
│   ├── Position Evaluation
│   └── Move Generation
└── Event Handling
```

### Key Components

#### **Minimax AI Algorithm**
- **Search Depth**: Configurable based on difficulty slider (1-10 moves ahead)
- **Alpha-Beta Pruning**: Optimizes search by eliminating inferior branches
- **Position Evaluation**: Multi-factor scoring system considering:
  - Material advantage (captured pieces)
  - King promotion opportunities
  - Center board control
  - Forward piece advancement
  - Threat assessment

#### **Move Validation System**
- **Legal Move Checking**: Validates diagonal movement rules
- **Capture Detection**: Identifies mandatory capture opportunities
- **Multiple Capture Logic**: Handles complex capture sequences
- **Boundary Checking**: Ensures moves stay within board limits

#### **Game State Management**
- **Board Representation**: 8x8 grid with piece tracking
- **Position Mapping**: Converts between GUI coordinates and logical positions
- **Turn Management**: Alternates between human and AI turns
- **Win Condition Detection**: Monitors for game-ending scenarios

## Code Structure

### Main Files
- `checkers_fixed_complete.py`: Complete game implementation
- Core classes and methods:
  - `CheckersBoard`: Main game class
  - `ai_moving()`: AI move calculation and execution
  - `minimax()`: Minimax algorithm with alpha-beta pruning
  - `has_more_captures()`: Multiple capture detection
  - `Move_eval()`: Position evaluation function

### Key Constants
```python
Take_peice = 30      # Points for capturing a piece
King_maker = 20      # Points for king promotion
Core_dominance = 5   # Points for center control
In_danger = -10      # Penalty for vulnerable positions
```

## Development Notes

### Known Limitations
- Single-player only (human vs AI)
- No network multiplayer support
- No game save/load functionality
- Fixed board size (8x8 standard checkers)

### Performance Considerations
- AI response time scales with difficulty level
- Higher difficulties (8-10) may have 1-2 second delays
- Alpha-beta pruning significantly improves search efficiency

### Future Enhancements
- [ ] Multiplayer support (local or network)
- [ ] Game replay system
- [ ] Opening book for stronger AI play
- [ ] Tournament mode with multiple AI opponents
- [ ] Advanced position analysis tools
- [ ] Custom board themes

## Contributing

Contributions are welcome! Areas for improvement:
- AI algorithm enhancements
- UI/UX improvements
- Performance optimizations
- Additional game modes
- Code refactoring and cleanup

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Minimax algorithm implementation based on classic game theory principles
- Checkers rules following official World Checkers Federation guidelines
- Tkinter GUI framework for cross-platform compatibility

---

**Enjoy playing checkers against an AI that learns from every game!** 🎯

*Built with Python • Powered by Minimax AI • Designed for Fun*
