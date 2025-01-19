**

# Bonk It 🎮

**

BONKIT IMAGE


---
**Live Site** 
https://bonk-it-4b634a86c337.herokuapp.com/

**Repository**
https://github.com/charlottedinsdale/Final-Hackathon


---
📖 **Introduction**

Bonk It is a fun, easy-to-play game testing your reflexes and thinking by challenging you to press on instructed colors. 
Perfect for quick gaming sessions and brain training!

---
🎯 **Target Audience**

The game is designed for anyone who wants to enjoy a simple yet engaging game.  
Players seeking an extra challenge can try the advanced mode, which tests both reflexes and cognitive processing using the  'Stroop Effect' - a psychological phenomenon where the brain experiences conflict between processing the meaning of a word and the color in which it's written.   
For example, if the word "Red" appears in blue ink and you need to press the button corresponding to the word  (Red), your brain must resolve the conflict between the word's meaning and its visual color.


---
⭐ **Features**

Game Modes

There are 3 games modes.

 - Easy Mode: Basic color matching gameplay. The prompt states the
   colour and is in the colour you need to hit. 
   
 - Hard Mode: Increased difficulty with faster timing. The prompt only states the colour you
   need to hit. 
 
 - Heck Mode:  Advanced gameplay incorporating the 'Stroop Effect' whereby the prompt states the colour you need to hit whilst itself being in another colour.  
   

**Core Features**

The core features of the game are summarised below :

 - User authentication (register, login, logout) 
 - Customizable user profiles 
 - Global leaderboards 
 - Personal statistics tracking 
 - Multiple difficulty levels 
 - Colorblind mode support 
 - Audio feedback and game music


---
💫 **Technologies Used**

Languages
 - HTML5
 - CSS3
 - JavaScript
 - Python 3


Frameworks & Libraries
 - Django 
 - Bootstrap


Database
 - PostgreSQL


Tools
 - Git 
 - GitHub
 - Heroku
 - Miro (Project Ideation & Scoping, Wireframes) 
 - Cloudinary 
 - ChatGPT 
 - Perplexity.

   
---
🚀 **Getting Started.**
 

---
🧪 **Testing**

*Validation*

HTML - W3C HTML Validator.

CSS - W3C CSS Validator.

 Python 

JavaScript - JSHint.


*Manual Testing*
Comprehensive testing performed on:

  

User authentication flows

Game mechanics

Leaderboard functionality

Profile management

Responsive design

  
---
🔜 **Future Features**

 - Platform-specific timing adjustments for mobile/desktop

	- taking into account that the desktop users play using a mouse or keyboard whilst mobile users play using their hands

 - Millisecond precision time indicator
 

 ---
📘 **Credits**

***Team 'Bonkers'***

Adam Swanick
Charlotte Dinsdale
Joe Sutherland
Rabinder Singh

  
---
**Acknowledgements**

*Specific code used from Perplexity*

document.getElementById('start-button').addEventListener(

'click', function() {

fetch('/game/increment-total-games/',

{

method: 'POST',

headers: {

'Content-Type': 'application/json',

'X-CSRFToken': getCookie('csrftoken')

// Include CSRF token if using Django

}

})

.then(response => response.json())

.then(data => {

console.log('Total games incremented:',

data.total_games);

// Optionally update the UI to reflect the new

})

.catch(error => {

console.error('Error:', error);

});

});

  

// Function to get CSRF token (if using Django)

function getCookie(name) {

const cookieValue = document.cookie.split('; ').

find(.

row => row.startsWith(name + '='));

return cookieValue ? decodeURIComponent(.

cookieValue.split('=')[1]) : null;

}

  
 --- 
**Tools & Resources**

Code Institute
Bootstrap
Font Awesome
Google Fonts


--- 
⭐ Star us on GitHub — it helps!