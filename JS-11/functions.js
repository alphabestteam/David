const helloWorld = () => "Hello World"

const sayHi = (name) => `Hello ${name}`

const setSquared = (number) => number * number

const rectangleArea = (width, length) => width * length

const circleValues = (radius) => {
    const circumference = 2 * Math.PI * radius
    const area = Math.PI * (radius ** 2)
    return [circumference, area]
}

const countVowels = (str) => {
    const vowels = "aeiou"
    return str.toLowerCase().split('').filter(char => {
        return vowels.includes(char)
    }).length;
}

const isSameLength = (arr1, arr2) => arr1.size === arr2.size

const numberToArray = (number) => {
    return number.toString().split("").map(num => {
        return parseInt(num)
    })
}

const getTruthyFalsyArr = (myArr) => {
    return myArr.map(value => {
        return !!value
    })
}

const myArr = [1, "hello", true, 0, false, "", " ", null, undefined, NaN, 2, "world", true, {}, [], 3, "foo", 'true', 'false', "bar"];

console.log(helloWorld());
console.log(sayHi("Ephraim"));
console.log(setSquared(4));
console.log(rectangleArea(5, 6));
console.log(circleValues(1));
console.log(countVowels('May the Force be with you. Always'));
console.log(isSameLength([1, 2, 3, 4], ["3", "aaa", "b", "q"]));
console.log(numberToArray(12345));
console.log(getTruthyFalsyArr(myArr));