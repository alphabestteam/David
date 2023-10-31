let bobsLost = true

alert("OMG, BOB IS LOST! Patric we need you to find him ASAP!")

while (bobsLost) {

    let bobsAnswer = confirm("Patric did you start searching for him yet??")

    if (bobsAnswer) {
        alert("I'm glad you started looking for him.I Wish You The Best Of Luck In Your Journey!")
        let wasBobFound = prompt("Did you successfully find Bob??").toLowerCase()
        if (wasBobFound === "yes") {
            alert("Wow that was fast! Cant believe you found him, I'm so happy")
            bobsLost = false
        } else {
            alert("Damn that's unlucky keep searching.")
        }
    } else {
        alert("Common Patric we need to find him.")
    }
}
