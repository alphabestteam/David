const evalNumbers = (firstNum, secondNum, operator) => {
    let operatorSymbol = getOperatorSymbol(operator)

    return eval(`${firstNum}
    ${operatorSymbol}
    ${secondNum}`)
}

const getOperatorSymbol = (operator) =>{
    switch (operator.toLowerCase()) {
        case 'add':
            return '+';
        case 'subtract':
            return '-';
        case 'multiply':
            return '*'
        case 'divide':
            return '/'
        case 'modulus':
            return '%'
    }
}