const quotes = [
    "I'm ready, I'm ready, I'm ready! - SpongeBob SquarePants",
    "F is for friends who do stuff together, U is for you and me, N is for anywhere and anytime at all! - SpongeBob SquarePants",
    "I'm not just ready, I'm ready Freddy! - SpongeBob SquarePants",
    "Remember, licking doorknobs is illegal on other planets. - SpongeBob SquarePants",
    "The inner machinations of my mind are an enigma. - Patrick Star",
    "I can't hear you, it's too dark in here! - Patrick Star",
    "I'm ugly and I'm proud! - SpongeBob SquarePants",
    "I'll have you know that I stubbed my toe last week while watering my spice garden and I only cried for 20 minutes. - Squidward Tentacles",
    "Once there was an ugly barnacle. He was so ugly that everyone died. The end. - Patrick Star",
    "Is mayonnaise an instrument? - Patrick Star",
    "Can you give SpongeBob his brain back? - Patrick Star",
    "I guess hibernation is the opposite of beauty sleep. - Squidward Tentacles",
    "I know of a place where you never get harmed. A magical place with magical charms. Indoors! Indoors! Indoors! - SpongeBob SquarePants",
    "I can't believe I'm finally wearing a Krusty Krab hat. Promotion, here I come! - SpongeBob SquarePants",
    "I'll take a double triple bossy deluxe on a raft, 4x4, animal-style, extra shingles with a shimmy and a squeeze, light axle grease, make it cry, burn it, and let it swim. - Bubble Bass",
    "Sandy: What do you usually do when I'm gone? SpongeBob: Wait for you to come back.",
    "SpongeBob: Don't worry, Mr. Krabs, I'll have you out of there faster than a toupee in a hurricane!",
    "SpongeBob: I know of a place where you never get harmed. A magical place with magical charm. Indoors. Indoors. Indoors. - Squidward: What's that? - SpongeBob: Outdoors.",
    "SpongeBob: Can I be excused for the rest of my life?",
    "SpongeBob: I'm not just ready, I'm ready Freddy!",
    "SpongeBob: You don't need a license to drive a sandwich.",
    "SpongeBob: Goodbye everyone, I'll remember you all in therapy.",
    "SpongeBob: Patrick, I don't think Wumbo is a real word. Patrick: Come on, SpongeBob, we're best friends. I would never call you a Wumbologist if I didn't think you were one.",
    "SpongeBob: I'm a Goofy Goober, yeah. You're a Goofy Goober, yeah. We're all Goofy Goobers, yeah. Goofy, goofy, goober, goober, yeah!",
    "SpongeBob: Once there was an ugly barnacle. He was so ugly that everyone died. The end."
];

let gameRunning = false
let startTime = null
let timerInterval = null

// time interval function
function updateTimer() {
    const currTime = new Date()
    const timeDifference = currTime - startTime
    const seconds = Math.floor(timeDifference / 1000)
    document.getElementById('timer').textContent = `Time: ${seconds}s`
}

function getRandomQuote() {
    const randomIndex = Math.round(Math.random() * (quotes.length - 1))
    return quotes[randomIndex]
}


function startGame() {
    // Check if he clicked the start button in middle of a game.
    if (gameRunning) restartTimer()

    gameRunning = true
    const quoteElement = document.getElementById('quote')
    const randomQuote = getRandomQuote()
    const quoteWords = randomQuote.split("")
    const input = document.getElementById('input')

    // Reset elements to have no values/children
    quoteElement.innerHTML = ''
    input.value = ''

    // Create and append span elements for each letter
    quoteWords.forEach(letter => {
        const span = document.createElement("span")
        span.textContent = letter
        span.setAttribute('class', 'letter')
        quoteElement.appendChild(span)
    })

    // Focus on the input, so he doesn't need to click the input to start.
    if (input.disabled) {
        input.disabled = false
    }
    input.focus()

    // Start time and interval
    startTime = new Date()
    timerInterval = setInterval(updateTimer, 1000)

}


// Check input to see if game finished and set the correct colors on each letter inputted
function checkInput() {
    const userInput = document.getElementById('input').value
    const letterElements = document.getElementsByClassName('letter')
    setCorrectIncorrectChars(userInput, letterElements)

    if (userInput.length === letterElements.length) {
        endGame(userInput)
    }
}

function setCorrectIncorrectChars(userInput, letterElements) {
    // Adds incorrect/correct classes to letters that match/don't match
    for (let i = 0; i < userInput.length; i++) {
        if (letterElements[i].textContent === userInput[i]) {
            letterElements[i].classList.remove('incorrect')
            letterElements[i].classList.add('correct')
        } else {
            letterElements[i].classList.remove('correct')
            letterElements[i].classList.add('incorrect')
        }
    }

    // Removes all incorrect/correct markings for letters that aren't written in the input. (In case you try to delete a whole word at once)
    for (let i = userInput.length; i < letterElements.length; i++) {
        letterElements[i].classList.remove('incorrect')
        letterElements[i].classList.remove('correct')
    }
}

function restartTimer() {
    clearInterval(timerInterval)
}


// End game handling
function endGame() {
    gameRunning = false;
    clearInterval(timerInterval);

    const input = document.getElementById('input')
    input.disabled = true
    const endTime = new Date();
    const overAllTime = endTime - startTime;
    const overAllSeconds = (overAllTime / 1000).toFixed(2);

    const resultElement = document.getElementById('result');
    const letterElements = Array.from(document.getElementsByClassName('letter'));
    const wordCount = document.getElementById('quote').textContent.split(" ").length;
    const wordsPerMin = ((wordCount / (overAllSeconds / 60)).toFixed(2))

    const badChars = letterElements.filter(element => element.classList.contains('incorrect'));
    const goodChars = letterElements.filter(element => element.classList.contains('correct'));
    const accuracy = ((goodChars.length / (goodChars.length + badChars.length)) * 100).toFixed(2);


    resultElement.textContent = `You typed ${wordCount} words
                                 in ${overAllSeconds} seconds.
                                 Your speed is ${wordsPerMin} wpm.
                                 With ${accuracy}% accuracy`

    saveDataLocally(wordCount, parseFloat(overAllSeconds), parseFloat(wordsPerMin), parseFloat(accuracy))
}

function saveDataLocally(wordCount, overAllSeconds, wordsPerMin, accuracy){
    // localStorage.clear()

    const score = parseFloat((wordsPerMin * accuracy / 10).toFixed(2))
    const gameData = getLocalGameData()
    const currGameData = {
        wordCount: wordCount,
        overAllSeconds: overAllSeconds,
        wordsPerMin: wordsPerMin,
        accuracy: accuracy,
        score: score
    }
    console.log(typeof(gameData))
    gameData.push(currGameData)
    console.log(gameData)
    localStorage.setItem('games', gameData)
    console.log(getLocalGameData())
}

const getLocalGameData = ()=>{
    const oldGames = localStorage.getItem('games')
    return JSON.parse(oldGames) || []
}

document.getElementById('input').addEventListener('input', checkInput)
document.getElementById('start-btn').addEventListener('click', startGame)
document.addEventListener('keydown', (event) => {
    if (event.key === 'Enter') {
        document.getElementById('start-btn').focus()
    }
})
