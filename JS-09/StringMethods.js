let movieInfo = " Kung Fu Panda is a beloved animated movie about a clumsy, food-loving panda named Po who dreams of becoming a kung fu master." +
    "\nPo's dream becomes a reality when he is unexpectedly chosen to become the Dragon Warrior and train with the Furious Five to protect the Valley of Peace from the evil Tai Lung." +
    "\nKung Fu Panda was released on June 6, 2008, and grossed over $631 million worldwide, making it the highest-grossing non-sequel animated film at the time of its release." +
    "\nAlong the way, Po learns valuable lessons about inner strength, perseverance, and the importance of family and friendship." +
    "\nWith stunning animation, a heartwarming story, and a star-studded cast including Jack Black, Angelina Jolie, and Jackie Chan, Kung Fu Panda has become a timeless classic for all ages."


const splitStringToArray = () => movieInfo.split("")

const replaceMovieToFilm = () => movieInfo.replace("movie", "film")

const replaceAllBearToPanda = () => movieInfo.replaceAll("Bear", "Panda")

const toUpperCase = () => movieInfo.toUpperCase()

const toLowerCase = () => movieInfo.toLowerCase()

const findPoInStr = () => movieInfo.search("Po")

const startFromPo = () => movieInfo.slice(findPoInStr())

const removeWhiteSpaces = () => movieInfo.trim()

const getFromPoTillPeriod = () => movieInfo.substring(movieInfo.indexOf("Po"), movieInfo.indexOf("."))


const replaceAllWhitespaces = () => movieInfo.trim().split(" ")

const endsWithAges = () => movieInfo.endsWith("ages.")

console.log(splitStringToArray())
console.log(replaceMovieToFilm())
console.log(replaceAllBearToPanda())
console.log(toUpperCase())
console.log(toLowerCase())
console.log(findPoInStr())
console.log(startFromPo())
console.log(removeWhiteSpaces())
console.log(getFromPoTillPeriod())
console.log(replaceAllWhitespaces())
console.log(endsWithAges())