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

**Enjoy playing checkers against an AI that learns from every game!** 

*Built with Python • Powered by Minimax AI • Designed for Fun*


# Cyber City Celestial Blood 

A comprehensive text-based RPG adventure game featuring dungeon crawling, turn-based combat, puzzle solving, and inventory management. Navigate through a futuristic space station, battle cybernetic enemies, and uncover the mystery of Buraddo HQ.

## Features

### **Core Gameplay**
- **Text-Based Adventure**: Rich narrative-driven exploration with detailed room descriptions
- **Turn-Based Combat**: Dice-roll combat system with equipment modifiers and strategic depth
- **50+ Interconnected Rooms**: Massive game world with logical connections and multiple pathways
- **Character Progression**: Level up through combat, gain HP, and improve your capabilities

### **Combat System**
- **D20 Dice Mechanics**: Roll-based attacks with success thresholds
- **Equipment Bonuses**: Weapons add damage, armor reduces incoming damage
- **Diverse Enemies**: 15 unique enemy types from training droids to cyber raptors
- **Boss Encounters**: Special enemies with unique mechanics and higher difficulty

### **Inventory & Equipment**
- **Weight-Based Inventory**: Limited carrying capacity adds strategic resource management
- **Equipment Categories**: Weapons, armor, potions, keycards, and attachments
- **Item Enhancement**: Weapon attachments and armor sets for customization
- **Money System**: Collect gold to track progress and future expansion possibilities

### **Puzzle Elements**
- **Terminal Hacking**: Computer interfaces with coded puzzles
- **Logic Challenges**: Mathematical sequences (Fibonacci, Pi) and wordplay
- **Environmental Puzzles**: Use game mechanics creatively to overcome obstacles
- **Multiple Solutions**: Different approaches to major challenges

### **Progression System**
- **Keycard Progression**: Find keycards to unlock new areas
- **Equipment Upgrades**: Discover better weapons and armor throughout the station
- **Health Management**: Potions for healing, boosting, and strategic resource planning

## Game World

### Setting
You are **Akiino**, infiltrating the mysterious **Buraddo HQ** space station. Navigate through corporate offices, biological labs, weapons facilities, and synthetic research areas while uncovering a dark conspiracy.

### Key Locations
- **Reception & Security**: Starting areas with basic enemies and equipment
- **Executive Offices**: High-security areas requiring keycards and strategy
- **Biological Labs**: Dangerous cyber-raptor encounters and valuable equipment
- **Weapons Labs**: Military-grade equipment and advanced security systems
- **Observation Deck**: Final confrontation location with environmental mechanics

### Enemy Types
- **Training & Sentinel Droids**: Basic mechanical enemies (HP: 20-50)
- **Cyber Raptors**: Fast biological-synthetic hybrids (HP: 25-50)
- **Defense Turrets**: High-damage stationary units (HP: 75)
- **Cyber-Toothed Tiger**: Elite biological weapon (HP: 100)
- **Battle Mech**: Heavy assault unit (HP: 150)
- **Dakik Yamamoto**: Final boss with special mechanics (HP: ∞)

## Installation & Setup

### Prerequisites
- Python 3.6 or higher
- No additional dependencies required

### Running the Game
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/david-game-portfolio.git
   cd david-game-portfolio/buraddo-hq-adventure
   ```

2. Run the game:
   ```bash
   python buraddo_hq_game.py
   ```

## How to Play

### Commands
```
MOVEMENT:
  move to <room name>     — travel to adjacent rooms
  
EXPLORATION:
  search room             — find items and secrets
  describe room           — re-read room description
  
INVENTORY:
  pick up <item name>     — collect items (money adds to gold)
  put down <item name>    — drop items from backpack
  show backpack           — view inventory contents
  
EQUIPMENT:
  equip <item name>       — equip weapons/armor from backpack
  unequip <item name>     — return equipped items to backpack
  show equipped           — view currently equipped gear
  
ITEMS:
  use <item name>         — consume potions for healing/buffs
  use keycard <card name> — unlock doors and restricted areas
  
COMBAT:
  engage enemy            — initiate combat with room enemies
  
INTERACTION:
  use terminal            — access computer interfaces for puzzles
  
INFORMATION:
  show hp                 — display health status
  help                    — show command list
  quit                    — exit game
```

### Combat Actions
During combat encounters:
- **attack** — Roll d20 + strength + weapon bonuses vs enemy
- **use <potion>** — Heal or boost stats (consumes turn)
- **dash** — Skip enemy's attack this turn
- **flee** — Escape combat (keeps you alive)

### Game Progression Tips
1. **Start with Reception**: Learn combat basics against Training Bobby
2. **Collect Equipment**: Search every room for weapons, armor, and items
3. **Manage Weight**: Balance useful items vs carrying capacity
4. **Find Keycards**: Essential for accessing restricted high-value areas
5. **Use Terminals**: Solve puzzles for major advantages
6. **Combat Strategy**: Equip armor before tough fights, stock healing potions

## Technical Implementation

### Architecture
```
Game Engine
├── Room System (50+ interconnected locations)
├── Combat Engine (d20-based with modifiers)
├── Inventory Management (weight-based constraints)
├── Item System (weapons, armor, consumables, keys)
├── Puzzle Framework (terminal interfaces)
└── Story Progression (boss encounters, win conditions)
```

### Core Classes
- **`Protagonist`**: Player character with stats, inventory, and progression
- **`Room`**: Game locations with descriptions, connections, and contents  
- **`Boss`**: Enemy entities with combat stats and behaviors
- **`Item` Hierarchy**: Weapons, Armor, Potions, KeyCards, Attachments
- **`Computer`**: Terminal interfaces for puzzle interactions
- **`Backpack`**: Weight-based inventory management system

### Key Game Systems

#### **Combat Mechanics**
```python
def Protag_strike(self, enemy):
    roll = Dice()  # 1d20
    weapon_bonus = sum(equipped_weapon_damage)
    if roll > 5:
        damage = roll + strength + weapon_bonus
        enemy.hp -= damage
```

#### **Equipment System**
- **Weapons**: Damage modifiers and attachment slots
- **Armor**: Damage reduction against incoming attacks  
- **Potions**: Healing, max HP boosts, temporary buffs
- **KeyCards**: Access control for locked areas

#### **Puzzle Framework**
- **Mathematical Sequences**: Fibonacci and Pi-based codes
- **Environmental Interaction**: Sunlight mechanics for final boss
- **Logic Challenges**: Pattern recognition and wordplay

### Data Structures
- **Room Graph**: Bidirectional connections modeling building layout
- **Item Database**: Categorized equipment with balanced stats
- **Enemy Progression**: Scaled difficulty across different areas

## Game Design Philosophy

### Exploration Focus
The game rewards thorough exploration with hidden items, optional areas, and multiple pathways through the station. Players can choose different routes based on their equipment and risk tolerance.

### Strategic Combat
Combat emphasizes preparation and resource management over reflexes. Players must balance equipment weight, potion usage, and tactical positioning.

### Narrative Integration
Environmental storytelling through room descriptions and enemy placement creates an immersive corporate dystopia without heavy exposition.

### Player Agency
Multiple solutions to challenges (combat vs stealth vs puzzle-solving) allow different playstyles and replay value.

## Development Notes

### Completed Features
- Complete room network with 50+ locations
- Full combat system with equipment integration
- Inventory management with weight constraints
- Puzzle system with multiple challenge types
- Character progression and boss encounters
- Win/lose conditions and game flow

### Code Quality
- **Object-Oriented Design**: Clean class hierarchies and encapsulation
- **Modular Architecture**: Separate systems for combat, inventory, movement
- **Error Handling**: Robust input validation and edge case management
- **Scalable Framework**: Easy to add new rooms, items, or enemies

### Performance Considerations
- Efficient room/item lookups using Python data structures
- Minimal memory overhead with object reuse
- Fast command parsing with string manipulation
- Stateless combat system for consistent behavior

## Future Enhancements

### Gameplay Additions
- [ ] Save/load game functionality
- [ ] Multiple character classes with different abilities
- [ ] Expanded crafting system for equipment enhancement
- [ ] Random events and environmental hazards
- [ ] Multiple endings based on player choices

### Technical Improvements
- [ ] Configuration file for easy game balancing
- [ ] Automated testing suite for game mechanics
- [ ] Performance profiling and optimization
- [ ] Modding API for community content

### Quality of Life
- [ ] Command aliases and auto-completion
- [ ] Detailed help system with examples
- [ ] Game statistics and achievement tracking
- [ ] Colorized output for better readability

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by classic text adventures like Zork and Adventure
- Game balance influenced by tabletop RPG mechanics
- Object-oriented design patterns from modern game development

---

**Experience the corporate nightmare of Buraddo HQ!**

*Built with Python • Powered by Imagination • Designed for Adventure*

