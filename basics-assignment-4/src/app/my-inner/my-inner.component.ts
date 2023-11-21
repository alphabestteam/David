import {Component, EventEmitter, Input, Output} from '@angular/core';

@Component({
  selector: 'app-my-inner',
  templateUrl: './my-inner.component.html',
  styleUrls: ['./my-inner.component.css']
})
export class MyInnerComponent {

  @Output() counterEmitter: EventEmitter<number> = new EventEmitter()

  innerCounter: number = 5;
  increment(): void {
    this.innerCounter++;

    if (this.innerCounter >= 10){
      this.innerCounter = 0;
      this.counterEmitter.emit(10);
    }

  }

  decrement(): void{
    this.innerCounter--;
    if (this.innerCounter <= -10) {
      this.innerCounter = 0;
      this.counterEmitter.emit(-10);
    }
  }

}
