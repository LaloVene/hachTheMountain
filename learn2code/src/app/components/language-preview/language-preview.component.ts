import { Component, OnInit, Input } from '@angular/core';
import { ModalController, NavController } from '@ionic/angular';

@Component({
  selector: 'app-language-preview',
  templateUrl: './language-preview.component.html',
  styleUrls: ['./language-preview.component.scss'],
})
export class LanguagePreviewComponent implements OnInit {
  @Input() language: any;

  constructor(
    private modalController: ModalController,
    private nav: NavController,
  ) {}

  ngOnInit() {}

  public navigateTo(id: number) {
    this.nav.navigateRoot(`language/${id}`);
    this.dismiss();
  }

  // Dismiss Modal
  dismiss() {
    this.modalController.dismiss({
      dismissed: true,
    });
  }
}
