import {Component} from '@angular/core';

@Component({
    selector: 'app-my-outer',
    templateUrl: './my-outer.component.html',
    styleUrls: ['./my-outer.component.css']
})
export class MyOuterComponent {

    innerCounter: number = 5;
    outerCounter: number = 0;
    handleOuterCounter(innerCounter: number): void {
        if (innerCounter === 10 || innerCounter === -10) {
            console.log(innerCounter)
            this.outerCounter += innerCounter
            this.innerCounter = 0
        }else{
            this.innerCounter = innerCounter;
        }
    }
}
