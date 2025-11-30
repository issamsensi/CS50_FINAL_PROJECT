# 🎮 UNLIMITE SHOOTER - CS50 Final Project

> **A comprehensive full-stack project featuring a 2D shooter game and promotional website**

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Pygame](https://img.shields.io/badge/Pygame-2.0+-green.svg)](https://www.pygame.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-red.svg)](https://flask.palletsprojects.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple.svg)](https://getbootstrap.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📖 Project Overview

**UNLIMITE SHOOTER** is a complete CS50 final project consisting of two main components:

1. **🎮 Game Component**: An action-packed 2D top-down shooter built with Python and Pygame
2. **🌐 Website Component**: A professional promotional website built with Flask, featuring game information, developer portfolio, and contact functionality

This project demonstrates proficiency across multiple technologies including Python, Pygame, Flask, HTML, CSS, JavaScript, Bootstrap, SQL, and modern web development practices.

## 🌐 Demo

### 🌐 [Website Live Demo](https://issamsensi.pythonanywhere.com/)

### 🎥 Demo Video

[![Watch the video](https://img.youtube.com/vi/9skhrPodQiQ/0.jpg)](https://www.youtube.com/watch?v=9skhrPodQiQ)



---

## 🎯 Project Components

### 🎮 Game: UNLIMITE SHOOTER

An intense top-down shooter where players battle endless waves of enemies, collect resources, and upgrade their abilities.

#### Game Features

**Core Gameplay**
- ✅ **Smooth Movement**: 8-directional movement with WASD or arrow keys
- ✅ **Directional Shooting**: Spacebar-based shooting that follows player direction
- ✅ **Wave-Based Combat**: Progressive difficulty with increasing enemy spawn rates
- ✅ **Enemy AI**: Intelligent pathfinding that tracks and pursues the player

**Combat System**
- ✅ **Three Bullet Types**:
  - **Normal**: Standard single-shot bullets
  - **Multi-Shot**: Fire three bullets in a spread pattern (3 crystals)
  - **Laser**: High-damage, fast-moving projectiles (5 crystals)
- ✅ **Three Enemy Types**:
  - **Normal Enemies**: Balanced speed and health (2 HP, 2 speed)
  - **Fast Enemies**: Quick but fragile (1 HP, 3 speed)
  - **Tank Enemies**: Slow but heavily armored (5 HP, 1 speed)
- ✅ **Health System**: Visual health bars for both player and enemies

**Progression & Economy**
- ✅ **Shop System**: Access via door at top of map
  - Increase Max HP (+100 HP for 50 gold)
  - Boost Speed (+1 speed for 30 gold)
  - Enhance Damage (+1 damage for 40 gold)
  - Improve Fire Rate (35 gold)
  - Unlock Multi-Shot (3 crystals)
  - Unlock Laser Bullets (5 crystals)
- ✅ **Collectibles**:
  - **Gold Coins**: 50% drop rate from enemies
  - **Crystals**: 5% drop rate from enemies (rare)
- ✅ **Wave Progression**: Difficulty increases every 10 kills

**Visual & Polish**
- ✅ **Custom Backgrounds**: Unique map and shop environments
- ✅ **Particle Effects**: Explosion effects on enemy death and item collection
- ✅ **HUD Display**: Real-time health bar, kills, wave, gold, and crystal counters
- ✅ **Game Over Screen**: Final statistics with restart option

---

### 🌐 Website: Promotional Platform

A modern, responsive website built with Flask to showcase the game and developer.

#### Website Features

**Pages & Routes**
- ✅ **Home (`/`)**: Landing page with game overview, download button, and highlights
- ✅ **About (`/about`)**: Detailed game information with screenshots
- ✅ **Developer (`/developer`)**: Developer portfolio with skills, hobbies, and artwork carousel
- ✅ **Contact (`/contact`)**: Contact form with social media links and mailto integration
- ✅ **Newsletter (`/newsletter`)**: Email subscription system with SQLite database

**Frontend Features**
- ✅ **Responsive Design**: Mobile-friendly layout with media queries
- ✅ **Modern UI**: Dark theme with custom color palette
- ✅ **Bootstrap 5 Integration**: Professional components and forms
- ✅ **Font Awesome Icons**: Social media icons and visual elements
- ✅ **Image Gallery**: Game screenshots and developer artwork carousel
- ✅ **Flash Messages**: User feedback for form submissions

**Backend Features**
- ✅ **Flask Framework**: Python-based web server
- ✅ **Jinja2 Templates**: Template inheritance and dynamic content
- ✅ **SQLite Database**: Newsletter email storage with duplicate prevention
- ✅ **CS50 SQL Library**: Database operations
- ✅ **Form Handling**: POST request processing with validation
- ✅ **Session Management**: Flash message system

**Design System**
- ✅ **Custom CSS Variables**: Consistent color theming
  - Primary: `#2B2F33`
  - Secondary: `#4B8B3B` (green accent)
  - Accent: `#D98C3D` (orange)
  - Background: `#0F1112` (dark)
- ✅ **Smooth Animations**: Hover effects and transitions
- ✅ **Drop Shadows**: Glowing effects on images
- ✅ **Sticky Header**: Fixed navigation bar

---

## 🛠️ Technology Stack

### Game Technologies

| Technology | Purpose |
|------------|---------|
| **Python 3.7+** | Core programming language |
| **Pygame 2.0+** | Game development framework |
| **Math Module** | Trigonometry for bullet trajectories |
| **Random Module** | Enemy spawning and drop rates |
| **Sys Module** | System operations and exit handling |
| **PyInstaller** | Executable compilation |

### Website Technologies

#### Backend
| Technology | Purpose |
|------------|---------|
| **Flask** | Web framework and routing |
| **Jinja2** | Template engine (included with Flask) |
| **CS50 Library** | SQL database operations |
| **SQLite** | Database for newsletter storage |
| **urllib.parse** | URL encoding for mailto links |

#### Frontend
| Technology | Purpose |
|------------|---------|
| **HTML5** | Page structure and semantics |
| **CSS3** | Custom styling and animations |
| **JavaScript** | Client-side interactivity (Bootstrap) |
| **Bootstrap 5.3** | UI components and responsive grid |
| **Font Awesome 6.4** | Icon library for social media |

#### Design & Assets
| Technology | Purpose |
|------------|---------|
| **Custom CSS Variables** | Theming and color consistency |
| **Google Fonts (Inter)** | Modern typography |
| **Media Queries** | Responsive breakpoints |
| **Flexbox** | Layout and alignment |

---

## 🚀 Installation & Setup

### Prerequisites

- **Python 3.7 or higher** ([Download](https://www.python.org/downloads/))
- **pip** (Python package manager)
- **Git** (optional, for cloning)

### Installation Steps

1. **Clone or download the repository**
   ```bash
   git clone https://github.com/issamsensi/CS50_FINAL_PROJECT.git
   cd CS50_FINAL_PROJECT
   ```

2. **Install required Python libraries**
   ```bash
   pip install pygame flask cs50
   ```
   
   Or if you have multiple Python versions:
   ```bash
   pip3 install pygame flask cs50
   ```

3. **Verify installation**
   ```bash
   python -c "import pygame, flask, cs50; print('All libraries installed!')"
   ```

---

## 🎮 Running the Game

### Method 1: Run from Source

Navigate to the project directory and run:

```bash
python GAME/main.py
```

Or:

```bash
python3 GAME/main.py
```

### Method 2: Run the Executable

If you have the pre-built executable:

**Windows:**
1. Navigate to `GAME/dist/`
2. Double-click `main.exe`

**Linux:**
```bash
cd GAME/dist/
chmod +x main  # First time only
./main
```

### Building Your Own Executable

```bash
# Install PyInstaller
pip install pyinstaller

# Navigate to GAME directory
cd GAME

# Build executable
pyinstaller --onefile --add-data "assets:assets" main.py

# The executable will be in GAME/dist/
```

---

## 🌐 Running the Website

### Development Server

1. **Navigate to the WEBSITE directory**
   ```bash
   cd WEBSITE
   ```

2. **Run the Flask application**
   ```bash
   python app.py
   ```
   
   Or:
   ```bash
   flask run
   ```

3. **Access the website**
   - Open your browser and go to: `http://127.0.0.1:5000`
   - Or: `http://localhost:5000`

### Production Deployment

For production deployment, consider using:
- **Gunicorn** (WSGI server)
- **Nginx** (reverse proxy)
- **Heroku**, **PythonAnywhere**, or **AWS**

Example with Gunicorn:
```bash
pip install gunicorn
gunicorn -w 4 app:app
```

---

## 🎯 Game Controls

| Action | Keys |
|--------|------|
| **Move Up** | `W` or `↑` |
| **Move Down** | `S` or `↓` |
| **Move Left** | `A` or `←` |
| **Move Right** | `D` or `→` |
| **Shoot** | `SPACE` |
| **Enter Shop** | Walk to the brown door at top-center of map |
| **Exit Shop** | `B` |
| **Purchase Upgrades** | `1-6` (number keys in shop) |
| **Restart Game** | `R` (on Game Over screen) |
| **Quit Game** | `Q` (on Game Over screen) or close window |

---

## 📁 Project Structure

```
CS50_FINAL_PROJECT/
│
├── GAME/                         # Game component
│   ├── assets/                   # Game assets
│   │   ├── coin.png              # Coin collectible sprite
│   │   ├── map.jpg               # Main game background
│   │   └── store.jpg             # Shop background
│   │
│   ├── build/                    # PyInstaller build files
│   ├── dist/                     # Compiled executable
│   │   └── main                  # Standalone game executable
│   │
│   ├── main.py                   # Main game source code (609 lines)
│   └── main.spec                 # PyInstaller specification
│
├── WEBSITE/                      # Website component
│   ├── static/                   # Static assets
│   │   ├── images/               # Image files
│   │   │   ├── drawings/         # Developer artwork (7 images)
│   │   │   ├── game.png          # Gameplay screenshot
│   │   │   ├── gameover.png      # Game over screenshot
│   │   │   ├── shop.png          # Shop screenshot
│   │   │   ├── img.png           # Game preview image
│   │   │   ├── pixel_sensi.png   # Developer avatar
│   │   │   └── map.jpg           # Background image
│   │   │
│   │   ├── styles.css            # Main stylesheet (234 lines)
│   │   ├── developer.css         # Developer page styles
│   │   ├── script.js             # JavaScript functionality
│   │   └── main                  # Game executable download
│   │
│   ├── templates/                # Jinja2 templates
│   │   ├── layout.html           # Base template with header/footer
│   │   ├── index.html            # Home page
│   │   ├── about.html            # About page
│   │   ├── developer.html        # Developer portfolio
│   │   └── contact.html          # Contact form
│   │
│   ├── app.py                    # Flask application (69 lines)
│   └── sensidb.db                # SQLite database
│
└── README.md                     # This file
```

### Key Files Explained

**Game Component:**
- **`main.py`**: Contains all game logic including Player, Enemy, Bullet, Collectible, and Particle classes
- **`assets/`**: Image resources for backgrounds and sprites

**Website Component:**
- **`app.py`**: Flask routes and application logic
- **`templates/layout.html`**: Base template with navigation and footer
- **`static/styles.css`**: Custom CSS with dark theme and responsive design
- **`sensidb.db`**: SQLite database storing newsletter subscriptions

---

## 🎨 Game Mechanics Deep Dive

### Enemy Spawning System
- Enemies spawn from random edges (left, right, top, bottom)
- Spawn rate increases as waves progress
- Enemy types unlock based on kill count:
  - 0-19 kills: Normal enemies only
  - 20-49 kills: Normal and Fast enemies
  - 50+ kills: All three enemy types

### Bullet Physics
- Bullets use trigonometry for directional movement
- Angle calculated based on player direction (0°, 90°, 180°, 270°)
- Multi-shot spreads bullets at -20°, 0°, +20° offsets
- Laser bullets travel 1.5x faster and deal 2x damage

### Particle System
- 15 particles spawn on enemy death or item collection
- Random velocity vectors for natural explosion effect
- Particles fade over 30 frames
- Color matches source (enemy color, yellow for coins, blue for crystals)

---

## 🌐 Website Features Deep Dive

### Database Schema

**Newsletter Table:**
```sql
CREATE TABLE newsletter (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL UNIQUE
);
```

### Contact Form Flow
1. User fills out contact form (name, email, message)
2. Flask validates all fields are present
3. Data is URL-encoded for mailto link
4. User's email client opens with pre-filled message
5. Recipient: `astkun010@gmail.com`

### Social Media Integration
- Facebook: `/issamsensi`
- Instagram: `@issamsensi`
- TikTok: `@issamsensi`
- LinkedIn: Issam Amghar
- GitHub: `/issamsensi`
- WhatsApp: +212658987985
- YouTube: `@issamsensi`
- Twitter/X: `@issamsensi`

---

## 🔮 Future Improvements

### Game Enhancements
- 🎵 **Audio System**: Background music and sound effects (shooting, explosions, pickups)
- 🗺️ **Multiple Maps**: Different environments with unique layouts and obstacles
- 🏆 **Boss Battles**: Epic boss fights every 10 waves
- 💪 **Power-ups**: Temporary buffs (invincibility, rapid fire, shields)
- 🎯 **Achievement System**: Unlock achievements for milestones
- 💾 **Save System**: Persistent high scores and progress
- 🎮 **Gamepad Support**: Controller compatibility
- 🌐 **Online Leaderboards**: Global score comparison

### Website Enhancements
- 📊 **Analytics Dashboard**: Track downloads and user engagement
- 🎥 **Video Trailer**: Embedded gameplay video
- 💬 **Comment System**: User feedback and reviews
- 🌍 **Internationalization**: Multi-language support
- 📱 **Progressive Web App**: Offline functionality
- 🔐 **User Accounts**: Login system for personalized experience
- 📧 **Email Automation**: Automated newsletter sending
- 🎨 **Theme Switcher**: Light/dark mode toggle

### Technical Improvements
- ⚡ **Performance Optimization**: Sprite batching and object pooling
- 🧪 **Unit Tests**: Automated testing for both components
- 📝 **Code Documentation**: Comprehensive docstrings
- 🐳 **Docker Containerization**: Easy deployment
- 🔄 **CI/CD Pipeline**: Automated testing and deployment
- 📊 **Logging System**: Error tracking and debugging

---

## 🙏 Credits & Acknowledgements

### Education
- **[CS50: Introduction to Computer Science](https://cs50.harvard.edu/)** - Harvard University
- **David J. Malan** - CS50 instructor and inspiration
- **CS50 Community** - Support and feedback

### Technologies & Libraries
- **[Python](https://www.python.org/)** - Programming language
- **[Pygame](https://www.pygame.org/)** - Game development library
- **[Flask](https://flask.palletsprojects.com/)** - Web framework
- **[Bootstrap](https://getbootstrap.com/)** - CSS framework
- **[Font Awesome](https://fontawesome.com/)** - Icon library
- **[CS50 Library](https://cs50.readthedocs.io/)** - SQL wrapper
- **[PyInstaller](https://www.pyinstaller.org/)** - Executable packaging

### Assets & Resources
- Background images sourced from free stock image websites
- Coin sprite created using custom pixel art
- Developer artwork created by Issam Sensi

### Developer
- **Issam Amghar (Issam Sensi)** - Project creator and developer
- Morocco 🇲🇦
- BTS DSI Graduate (Développement des Systèmes d'Information)

---

## 📄 License

This project is licensed under the **MIT License**:

```
MIT License

Copyright (c) 2025 Issam Amghar (Issam Sensi)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 🎓 About This CS50 Final Project

This project was created as the final project for **Harvard's CS50: Introduction to Computer Science** course. It demonstrates comprehensive understanding of:

### Programming Concepts
- ✅ Object-oriented programming with Python classes
- ✅ Game loop and state management
- ✅ Collision detection algorithms
- ✅ Event handling and user input
- ✅ Database operations and SQL
- ✅ Web development with Flask
- ✅ Template rendering with Jinja2
- ✅ RESTful routing and HTTP methods
- ✅ Form validation and data processing
- ✅ Responsive web design

### Technologies Demonstrated
- ✅ Python (game logic and web backend)
- ✅ Pygame (game development)
- ✅ Flask (web framework)
- ✅ HTML5 (markup and structure)
- ✅ CSS3 (styling and animations)
- ✅ JavaScript (via Bootstrap)
- ✅ SQL (database operations)
- ✅ Bootstrap (responsive design)
- ✅ Git (version control)

### Software Engineering Practices
- ✅ Code organization and modularity
- ✅ Resource management and optimization
- ✅ User experience design
- ✅ Error handling and validation
- ✅ Documentation and comments
- ✅ Project structure and architecture

---

## 🐛 Known Issues

### Game
- Enemies may occasionally overlap when spawning from edges
- Performance may degrade with 50+ simultaneous enemies on screen
- Shop door hitbox could be more forgiving for easier entry

### Website
- Contact form uses mailto (requires email client)
- Newsletter database has no admin panel for viewing subscribers
- No email validation beyond HTML5 input type

**Contributions and bug reports are welcome!** Feel free to open an issue or submit a pull request.

---

## 📞 Contact

**Developer**: Issam Amghar (Issam Sensi)  
**Email**: astkun010@gmail.com  
**GitHub**: [@issamsensi](https://github.com/issamsensi)  
**LinkedIn**: [Issam Amghar](https://www.linkedin.com/in/issam-amghar)  
**Location**: Morocco 🇲🇿

### Social Media
- 📘 Facebook: [/issamsensi](https://facebook.com/issamsensi)
- 📸 Instagram: [@issamsensi](https://instagram.com/issamsensi)
- 🎵 TikTok: [@issamsensi](https://www.tiktok.com/@issamsensi)
- 📺 YouTube: [@issamsensi](https://youtube.com/@issamsensi)
- 🐦 Twitter/X: [@issamsensi](https://x.com/issamsensi)
- 💬 WhatsApp: [+212658987985](https://wa.me/+212658987985)

---

## 📊 Project Statistics

- **Total Lines of Code**: ~900+ lines
  - Game: 609 lines (Python)
  - Website Backend: 69 lines (Python/Flask)
  - Website Frontend: 234+ lines (CSS) + HTML templates
- **Development Time**: CS50 Final Project
- **Technologies Used**: 10+ (Python, Pygame, Flask, HTML, CSS, JS, Bootstrap, SQL, etc.)
- **Pages**: 5 (Home, About, Developer, Contact, Newsletter)
- **Game Classes**: 6 (Game, Player, Enemy, Bullet, Collectible, Particle)
- **Database Tables**: 1 (Newsletter)

---

<div align="center">

## ⭐ Star This Project!

If you found this project interesting or useful, please consider giving it a star on GitHub!

**Made with ❤️ for CS50 by Issam Sensi**

*This was CS50!* 🎓

</div>
