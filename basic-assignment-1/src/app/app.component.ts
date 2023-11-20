import {Component} from '@angular/core';

@Component({
    selector: 'app-root',
    templateUrl: './app.component.html',
    styleUrls: ['./app.component.css']
})
export class AppComponent {
    alertAmount: number[] = []

    btnColor: string = 'primary'
    btnName: string = 'success'
    alertDisplayed: string = 'warning';

    setAlertAmount(amount: number): void {
        this.alertAmount = Array(amount).fill(0);
    }

    changeAlertDisplay: () => void = () => {
        this.alertDisplayed = this.alertDisplayed === 'warning' ? 'success' : 'warning';
        this.btnColor = this.btnColor === 'primary' ? 'warn' : 'primary'
        this.btnName = this.btnName === 'success' ? 'warn' : 'success'
    }
}
