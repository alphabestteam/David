import {Component} from '@angular/core';
import {FormBuilder, FormGroup, Validators} from "@angular/forms";


interface Info {
  email: string;
  username: string;
  password: String;
}


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})

export class AppComponent {

  myForm: FormGroup;

  isSubmitted: boolean = false;

  submittedInfo: Info = {
    email: '',
    username: '',
    password: ''
  }

  constructor(private fb: FormBuilder) {
    this.myForm = fb.group({
      email: ['', [Validators.required, Validators.email]],
      username: ['', [Validators.required, Validators.minLength(3)]],
      password: ['', [Validators.required, Validators.minLength(8)]],
    });
  }

  isFieldInvalid(field: string): boolean | undefined {
    const formControl = this.myForm.get(field)
    return formControl?.invalid && (formControl.dirty || formControl.touched)
  }

  onSubmit(): void {
    this.submittedInfo.email = this.myForm.value.email
    this.submittedInfo.username = this.myForm.value.username
    this.submittedInfo.password = this.myForm.value.password

    this.isSubmitted = true
  }
}
