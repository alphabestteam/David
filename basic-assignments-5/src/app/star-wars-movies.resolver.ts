import {ActivatedRouteSnapshot, ResolveFn} from '@angular/router';
import {resolve} from "@angular/compiler-cli";
import { StarWarsMovie } from "./interfaces/forceFilmInterface";
import {Injectable} from "@angular/core";



export const starWarsMoviesResolver: ResolveFn<boolean> = (route, state) => {
return true
};


