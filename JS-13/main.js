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

function getRandomColor(arr) {
    if (colors.length === 0) return;
    const randomIndex = Math.round(Math.random() * (colors.length - 1))
    return arr[randomIndex]
}

const randomWordsElement = document.getElementById("random-words")

loremArr.forEach(word => {
    const span = document.createElement("span")
    const style = "background-color: " + getRandomColor(colors)
    span.setAttribute("style", style)
    span.textContent = word
    span.className = "random-word"
    randomWordsElement.appendChild(span)
})

