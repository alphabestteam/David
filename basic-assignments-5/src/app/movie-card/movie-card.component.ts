import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { StarWarsMovie } from '../interfaces/forceFilmInterface'

@Component({
  selector: 'app-movie-card',
  templateUrl: './movie-card.component.html',
  styleUrls: ['./movie-card.component.scss']
})
export class MovieCardComponent {
    starWarsMovie?: StarWarsMovie;

    constructor(private route: ActivatedRoute) {
    }
    ngOnInit(): void {
        this.starWarsMovie = this.route.snapshot.data['movie'];
    }

}
