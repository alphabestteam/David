let movieInfo = " Kung Fu Panda is a beloved animated movie about a clumsy, food-loving panda named Po who dreams of becoming a kung fu master." +
    "\nPo's dream becomes a reality when he is unexpectedly chosen to become the Dragon Warrior and train with the Furious Five to protect the Valley of Peace from the evil Tai Lung." +
    "\nKung Fu Panda was released on June 6, 2008, and grossed over $631 million worldwide, making it the highest-grossing non-sequel animated film at the time of its release." +
    "\nAlong the way, Po learns valuable lessons about inner strength, perseverance, and the importance of family and friendship." +
    "\nWith stunning animation, a heartwarming story, and a star-studded cast including Jack Black, Angelina Jolie, and Jackie Chan, Kung Fu Panda has become a timeless classic for all ages."


function splitStringToArray(){
    return movieInfo.split("")
}

function replaceMovieInfo(){
    return movieInfo.replace("movie", "film")
}

function replaceAllMovieInfo(){
    return movieInfo.replaceAll("Bear", "Panda")
}

function toUpperCase(){
    return movieInfo.toUpperCase()
}

function toLowerCase(){
    return movieInfo.toLowerCase()
}

function findPoInStr(){
    return movieInfo.search("Po")
}

function startFromPo(){
    return movieInfo.split("Po")[1]
}

function removeWhiteSpaces(){
    return movieInfo.trim()
}

function getFromPoTillPeriod(){
    return movieInfo.substring(movieInfo.indexOf("Po ")-1, movieInfo.indexOf("."))
}

function replaceAllWhitespaces(){
    return movieInfo.trim().split(" ")
}

function endsWithAges(){
    return movieInfo.endsWith("ages.")
}