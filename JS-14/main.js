const mainHeading = document.getElementById("main-heading")
console.log(mainHeading.id)
console.log(mainHeading.className)
console.log(mainHeading.classList)
console.log(mainHeading.dataset)
console.log(mainHeading.getAttribute("nonStandard"))
mainHeading.classList.add("bg-lightcyan", "border")
console.log(mainHeading.textContent)
console.log(mainHeading.textContent.trim())
mainHeading.textContent = "Hello there pearl!"

const bobsSpan = document.createElement('span')
bobsSpan.innerHTML = '<br> its me spongebob!'
mainHeading.appendChild(bobsSpan)
console.log(mainHeading)
const cloned = mainHeading.cloneNode(true)
console.log(cloned)

const subHeading = document.createElement("h2")
subHeading.textContent = "jellyfish hunting is the best"

document.body.appendChild(subHeading)

const loremIpsumStr = "Lorem ipsum dolor sit amet consectetur adipiscing elit," +
    " urna consequat felis vehicula class ultricies mollis dictumst," +
    " aenean non a in donec nulla. Phasellus ante pellentesque erat cum risus consequat imperdiet aliquam," +
    " integer placerat et turpis mi eros nec lobortis taciti, vehicula nisl litora tellus ligula porttitor metus."

const loremArr = loremIpsumStr.split(" ")
const colors = ["red", "orange", "yellow", "greenyellow", "lightblue", "mediumpurple"]

const getRandomColor = () => {
    if (colors.length === 0) return;
    return Math.round(Math.random() * 16777215).toString(16).padStart(6, '0') //This reason we use padStart is in case it returns something less than the length 6 we want to add 0's till it reaches the length of 6.
}

const randomWordsElement = document.getElementById("random-words")

loremArr.forEach(word => {
    const span = document.createElement("span")
    const style = "background-color: #" + getRandomColor()
    span.setAttribute("style", style)
    span.textContent = word
    span.className = "random-word"
    randomWordsElement.appendChild(span)
})

function changeBackgroundColor() {
    const loremWordsElements = document.querySelectorAll('[class=random-word]')
    loremWordsElements.forEach(element => {
        const style = "background-color: #" + getRandomColor()
        element.setAttribute("style", style)
    })
}

document.getElementById("background-change-btn").addEventListener('click', changeBackgroundColor)