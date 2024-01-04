import {Component, Input} from '@angular/core';

@Component({
  selector: 'app-item',
  templateUrl: './item.component.html',
  styleUrls: ['./item.component.scss']
})
export class ItemComponent {
  @Input() item: string = ""
  @Input() inCart: boolean = false;

  addToCart(): void {
    const items: string[] = localStorage.getItem('items')?.split(',') || []

    if (items.includes(this.item)){
      alert("Item already in your cart")
      return
    }

    items.push(this.item)
    localStorage.setItem('items', items.join(','))
    alert(`${this.item} successfully ADDED to your cart`)
  }

  removeFromCart(): void {
    const items: string[] = localStorage.getItem('items')?.split(',') || []
    const newItems: string[] = items.filter((item: string): boolean => {
      return item !== this.item
    })
    localStorage.setItem('items', newItems.join(','))
    alert(`${this.item} successfully REMOVED from your cart`)
  }
}
