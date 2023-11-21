import {Component} from '@angular/core';

@Component({
    selector: 'app-my-outer',
    templateUrl: './my-outer.component.html',
    styleUrls: ['./my-outer.component.css']
})
export class MyOuterComponent {

    outerCounter: number = 0;
    handleOuterCounter(number: number): void {
        this.outerCounter += number
    }
}
