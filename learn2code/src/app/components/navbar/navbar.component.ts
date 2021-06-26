import { Component, OnInit } from '@angular/core';
import { NavController } from '@ionic/angular';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss'],
})
export class NavbarComponent implements OnInit {
  constructor(
    private nav: NavController,
  ) {}

  ngOnInit() {}

  public navigateTo(url:string) {
    this.nav.navigateRoot(url);
  }
}
