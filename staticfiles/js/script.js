// Game configuration

const TIME_TO_ANSWER = 3000; 

// Game state
let score = 0;
let promptTimer;
let currentPrompt;
let gameActive = false;

// Available prompts and their corresponding button ids
const prompts = [
    { text: "Pink", buttonId: "btn-pink" },
    { text: "Blue", buttonId: "btn-blue" },
    { text: "Green", buttonId: "btn-green" },
    { text: "Red", buttonId: "btn-red"},
    { text: "BONK IT!", buttonId: "btn-bonk"}
];

// DOM elements
const gameInstructionDiv = document.getElementById("game-instruction");
const currentScoreSpan = document.getElementById("current-score");
const startButton = document.getElementById("start-button");

// Start game function
function startGame() {
    score = 0;
    gameActive = true;
    updateScore();
    startButton.disabled = true;
    gameInstructionDiv.textContent = "Get Ready!"
    setTimeout(newPrompt, 1000);
   
}

// End game function
function endGame() {
    gameActive = false;
    clearTimeout(promptTimer);
    gameInstructionDiv.textContent = "Game Over! Final Score: " + score;
    startButton.disabled = false;
}

// Generate new prompt
function newPrompt() {
    if (!gameActive) return;
    
    let availablePrompts = prompts.filter(prompt => prompt !== previousPrompt);
    currentPrompt = availablePrompts[Math.floor(Math.random() * availablePrompts.length)];
    previousPrompt = currentPrompt;
    
    gameInstructionDiv.textContent = currentPrompt.text;
    
    promptTimer = setTimeout(() => {
        if (gameActive) endGame();
    }, TIME_TO_ANSWER);
}

// Handle button clicks
function handleButtonClick(buttonId) {
    if (!gameActive) return;
    
    clearTimeout(promptTimer);
    
    if (buttonId === currentPrompt.buttonId) {
        score++;
        updateScore();
        newPrompt();
    } else {
        endGame();
    }
}

// Update score display
function updateScore() {
    currentScoreSpan.textContent = score;
}

// Event listeners
startButton.addEventListener("click", startGame);

// Add click listeners to game buttons
prompts.forEach(prompt => {
    document.getElementById(prompt.buttonId).addEventListener("click", () => handleButtonClick(prompt.buttonId));
});
