function sequenceA() {
    setTimeout(_ => console.log('Sponge'), 0);
    console.log("Bob");
}

function sequenceB(){
    setTimeout(_ => console.log(`🍅 Timeout at B`), 0);
    Promise.resolve().then(_ => console.log('🍍 Promise at B'));
}

function sequenceC(){
    setTimeout(_ => console.log(`🍅 Timeout at C`), 0);
    Promise.resolve().then(_ => setTimeout(console.log('🍍 Promise at C'), 1000));
}

function sequenceD(){
    console.log('Sponge');
    setTimeout(_ => console.log('Square'), 0);
    Promise.resolve().then(_ => console.log('Pants'));
    console.log('Bob');
}

function questionA(){
    sequenceA();
}

function questionB(){
    sequenceB();
}

function questionC(){
    sequenceC();
}

function questionD(){
    sequenceD();
}

function questionE(){
    sequenceB();
    sequenceC();
}

// questionA();
//      First the console.log will be executed then the TimeOut.
//      Even tough the timeout was set to 0 millisecods it still gets schedualed to execute when the queue is empty,
//      meaning were still going to need to wait for console.log to be executed before we go and execute the timeout callback function.

// questionB();
//      Between setTimeout and Promises the Promises takes priority since it's a microtask which has a higher priority then a macrotask.
// questionC();
// questionD();
// questionE();