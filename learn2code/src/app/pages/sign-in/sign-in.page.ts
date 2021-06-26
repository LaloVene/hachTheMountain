import { ExampleService } from './../../services/example/example.service';
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
    private alertController: AlertController,
    private exampleService: ExampleService,
  ) {}

  ngOnInit() {
    this.createNewForm();
    this.exampleFunction();
  }

  // Doens´t work beacuase of CORS, I don´t think that will happen with ours
  exampleFunction() {
    // I pass it Hola as an example of what you could use it for
    this.exampleService.workingOne('hola!')
      .subscribe((res) => {
        // Normal behavior
        console.log(res);
      }, (err) => {
        // In case there is an error (Optional)
        console.log('ERROR:', err)
      });
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
