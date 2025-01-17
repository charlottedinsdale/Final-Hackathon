Bonk It 🎮
Live Site | Repository
📖 Introduction
Bonk It is a fun, easy-to-play game testing your reflexes and thinking by challenging you to press on instructed colors. Perfect for quick gaming sessions and brain training!
Show Image
🎯 Target Audience
The game is designed for anyone who wants to enjoy a simple yet engaging game. Players seeking an extra challenge can try the advanced mode, which tests both reflexes and cognitive processing.
The advanced version implements the Stroop Effect - a psychological phenomenon where the brain experiences conflict between processing the meaning of a word and the color in which it's written. For example, if the word "Red" appears in blue ink and you need to press the button corresponding to the color (blue), your brain must resolve the conflict between the word's meaning and its visual color.
⭐ Features
Game Modes

Easy Mode: Basic color matching gameplay
Hard Mode: Increased difficulty with faster timing
Heck Mode: Advanced gameplay incorporating the Stroop Effect

Core Features

User authentication (register, login, logout)
Customizable user profiles
Global leaderboards
Personal statistics tracking
Multiple difficulty levels
Colorblind mode support
Audio feedback and game music
Progressive difficulty scaling
Visual time indicator

💫 Technologies Used
Languages

HTML5
CSS3
JavaScript
Python 3

Frameworks & Libraries

Django
Bootstrap
jQuery

Database

PostgreSQL

Tools

Git
GitHub
Heroku
Miro (Wireframes)
Cloudinary

🚀 Getting Started
Prerequisites

Python 3.x
pip
PostgreSQL
Git

Installation

Clone the repository

bashCopygit clone https://github.com/yourusername/bonk-it.git

Create a virtual environment

bashCopypython -m venv venv

Activate virtual environment

bashCopy# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

Install dependencies

bashCopypip install -r requirements.txt

Create .env file and add:

pythonCopySECRET_KEY=your_secret_key
DATABASE_URL=your_database_url
CLOUDINARY_URL=your_cloudinary_url

Run migrations

bashCopypython manage.py migrate

Start development server

bashCopypython manage.py runserver
🧪 Testing
Validation

HTML - W3C HTML Validator
CSS - W3C CSS Validator
Python - PEP8 Online
JavaScript - JSHint

Manual Testing
Comprehensive testing performed on:

User authentication flows
Game mechanics
Leaderboard functionality
Profile management
Responsive design

🔜 Future Features

Platform-specific timing adjustments for mobile/desktop
Millisecond precision time indicator

📘 Credits
Team 'Bonkers'

Adam Swanick
Charlotte Dinsdale
Joe Sutherland
Rabinder Singh

Tools & Resources

Code Institute
Bootstrap
Font Awesome
Google Fonts

📝 License
This project is licensed under the MIT License.
📫 Contact

GitHub: @yourusername
Email: your.email@example.com


⭐ Star us on GitHub — it helps!