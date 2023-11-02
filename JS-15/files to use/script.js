const button = document.getElementById('the-button');
const main = document.querySelector("main");
const bobGif = document.getElementById("bob");


const toggleBob = function () {
    if (bobGif.getAttribute("data-toggle") === 'hidden') {
        bobGif.style.display = 'block'
        bobGif.setAttribute("data-toggle", "shown")
        button.textContent = "Hide Bob ;)"
    } else {

        bobGif.style.display = 'none'
        bobGif.setAttribute("data-toggle", "hidden")
        button.textContent = "Show me Bob ;)"
    }
};

