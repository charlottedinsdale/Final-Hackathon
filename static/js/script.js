// Game configuration

const TIME_TO_ANSWER = 2000; 
// const userHighScore = {{ user_high_score }};

// Game state
let score = 0;
let promptTimer;
let currentPrompt;
let previousPrompt
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
const gameOverModal = new bootstrap.Modal(document.getElementById('game-over-modal'));
const finalScoreSpan = document.getElementById("final-score");
const highScoreForm = document.getElementById("high-score-form");

// Start game function
function startGame() {
    score = 0;
    gameActive = true;
    updateScore();
    startButton.disabled = true;
    gameInstructionDiv.textContent = "Get Ready!"
    previousPrompt = null;
    setTimeout(newPrompt, 2000);
   
}

// Assuming you've defined these at the top of your script

const userHighScore = parseInt(document.getElementById('high-score').dataset.highScore);

// End game function
function endGame() {
    gameActive = false;
    clearTimeout(promptTimer);
    gameInstructionDiv.textContent = "Game Over! Final Score: " + score;
    startButton.disabled = false;

    // Update final score displays
    finalScoreSpan.textContent = score;
    document.getElementById("score-input").value = score;
    
    // Show/hide appropriate content based on score
    if (score > userHighScore) {
        document.getElementById("high-score-content").style.display = "block";
        document.getElementById("low-score-content").style.display = "none";
    } else {
        document.getElementById("high-score-content").style.display = "none";
        document.getElementById("low-score-content").style.display = "block";
        document.getElementById("user-high-score").textContent = userHighScore;
    }
    
    // Show the Bootstrap modal
    gameOverModal.show();
}



// Generate new prompt
function newPrompt() {
    if (!gameActive) return;
    
    let availablePrompts = prompts.filter(prompt => prompt !== previousPrompt);
    currentPrompt = availablePrompts[Math.floor(Math.random() * availablePrompts.length)];
    previousPrompt = currentPrompt;
    
    gameInstructionDiv.textContent = currentPrompt.text;
    gameInstructionDiv.className = `prompt-${currentPrompt.buttonId}`

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
