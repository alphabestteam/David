import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';
import {FormsModule} from '@angular/forms';

import {MatInputModule} from '@angular/material/input';
import {MatSelectModule} from '@angular/material/select';
import {MatFormFieldModule} from '@angular/material/form-field';


import {AppComponent} from './app.component';
import {WarningAlertComponent} from './warning-alert/warning-alert.component';
import {SuccessAlertComponent} from './success-alert/success-alert.component';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import {MatSlideToggleModule} from "@angular/material/slide-toggle";
import {SelectorComponent} from './selector/selector.component';
import {MatButtonModule} from "@angular/material/button";

@NgModule({
    declarations: [
        AppComponent,
        WarningAlertComponent,
        SuccessAlertComponent,
    ],
    imports: [
        BrowserModule,
        FormsModule,
        BrowserAnimationsModule,
        MatSlideToggleModule,
        MatInputModule,
        MatSelectModule,
        MatFormFieldModule,
        SelectorComponent,
        MatButtonModule,
    ],
    providers: [],
    bootstrap: [AppComponent]
})
export class AppModule {
}
