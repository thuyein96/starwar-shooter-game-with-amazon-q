# Star Wars: Rebel Defense

![Game Screenshot](https://via.placeholder.com/800x600.png?text=Star+Wars:+Rebel+Defense)

A retro-style 2D space shooter game inspired by Star Wars, built with Python and Pygame. Take control of an X-Wing fighter and defend the Rebellion against waves of Imperial TIE Fighters!

## Features

- **Star Wars Theme**: Control an X-Wing fighter against various TIE Fighter enemies
- **Parallax Scrolling**: Multi-layered star field background creates depth and immersion
- **Power-up System**: Collect power-ups for rapid fire, shields, and double lasers
- **Enemy Variety**: Face different types of TIE Fighters with unique behaviors:
  - TIE Fighters: Basic enemies with straight movement
  - TIE Interceptors: Fast enemies with swooping patterns
  - TIE Bombers: Tough enemies with zigzag movement
- **Visual Effects**: Explosion animations, shield effects, and laser beams
- **Progressive Difficulty**: Game gets harder as your score increases

## How to Play

### Requirements
- Python 3.x
- Pygame library

### Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/star-wars-rebel-defense.git
cd star-wars-rebel-defense
```

2. Install Pygame if you don't have it:
```bash
pip install pygame
```

3. Run the game:
```bash
python star_wars_shooter.py
```

### Controls

- **Left/Right Arrow Keys**: Move your X-Wing fighter
- **Space Bar**: Fire lasers
- **Escape**: Quit game
- **R**: Restart after Game Over

## Gameplay Tips

- Collect shield power-ups (blue) when your health is low
- Use rapid fire (cyan) and double laser (yellow) power-ups to clear the screen
- Focus on destroying TIE Bombers first as they're the toughest enemies
- Keep moving to avoid enemy lasers

## Game Elements

### Your Ship
- **X-Wing Fighter**: Your ship with a health bar displayed below it

### Enemies
- **TIE Fighter**: Basic enemy (10 points)
- **TIE Interceptor**: Fast enemy (15 points)
- **TIE Bomber**: Tough enemy (20 points)

### Power-ups
- **Rapid Fire**: Increases your firing rate
- **Shield**: Provides temporary protection
- **Double Laser**: Shoots two lasers at once

## Development

This game was created as a learning project to explore:
- Object-oriented programming with Python
- Game development with Pygame
- Procedural graphics generation
- Game design principles including balancing and progression

All graphics are generated programmatically using Pygame's drawing functions, making the game lightweight and easy to modify.

## Future Enhancements

- Add sound effects and background music
- Implement boss battles
- Add more power-up types
- Create level designs with specific enemy patterns
- Add high score system

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This is a fan-made game and is not affiliated with Disney or Lucasfilm. Star Wars is a registered trademark of Lucasfilm Ltd.

---

May the Force be with you!
