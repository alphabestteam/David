import {Component} from '@angular/core';

@Component({
    selector: 'app-root',
    templateUrl: './app.component.html',
    styleUrls: ['./app.component.css']
})
export class AppComponent {
    isDetailsToggled = true;
    timeStampLogs: Date[] = []

    toggleDetails(): void {
        this.isDetailsToggled = !this.isDetailsToggled
        this.timeStampLogs.push(new Date())
    }

    setBackground(eleIndex: number) {
        return eleIndex >= 5 ? {'background-color': 'blue'} : {}
    }

    setColor(eleIndex: number) {
        return eleIndex >= 5 ? 'color-white' : '';
    }
}