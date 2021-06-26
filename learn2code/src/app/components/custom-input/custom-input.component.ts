import { Component, OnInit, Input } from '@angular/core';
import {
  ControlContainer,
  FormGroupDirective,
  FormGroup,
} from '@angular/forms';

@Component({
  selector: 'app-custom-input',
  templateUrl: './custom-input.component.html',
  styleUrls: ['./custom-input.component.scss'],
  viewProviders: [
    {
      provide: ControlContainer,
      useExisting: FormGroupDirective,
    },
  ],
})
export class CustomInputComponent implements OnInit {
  @Input() formControlName: string;
  @Input() formGroup: FormGroup;
  @Input() type: string;
  @Input() label: string;
  @Input() pattern: string = null;
  @Input() formSubmitted: boolean;
  @Input() mode: string;
  @Input() selectOptions: any[];
  @Input() selectTarget: string;

  constructor() {}

  ngOnInit() {}

  onInputChange() {}
  // Select Option Popover
}
