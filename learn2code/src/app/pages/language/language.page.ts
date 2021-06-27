import { ExampleService } from './../../services/example/example.service';
import { Component, OnInit } from '@angular/core';
import { PopoverController } from '@ionic/angular';
import { DiffPopoverComponent } from './../../components/diff-popover/diff-popover.component';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-language',
  templateUrl: './language.page.html',
  styleUrls: ['./language.page.scss'],
})
export class LanguagePage implements OnInit {
  language_id: number;
  language: any;
  public topics = [
    {
      id: 1,
      name: 'Introduction',
      img: 'https://img.icons8.com/pastel-glyph/2x/code.png',
    },
    {
      id: 2,
      name: 'Data Structures & Algorithms',
      img: 'https://hackr.io/tutorials/learn-data-structures-algorithms/logo/logo-data-structures-algorithms?ver=1587721467',
    },
    {
      id: 3,
      name: 'Web',
      img: 'https://image.flaticon.com/icons/png/512/841/841364.png',
    },
    {
      id: 4,
      name: 'Machine Learning',
      img: 'https://image.flaticon.com/icons/png/512/2103/2103626.png',
    },
  ];

  constructor(
    public popoverController: PopoverController,
    private exampleService: ExampleService,
    private route: ActivatedRoute
  ) {
    this.language_id = parseInt(this.route.snapshot.paramMap.get('id'));
    this.getTopics(this.language_id);
    this.getLanguages();
  }

  ngOnInit() {}

  getTopics(id: number) {
    let body = {
      idTopic: id,
    };
    this.exampleService.getTopics(body).subscribe((data) => {
      this.topics = data.topics;
    });
  }
  private getLanguages() {
    this.exampleService.getLanguages().subscribe((data) => {
      this.language = data.languages.find(
        (lang) => lang.IdLanguages == this.language_id
      );
    });
  }

  async presentPopover(ev: any, id: number) {
    const popover = await this.popoverController.create({
      component: DiffPopoverComponent,
      cssClass: 'round-popover',
      event: ev,
      translucent: true,
    });
    await popover.present();

    const { role } = await popover.onDidDismiss();
    console.log('onDidDismiss resolved with role', role);
  }
}
