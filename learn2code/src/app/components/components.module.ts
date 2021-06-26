import { NavbarComponent } from './navbar/navbar.component';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { IonicModule } from '@ionic/angular';
import { CustomInputComponent} from './custom-input/custom-input.component'
import { DiffPopoverComponent } from './diff-popover/diff-popover.component';


@NgModule({
  declarations: [CustomInputComponent, DiffPopoverComponent, NavbarComponent],
  imports: [CommonModule, IonicModule, FormsModule, ReactiveFormsModule],
  exports: [CustomInputComponent, DiffPopoverComponent, NavbarComponent],
})
export class ComponentsModule {}
