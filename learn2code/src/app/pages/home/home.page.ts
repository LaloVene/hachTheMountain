import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: './home.page.html',
  styleUrls: ['./home.page.scss'],
})

export class HomePage implements OnInit {
  public langs = [
    {
      id: 1,
      name: 'Python',
      img: 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/768px-Python-logo-notext.svg.png',
      desc: 'an interpreted, object-oriented, high-level programming language with dynamic semantics',
    },
    {
      id: 2,
      name: 'Java',
      img: 'https://upload.wikimedia.org/wikipedia/en/3/30/Java_programming_language_logo.svg',
      desc: 'null',
    },
    {
      id: 3,
      name: 'JavaScript',
      img: 'https://upload.wikimedia.org/wikipedia/commons/6/6a/JavaScript-logo.png',
      desc: 'null',
    },
    {
      id: 4,
      name: 'C++',
      img: 'https://upload.wikimedia.org/wikipedia/commons/1/18/ISO_C%2B%2B_Logo.svg',
      desc: 'null',
    },
    {
      id: 5,
      name: 'PHP',
      img: 'https://upload.wikimedia.org/wikipedia/commons/2/27/PHP-logo.svg',
      desc: 'null',
    },
    {
      id: 6,
      name: 'Swift',
      img: 'https://upload.wikimedia.org/wikipedia/commons/9/9d/Swift_logo.svg',
      desc: 'null',
    },
    {
      id: 7,
      name: 'SQL',
      img: 'https://upload.wikimedia.org/wikipedia/commons/8/87/Sql_data_base_with_logo.png',
      desc: 'null',
    },
    {
      id: 8,
      name: 'Ruby',
      img: 'https://upload.wikimedia.org/wikipedia/commons/7/73/Ruby_logo.svg',
      desc: 'null',
    },
    {
      id: 9,
      name: 'Go',
      img: 'https://en.wikipedia.org/wiki/Go_(programming_language)#/media/File:Go_Logo_Blue.svg',
      desc: 'null',
    },
    {
      id: 10,
      name: 'Visual Basic .NET',
      img: 'https://upload.wikimedia.org/wikipedia/commons/4/40/VB.NET_Logo.svg',
      desc: 'null',
    },
    {
      id: 11,
      name: 'R',
      img: 'https://upload.wikimedia.org/wikipedia/commons/1/1b/R_logo.svg',
      desc: 'null',
    },
    {
      id: 12,
      name: 'Perl',
      img: 'https://upload.wikimedia.org/wikipedia/en/e/e0/Programming-republic-of-perl.png',
      desc: 'null',
    },
    {
      id: 13,
      name: 'MATLAB',
      img: 'https://upload.wikimedia.org/wikipedia/commons/2/21/Matlab_Logo.png',
      desc: 'null',
    },
    {
      id: 14,
      name: 'LGBTQIA+ Resources',
      img: 'https://therainbowot.files.wordpress.com/2020/06/rainbow-fist-1.png?w=1024',
      desc: 'null',
    },
    {
      id: 15,
      name: '#LetIndiaBreathe Resources',
      img: 'https://www.letindiabreathe.in/logowhite-1.png',
      desc: 'null',
    },
    {
      id: 16,
      name: 'Mental Health Support',
      img: 'https://wfmh.global/wp-content/uploads/2018/01/wfmh-logo.png',
      desc: 'null',
    },
  ];
  public teams = [
    {
      id: 1,
      name: 'Carlos Moisés Chávez Jiménez',
      img: 'https://wfmh.global/wp-content/uploads/2018/01/wfmh-logo.png',
      desc: 'Computer Technologies student at Tecnólogio de Monterrey. He enjoys [tech-related]. In his free time, he likes to [non-tech related]. ',
      gh: 'https://github.com/NoMolestar',
      li: 'https://linkedin.com/in/moises-chavez-itesm/',
    },
    {
      id: 2,
      name: 'Charbel Breydy Torres',
      img: 'https://wfmh.global/wp-content/uploads/2018/01/wfmh-logo.png',
      desc: 'Robotics student at Universidad de las Américas Puebla. ',
    },
    {
      id: 3,
      name: 'Eduardo Venegas',
      img: 'https://wfmh.global/wp-content/uploads/2018/01/wfmh-logo.png',
      desc: 'Student at Tecnólogio de Monterrey.',
    },
    {
      id: 4,
      name: 'Ayana N',
      img: 'https://upload.wikimedia.org/wikipedia/commons/1/18/ISO_C%2B%2B_Logo.svg',
      desc: 'Student at McMaster University.',
    },
  ];

  ngOnInit() {}
}
