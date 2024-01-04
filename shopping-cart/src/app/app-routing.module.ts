import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {CartComponent} from "./cart/cart.component";
import {ShopComponent} from "./shop/shop.component";

const routes: Routes = [
  {path: "", component: ShopComponent},
  {path: "shop", component: ShopComponent},
  {path: "cart", component: CartComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
