function sequenceA() {
    setTimeout(_ => console.log('Sponge'), 3000);
    console.log("Bob");
}

function sequenceB() {
    setTimeout(_ => console.log(`🍅 Timeout at B`), 0);
    Promise.resolve().then(_ => console.log('🍍 Promise at B'));
}

function sequenceC() {
    setTimeout(_ => console.log(`🍅 Timeout at C`), 0);
    Promise.resolve().then(_ => setTimeout(console.log('🍍 Promise at C'), 1000));
}

function sequenceD() {
    console.log('Sponge');
    setTimeout(_ => console.log('Square'), 0);
    Promise.resolve().then(_ => console.log('Pants'));
    console.log('Bob');
}

function questionA() {
    sequenceA();
}

function questionB() {
    sequenceB();
}

function questionC() {
    sequenceC();
}

function questionD() {
    sequenceD();
}

function questionE() {
    sequenceB();
    sequenceC();
}

// questionA()
// questionB()
questionC()
// questionD()
// questionE()

//questionA();
//      First the console.log will be executed then the TimeOut.
//      Even tough the timeout was set to 0 milliseconds it still gets scheduled to execute when the queue is empty,
//      meaning were still going to need to wait for console.log to be executed before we go and execute the timeout callback function.

// questionB();
//      Between setTimeout and Promises the Promises takes priority since it's a microtask which has a higher priority then a macrotask which is what a setTimeout schedules.
// questionC();
//      Promise creates a microtasks which means it will be executed first, event though it includes a macrotask inside of it.
//      Once the microtask is dealt with it will move to the macrotask which is the first timeout.
//      first -> Promise at C
//      second -> Timeout at C
// questionD();
//      Same idea here first will be the console.logs then it will execute the promise then the timeout.
//      Since the timeout and promises get scheduled to run after the queue is empty it needs to wait for both logs to run
//      then they can run.
//      Order:
//      first -> Sponge
//      second -> Bob
//      third -> Pants
//      forth -> Square
// questionE();
//      This questions is a bit more tricky but overall keeps the same rules.
//      When we run sequenceB then sequenceC it starts putting things in the queue to run the first things to be run would be the microtasks then the macrotasks.
//      Order:
//      first -> Promise at B
//      second -> Promise at C
//      third -> Timeout at B
//      forth -> Timeout at C
