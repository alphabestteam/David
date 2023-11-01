// 1. arr.at(index) is a newer feature that gives us the ability to use negative numbers to start from the end of the array (like in python).
//    arr[index] for the most part does the same thing just doesnt know how to start from the end by using a negative index
//    Example -> arr.at(-1) - This would get the last index in the array


// Q2
function createArrayFilledWith(letter, arrayLength) {
    return new Array(arrayLength).fill(letter)
}

// Q3
function removeElementsStartingFrom(n, arr) {
    if (isNaN(n)) {
        console.log("n must be a number")
        return
    } else if (n > arr.length) {
        console.log("n cant be bigger then the array")
        return;
    }

    return arr.slice(n)
}

// Q4
function addToBeginningOfArray(value, arr) {
    return arr.unshift(value)
}

// Q5
function concatenateArrays(arr1, arr2) {
    return arr1.concat(arr2)
}

// Q6
function convertArrayItemsToUpperCase(strArr) {
    return strArr.map(value => {
        return value.toUpperCase()
    })
}

// Q7
function filterDoubleDigitNumbers(numArr) {
    return numArr.filter(value => {
        const dividedValue = value / 10
        if (dividedValue >= 1 || dividedValue <= 9)
            return value
    })
}

// Q8
function isValueInArray(value, arr) {
    return arr.includes(value)
}

// Q9
function findFirstValueOverTen(arr) {
    return arr.find(value => {
        return value > 10
    })

}

// Q10
function doesContainValueOverTen(arr) {
    return firstIndexOverTen(arr) !== undefined
}

/*
*  11. Since the .sort() function sorts values as strings so when we try and do it on an int it only checks the first digit and sees whats bigger.
*       for example .sort() would think 4 is bigger than 100.
*       To fix this we need to use a compare function
*/

// Q12
function sortArrayNumerically(arr) {
    return arr.sort((a, b) => {
        return a - b
    })
}

// Q13
function joinArrayWithDelimiter(strArr) {
    return strArr.join("**")
}

// Q14
function sortStringArrayAlphabetically(strArr) {
    return strArr.sort()
}

// Q15
function areAllValuesLessThanThreshold(numArr, threshold) {
    return numArr.every(value => {
        return value < threshold
    })
}

// Q16
function doesContainValueGreaterThan(numArr, num) {
    return numArr.some(value => {
        return value > num
    })
}