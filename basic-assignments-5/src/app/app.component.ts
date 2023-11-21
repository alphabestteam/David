import { Component } from '@angular/core';
import { FILMS} from "./star-wars-fake-db/film-data";
import { Film } from './interfaces/film'
import {StarWarsMovie} from './interfaces/forceFilmInterface'
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  getAllFilmsTitlesAndLinks = (): Film[] => {
    const filmArr: Film[] = []
    FILMS.forEach((film: StarWarsMovie) =>{
      filmArr.push({title: film.title.toString(), link: film.title.replaceAll(" ", "-")})
    })
    return filmArr
  }

  allFilmsTitlesAndLinks: Film[] = this.getAllFilmsTitlesAndLinks()

}
