import { Component, OnInit } from '@angular/core';
import { NavController } from '@ionic/angular';

@Component({
  selector: 'app-diff-popover',
  templateUrl: './diff-popover.component.html',
  styleUrls: ['./diff-popover.component.scss'],
})
export class DiffPopoverComponent implements OnInit {
  constructor(private nav: NavController) {}

  ngOnInit() {}

  public navigateTo(url: string) {
    this.nav.navigateRoot(url);
  }
}
