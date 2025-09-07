# CloudBlast RPG Game

A captivating 2D platform RPG built with **pygame**, offering a full-fledged gaming experience with combat, magic, intelligent enemies, particle effects, and everything you'd expect from a classic vintage RPG.

## 📋 Project Description

CloudBlast is a two-dimensional role-playing game that combines platforming elements with traditional RPG mechanics. The player explores a world filled with enemies, gains experience, upgrades stats, and uses various weapons and spells to progress through the game.

### ✨ Key Features

- **Combat System**: 5 different weapons (sword, spear, axe, rapier, sai) with unique stats  
- **Magic System**: Fire and healing spells  
- **Diverse Enemies**: 4 enemy types (squid, raccoon, spirit, bamboo) with distinct AI behaviors  
- **Progression System**: Earn experience and upgrade character stats  
- **Particle Effects**: Smooth animations and appealing visual effects  
- **Immersive Audio**: Background music and sound effects  
- **Detailed Map**: Tilemap-based world with multiple depth layers  

## 🔧 System Requirements

### Software Prerequisites  
- **Python 3.7+** (tested with Python 3.12.3)  
- **pygame** 2.0+  
- Operating System: Windows, macOS, or Linux  

### Minimum Hardware Requirements  
- RAM: 512 MB  
- Disk Space: 50 MB  
- Graphics Card: Compatible with DirectX 9.0c or OpenGL 2.1  

## 🚀 Installation and Setup

### Option 1: Precompiled Executable (Windows)  
The `main.exe` executable is available in the `code/` folder:  
```bash
cd code/
./main.exe  # On Linux/macOS
# main.exe  # On Windows
```

### Option 2: Run from Source Code

1. **Clone the repository**:  
```bash
git clone https://github.com/GiorCocc/RPG-GAME.git
cd RPG-GAME
```

2. **Install dependencies**:  
```bash
pip install -r requirements.txt
# Or manually:
# pip install pygame
```

3. **Launch the game**:  
```bash
cd code/
python main.py
```

### Development Environment Setup

For developers who want to modify the game:  
```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install pygame
pip install pygame

# To create a new executable (optional)
pip install pyinstaller
pyinstaller --onefile main.py
```

## 🎮 Game Controls

| Command               | Key                      | Description                                                  |
| ---------------------| -------------------------| -------------------------------------------------------------|
| Move Up              | `Arrow Up`               | Moves the character upward                                   |
| Move Down            | `Arrow Down`             | Moves the character downward                                 |
| Move Right           | `Arrow Right`            | Moves the character to the right                             |
| Move Left            | `Arrow Left`             | Moves the character to the left                              |
| Attack               | `Space`                  | Attacks enemies or bushes with the selected weapon           |
| Cast Magic           | `Left CTRL`              | Casts a spell with the selected magic                        |
| Switch Weapon        | `Q`                      | Cycles through: sword, spear, axe, rapier, sai               |
| Switch Magic         | `E`                      | Toggles between: fire and healing                            |
| Upgrade Menu         | `M`                      | Opens the upgrade menu to spend XP points                   |
| Menu Navigation      | `Arrow Left/Right`       | Navigates through menu options                               |
| Confirm Selection    | `Space`                  | Confirms selection in the upgrade menu                       |

## 📁 Project Structure

```
RPG-GAME/
├── code/                    # Main source code
│   ├── main.py             # Main game file
│   ├── player.py           # Player logic
│   ├── enemy.py            # Enemy system
│   ├── level.py            # Level management
│   ├── weapon.py           # Weapon system
│   ├── magic.py            # Magic system
│   ├── ui.py               # User interface
│   ├── settings.py         # Game settings
│   ├── particles.py        # Particle effects
│   ├── upgrade.py          # Upgrade system
│   ├── support.py          # Support functions
│   ├── entity.py           # Base entity class
│   ├── tile.py             # Tilemap system
│   ├── debug.py            # Debug tools
│   └── main.exe            # Windows executable
├── graphics/               # Graphic assets
│   ├── player/             # Player sprites
│   ├── monsters/           # Enemy sprites
│   ├── weapons/            # Weapon sprites
│   ├── particles/          # Visual effects
│   ├── objects/            # World objects
│   ├── tilemap/            # Map tiles
│   └── font/               # Custom fonts
├── audio/                  # Audio files
│   ├── main.ogg            # Background music
│   ├── attack/             # Attack sounds
│   └── *.wav               # Various sound effects
├── map/                    # Map data
│   └── *.csv               # CSV files for levels
└── README.md               # This file
```

## 🎯 Gameplay Elements

### Available Weapons  
- **Sword**: Balanced, medium damage, medium speed  
- **Spear**: High damage, slow speed  
- **Axe**: Heavy damage, moderate speed  
- **Rapier**: Low damage, very high speed  
- **Sai**: Moderate damage, high speed  

### Magic System  
- **Flame**: Offensive spell dealing fire damage  
- **Healing**: Restores player's health points  

### Enemies  
- **Squid**: Aquatic enemy with slash attack  
- **Raccoon**: Tough enemy with claw attack  
- **Spirit**: Fast enemy with lightning attack  
- **Bamboo**: Agile enemy with leaf attack  

## 🛠️ Future Development

- New worlds and levels  
- Additional gameplay mechanics  
- Expanded inventory system  
- Local multiplayer  
- New enemy types and bosses  
- Quest and mission system  

## 🎨 Credits and Assets

Graphics kindly provided by:  
- **[Ninja Adventure - Asset Pack by pixel-boy](https://pixel-boy.itch.io/ninja-adventure-asset-pack)** – Available for free download  

All graphic assets are used under a free-to-use license for personal and open-source projects.

## 📄 License

This project is distributed under an open-source license. Rights to graphic assets belong to their respective authors (see Credits section).

**Note**: Ninja Adventure assets are used according to their free-to-use license terms. For commercial use, refer to the original license.

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the project  
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)  
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)  
4. Push to the branch (`git push origin feature/AmazingFeature`)  
5. Open a Pull Request  

## 📞 Contact

For questions, suggestions, or bug reports, open an issue on GitHub.

---

**Have fun with CloudBlast! 🎮**
