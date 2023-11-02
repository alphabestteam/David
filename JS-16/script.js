function addEvent() {
    let clickCount = 0
    function increment(){
        clickCount++
        document.getElementById("counter-display").textContent = clickCount
    }
    return increment
}
const increment = addEvent();

