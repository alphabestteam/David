
const button = document.getElementById('the-button');
const main = document.querySelector("main");
const bobGif = document.getElementById("bob");



const toggleBob = function(){
    if (bobGif.classList.contains('hide')){
        bobGif.classList.remove('hide')
        button.textContent = "Hide Bob ;)"
    }else{
        bobGif.classList.add('hide')
        button.textContent = "Show me Bob ;)"
    }
};

button.addEventListener("click", toggleBob)