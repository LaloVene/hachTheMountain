import { ComponentsModule } from './../../components/components.module';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { ResourcesPageRoutingModule } from './resources-routing.module';

import { ResourcesPage } from './resources.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    ResourcesPageRoutingModule,
    ComponentsModule,
  ],
  declarations: [ResourcesPage]
})
export class ResourcesPageModule {}
