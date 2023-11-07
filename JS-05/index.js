function checkScore() {
    const testScore = document.getElementById("test-score").value
    if (isValidScore(testScore)) {
        const alphabeticalScore = getAlphabeticalScore(testScore)
        const scoreSentence = getScoreSentence(alphabeticalScore)
        const resultDiv = document.createElement("div")
        const results = document.createElement("p")
        results.id = "result-div"
        results.innerText = `Numeric Score: ${testScore}
            Alphabetical Score: ${alphabeticalScore}
            Score Sentence: ${scoreSentence}`

        document.body.appendChild(resultDiv)
        resultDiv.appendChild(results)

    } else {
        alert(`The score you entered: ${testScore}
               Test scores must only be numeric and between 0-100`)
    }

}

function getScoreSentence(alphabeticalScore) {
    switch (alphabeticalScore) {
        case "A+":
            return "Perfect!"
        case "A":
            return "Amazing!"
        case "B":
            return "Nicely done!"
        case "C":
            return "This is fine!"
        case "D":
            return "You can do better!"
        case "E":
            return "Moed B is an option!"
        case "F":
            return "Moed B is a must!"
    }
}

function isValidScore(testScore) {
    if (isNaN(parseInt(testScore))) {
        return false
    }
    return testScore <= 100 && testScore >= 0
}

const getAlphabeticalScore = (score) => {
    if (score === 100) {
        return "A+"
    } else if (score <= 99 && score >= 90) {
        return "A"
    } else if (score <= 89 && score >= 80) {
        return "B"
    } else if (score <= 79 && score >= 70) {
        return "C"
    } else if (score <= 69 && score >= 60) {
        return "D"
    } else if (score <= 59 && score >= 50) {
        return "E"
    } else {
        return "F"
    }
}
