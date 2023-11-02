const main = document.querySelector('main');



const naiveHead1 = createHeading('red', 'naive 1');
const naiveHead2 = createHeading('blue', 'naive 2');

//this is to be changed to append a header we create by using the higher order function headingFactory(color).
main.appendChild(naiveHead1);
main.appendChild(naiveHead2);

function createHeading(color, text){
    const heading = document.createElement('h1');
    heading.setAttribute('style', 'color: ' + color);
    heading.textContent = text;
    return heading;
}

function headingFactory(color){
    function createHeading(text){
        const heading = document.createElement('h1');
        heading.setAttribute('style', 'color:' + color)
        heading.textContent = text
        return heading
    }
    return createHeading
}

const createHeaderRed = headingFactory("red")
const createHeaderBlue = headingFactory("blue")

const usingFactory1 = createHeaderRed("using factory 1")
const usingFactory2 = createHeaderBlue("using factory 2")

main.appendChild(usingFactory1)
main.appendChild(usingFactory2)


// higher-order functions simplify our code and makes it way easier to read.
// It also is very good for making functions more dynamic in the way they are used which leads to overall better code.
// Makes the code more reusable.
