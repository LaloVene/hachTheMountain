import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-resources',
  templateUrl: './resources.page.html',
  styleUrls: ['./resources.page.scss'],
})
export class ResourcesPage implements OnInit {
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
          url: 'www.google.com'
        },
        {
          id: 1,
          id_rec: 1,
          name: 'Link 12',
          url: 'www.google.com'
        },
        {
          id: 1,
          id_rec: 1,
          name: 'Link 21',
          url: 'www.google.com'
        },
        {
          id: 1,
          id_rec: 1,
          name: 'Link 121',
          url: 'www.google.com'
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
          url: 'www.google.com'
        }
      ],
    },
  ];

  constructor() {}

  ngOnInit() {}
}
