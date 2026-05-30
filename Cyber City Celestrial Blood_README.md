# Buraddo HQ Adventure

A comprehensive text-based RPG adventure game featuring dungeon crawling, turn-based combat, puzzle solving, and inventory management. Navigate through a futuristic space station, battle cybernetic enemies, and uncover the mystery of Buraddo HQ.

## Features

### 🎮 **Core Gameplay**
- **Text-Based Adventure**: Rich narrative-driven exploration with detailed room descriptions
- **Turn-Based Combat**: Dice-roll combat system with equipment modifiers and strategic depth
- **50+ Interconnected Rooms**: Massive game world with logical connections and multiple pathways
- **Character Progression**: Level up through combat, gain HP, and improve your capabilities

### ⚔️ **Combat System**
- **D20 Dice Mechanics**: Roll-based attacks with success thresholds
- **Equipment Bonuses**: Weapons add damage, armor reduces incoming damage
- **Diverse Enemies**: 15 unique enemy types from training droids to cyber raptors
- **Boss Encounters**: Special enemies with unique mechanics and higher difficulty

### 🎒 **Inventory & Equipment**
- **Weight-Based Inventory**: Limited carrying capacity adds strategic resource management
- **Equipment Categories**: Weapons, armor, potions, keycards, and attachments
- **Item Enhancement**: Weapon attachments and armor sets for customization
- **Money System**: Collect gold to track progress and future expansion possibilities

### 🧩 **Puzzle Elements**
- **Terminal Hacking**: Computer interfaces with coded puzzles
- **Logic Challenges**: Mathematical sequences (Fibonacci, Pi) and wordplay
- **Environmental Puzzles**: Use game mechanics creatively to overcome obstacles
- **Multiple Solutions**: Different approaches to major challenges

### 🗝️ **Progression System**
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
- ✅ Complete room network with 50+ locations
- ✅ Full combat system with equipment integration
- ✅ Inventory management with weight constraints
- ✅ Puzzle system with multiple challenge types
- ✅ Character progression and boss encounters
- ✅ Win/lose conditions and game flow

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

**Experience the corporate nightmare of Buraddo HQ!** 🚀

*Built with Python • Powered by Imagination • Designed for Adventure*
