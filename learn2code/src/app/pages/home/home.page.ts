import { Component, OnInit } from '@angular/core';
import { ModalController } from '@ionic/angular';
import { LanguagePreviewComponent } from '../../components/language-preview/language-preview.component';

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
      desc: 'An interpreted, object-oriented, high-level programming language with dynamic semantics.',
    },
    {
      id: 2,
      name: 'Java',
      img: 'https://upload.wikimedia.org/wikipedia/en/3/30/Java_programming_language_logo.svg',
      desc: 'A high-level, class-based, object-oriented programming language that is designed to have as few implementation dependencies as possible.',
    },
    {
      id: 3,
      name: 'JavaScript',
      img: 'https://upload.wikimedia.org/wikipedia/commons/6/6a/JavaScript-logo.png',
      desc: 'A programming language that conforms to the ECMAScript specification. JavaScript is high-level, often just-in-time compiled, and multi-paradigm.',
    },
    {
      id: 4,
      name: 'C++',
      img: 'https://upload.wikimedia.org/wikipedia/commons/1/18/ISO_C%2B%2B_Logo.svg',
      desc: 'A general-purpose programming language created as an extension of the C programming language.',
    },
    {
      id: 5,
      name: 'PHP',
      img: 'https://upload.wikimedia.org/wikipedia/commons/2/27/PHP-logo.svg',
      desc: 'A general-purpose scripting language especially suited to web development.',
    },
    {
      id: 6,
      name: 'Swift',
      img: 'https://upload.wikimedia.org/wikipedia/commons/9/9d/Swift_logo.svg',
      desc: 'A general-purpose, multi-paradigm, compiled programming language developed by Apple Inc. and the open-source community.',
    },
    {
      id: 7,
      name: 'SQL',
      img: 'https://upload.wikimedia.org/wikipedia/commons/8/87/Sql_data_base_with_logo.png',
      desc: 'A domain-specific language used in programming and designed for managing data held in a relational database management system, or for stream processing in a relational data stream management system.',
    },
    {
      id: 8,
      name: 'Ruby',
      img: 'https://upload.wikimedia.org/wikipedia/commons/7/73/Ruby_logo.svg',
      desc: 'An interpreted, high-level, general-purpose programming language.',
    },
    {
      id: 9,
      name: 'PoCIT Resources',
      img: 'https://peopleofcolorintech.com/wp-content/uploads/2015/08/small-logo-vertical.png',
      desc: '',
    },
    {
      id: 10,
      name: 'LGBTQIA+ Resources',
      img: 'https://therainbowot.files.wordpress.com/2020/06/rainbow-fist-1.png?w=1024',
      desc: '',
    },
    {
      id: 11,
      name: '#LetIndiaBreathe Resources',
      img: 'https://www.letindiabreathe.in/logowhite-1.png',
      desc: '',
    },
    {
      id: 12,
      name: 'Mental Health Support',
      img: 'https://wfmh.global/wp-content/uploads/2018/01/wfmh-logo.png',
      desc: '',
    },
  ];
  public teams = [
    {
      id: 1,
      name: 'Moisés Chávez',
      img: 'https://upload.wikimedia.org/wikipedia/en/6/68/ITESM_wordmark%2C_2014.png',
      desc: 'Computer Technologies student at Tecnólogio de Monterrey. He enjoys working with back-end technologies. In his free time, he likes to listen to music, watch movies and lift weights! ',
      gh: 'https://github.com/NoMolestar',
      li: 'https://linkedin.com/in/moises-chavez-itesm/',
    },
    {
      id: 2,
      name: 'Charbel Breydy Torres',
      img: 'https://www.udlap.mx/assets/img/logo-udlap-250.png',
      desc: 'Robotics and Telecommunications Engineering student at Universidad de las Américas Puebla (UDLAP). He enjoys learning about Machine Learning and Artificial Intelligence. In his free time he loves to cook and practice 6 different languages. Can you guess which ones? ',
      gh: 'https://github.com/buly1601',
      li: '',
    },
    {
      id: 3,
      name: 'Eduardo Venegas',
      img: 'https://upload.wikimedia.org/wikipedia/en/6/68/ITESM_wordmark%2C_2014.png',
      desc: 'Student at Tecnólogio de Monterrey. He works as a Full Stack Developer and as a Data Engineer. In his free time, he likes to lift weights while practicing his German language skills!',
      gh: 'https://github.com/LaloVene',
      li: 'https://www.linkedin.com/in/eduardo-venegas/',
    },
    {
      id: 4,
      name: 'Ayana Nithey',
      img: 'https://upload.wikimedia.org/wikipedia/en/5/53/McMaster_University_logo.svg',
      desc: 'Student at McMaster University majoring in Computer Science & Mathematics. Like to broaden French and Spanish language skills. In her free time, she likes to bike and help her friends and family transform their world with tech.',
      gh: 'https://github.com/nanonite9',
      li: 'https://linkedin.com/in/ayana-n',
    },
  ];
  public footers = [
    {
      id: 1,
      htm: 'https://hackthemountain.tech/',
    },
  ];
  
  

  constructor(private modalController: ModalController) {}

  ngOnInit() {}

  async presentModal(language: any) {
    const modal = await this.modalController.create({
      component: LanguagePreviewComponent,
      cssClass: 'my-custom-class',
      componentProps: {
        language: language,
      },
    });
    return await modal.present();
  }
}

