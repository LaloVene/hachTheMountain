import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { AlertController } from '@ionic/angular';

@Component({
  selector: 'app-sign-in',
  templateUrl: './sign-in.page.html',
  styleUrls: ['./sign-in.page.scss'],
})
export class SignInPage implements OnInit {
  // Form
  public registerForm: FormGroup;
  public registerFormSubmitted: boolean = false;
  public loginForm: FormGroup;
  public loginFormSubmitted: boolean = false;

  constructor(
    private formBuilder: FormBuilder,
    private alertController: AlertController
  ) {}

  ngOnInit() {
    this.createNewForm();
  }

  createNewForm() {
    this.registerForm = this.formBuilder.group({
      username: ['', Validators.required],
      password: ['', Validators.required],
    });
    this.loginForm = this.formBuilder.group({
      username: ['', Validators.required],
      password: ['', Validators.required],
    });
  }

  register() {
    this.registerFormSubmitted = true;
    if (this.registerForm.invalid) {
      this.badForm();
    } else {
      console.log(111);
    }
  }
  login() {
    this.loginFormSubmitted = true;
    if (this.loginForm.invalid) {
      this.badForm();
    } else {
      console.log(111);
    }
  }

  async badForm() {
    const alert = await this.alertController.create({
      message: 'Favor de verificar algunos campos',
      buttons: [
        {
          text: 'Ok',
          handler: () => {
            alert.dismiss();
          },
        },
      ],
    });
    await alert.present();
  }
}
