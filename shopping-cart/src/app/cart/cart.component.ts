import {Component, OnInit} from '@angular/core';

@Component({
  selector: 'app-cart',
  templateUrl: './cart.component.html',
  styleUrls: ['./cart.component.scss']
})
export class CartComponent implements OnInit{
  items: string[] | null = null

  ngOnInit(){
    const storage: string | null= localStorage.getItem('items')
    if (storage){
      this.items = storage.split(',')
      if (this.items[0] === ""){
        this.items.shift()
      }
    }
  }
}
