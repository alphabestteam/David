import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MovieCardComponent } from "./movie-card/movie-card.component";
import { FILMS } from './star-wars-fake-db/film-data'
import { StarWarsMovie } from './interfaces/forceFilmInterface'


const getMovieTitle = (title: string) :StarWarsMovie | undefined => {
  return FILMS.find((film: StarWarsMovie): boolean => film.title === title )
}


const routes: Routes = [
  {path: 'The-Phantom-Menace', component: MovieCardComponent, data: {movie: getMovieTitle("The Phantom Menace")}},
  {path: 'Attack-of-the-Clones', component: MovieCardComponent, data: {movie: getMovieTitle("Attack of the Clones")}},
  {path: 'Revenge-of-the-Sith', component: MovieCardComponent, data: {movie: getMovieTitle("Revenge of the Sith")}},
  {path: 'A-New-Hope', component: MovieCardComponent, data: {movie: getMovieTitle("A New Hope")}},
  {path: 'The-Empire-Strikes-Back', component: MovieCardComponent, data: {movie: getMovieTitle("The Empire Strikes Back")}},
  {path: 'Return-of-the-Jedi', component: MovieCardComponent, data: {movie: getMovieTitle("Return of the Jedi")}},
];



@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
