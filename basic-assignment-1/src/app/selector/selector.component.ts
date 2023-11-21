import {Component, EventEmitter, Output} from '@angular/core';
import {FormsModule} from '@angular/forms';
import {MatInputModule} from '@angular/material/input';
import {MatSelectModule} from '@angular/material/select';
import {MatFormFieldModule} from '@angular/material/form-field';
import {NgForOf} from "@angular/common";


@Component({
    selector: 'app-selector',
    templateUrl: './selector.component.html',
    styleUrl: './selector.component.css',
    standalone: true,
    imports: [MatFormFieldModule, MatSelectModule, MatInputModule, FormsModule, NgForOf],
})
export class SelectorComponent {
    @Output() newItemEvent = new EventEmitter<number>();

    onSelected(num: number): void {
        this.newItemEvent.emit(num)
    }

    numbers: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    protected readonly parseInt = parseInt;
}
