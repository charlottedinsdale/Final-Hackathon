// Game configuration


function calculateTimerDuration(score) {
    const baseTime = 1500; // Start with 1.5 seconds
    const minTime = 800; // Minimum time of 0.8 seconds
    const decreaseRate = 35; // Decrease by 50ms for each point
    
    let calculatedTime = baseTime - (score * decreaseRate);
    return Math.max(calculatedTime, minTime); // Ensure it doesn't go below minTime
}
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
const navbar = document.getElementById("navbar");
const footer = document.getElementById("footer");
const currentScoreSpan = document.getElementById("current-score");
const startButton = document.getElementById("start-button");
const playAgainButton = document.getElementById("play-again")
const gameOverModal = new bootstrap.Modal(document.getElementById('game-over-modal'));
const finalScoreSpan = document.getElementById("final-score");
const highScoreForm = document.getElementById("high-score-form");
const userHighScore = parseInt(document.getElementById('high-score').dataset.highScore);

// Start game function
function startGame() {
    score = 0;
    gameActive = true;
    updateScore();
    startButton.disabled = true;
    startButton.style.display = "none"
    gameInstructionDiv.textContent = "Get Ready!"
    previousPrompt = null;
    setTimeout(newPrompt, 2000);
   
}




// End game function
function endGame() {
    gameActive = false;
    clearTimeout(promptTimer);
    gameInstructionDiv.textContent = "Game Over! Final Score: " + score;
    startButton.disabled = false;
    footer.style.display = "flex";
    navbar.style.display = "block";
    // Update final score displays
    finalScoreSpan.textContent = score;
    document.getElementById("score-input").value = score;
    const highScoreElement = document.getElementById("user-high-score");
    const displayHighScore = isNaN(userHighScore) ? 0 : userHighScore;
    // Show/hide appropriate content based on score
    if (score > displayHighScore) {
        console.log(displayHighScore)
        document.getElementById("high-score-content").style.display = "block";
        document.getElementById("low-score-content").style.display = "none";
        document.getElementById("submit-score").style.display = "block";
        document.getElementById("play-again").style.display = "none";
    } else {
        document.getElementById("high-score-content").style.display = "none";
        document.getElementById("low-score-content").style.display = "block";
        document.getElementById("submit-score").style.display = "none";
        document.getElementById("play-again").style.display = "block";
        document.getElementById("user-high-score").textContent = userHighScore;
        highScoreElement.textContent = displayHighScore;
    }
    startButton.style.display = "flex"
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
    // gameInstructionDiv.className = `prompt-${currentPrompt.buttonId}`

    const timerDuration = calculateTimerDuration(score);

    promptTimer = setTimeout(() => {
        if (gameActive) endGame();
    }, timerDuration);
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
startButton.addEventListener("click", function(){
    footer.style.display = "none";
    navbar.style.display = "none";
    startGame();
});
document.getElementById('play-again').addEventListener('click', function() {
    let modal = bootstrap.Modal.getInstance(document.getElementById('game-over-modal'));
    footer.style.display = "none";
    navbar.style.display = "none";
    modal.hide();
    startGame();
  });

// Add click listeners to game buttons
prompts.forEach(prompt => {
    document.getElementById(prompt.buttonId).addEventListener("click", () => handleButtonClick(prompt.buttonId));
});