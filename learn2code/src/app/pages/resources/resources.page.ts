import { Component, OnInit } from '@angular/core';
import { ExampleService } from './../../services/example/example.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-resources',
  templateUrl: './resources.page.html',
  styleUrls: ['./resources.page.scss'],
})
export class ResourcesPage implements OnInit {
  language_id: number;
  language: any;
  public resources = [
    {
      id: 1,
      id_topic: 1,
      difficulty: 1,
      title: 'Introduction',
      urls: [
        {
          id: 1,
          id_rec: 1,
          name: 'Link 1',
          url: 'www.google.com',
        },
        {
          id: 1,
          id_rec: 1,
          name: 'Link 12',
          url: 'www.google.com',
        },
        {
          id: 1,
          id_rec: 1,
          name: 'Link 21',
          url: 'www.google.com',
        },
        {
          id: 1,
          id_rec: 1,
          name: 'Link 121',
          url: 'www.google.com',
        },
      ],
      videos: [
        {
          name: 'Javascript',
          url: 'PkZNo7MFNFg',
        },
      ],
    },
    {
      id: 1,
      id_topic: 1,
      difficulty: 1,
      title: 'Other',
      urls: [
        {
          id: 1,
          id_rec: 1,
          name: 'Link 1',
          url: 'www.google.com',
        },
      ],
      videos: [
        {
          name: 'Javascript',
          url: 'PkZNo7MFNFg',
        },
      ],
    },
  ];

  constructor(
    private exampleService: ExampleService,
    private route: ActivatedRoute
  ) {
    this.language_id = parseInt(this.route.snapshot.paramMap.get('id'));
    this.getLanguages();
  }

  ngOnInit() {}

  private getLanguages() {
    this.exampleService.getLanguages().subscribe((data) => {
      this.language = data.languages.find(
        (lang) => lang.IdLanguages == this.language_id
      );
    });
  }
}
