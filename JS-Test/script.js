/*
List of endpoints:
  GET - http://localhost:8000/hello -> {'Hello': 'World'} Here as an example
  GET - http://localhost:8000/menu -> {'items': menu} A dict of the menu
  POST - http://localhost:8000/latest-order -> A dict of the latest order
  POST - http://localhost:8000/orders -> An endpoint to handle an order. The order is in the http body as so: { 'items': items }

*/

let itemsObjects = null


createOrderSummaryList = () => {
    const orderSummary = document.getElementById('order-summary')
    const unorderedList = document.createElement('ul')
    unorderedList.setAttribute('id', 'order-list')
    orderSummary.appendChild(unorderedList)
}

createElementsAndDisplay = (items) => {
    const menuDiv = document.getElementById('menu')
    const itemKeys = Object.keys(items)

    itemKeys.forEach((item, index) => {
        itemsObjects['items'][item]['quantity'] = 0
        let USDollar = new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: 'USD',
        });

        const itemName = item
        const itemPrice = items[item]['price']
        const formattedPrice = USDollar.format(itemPrice)
        const itemDesc = items[item]['description']

        const itemContainerEle = document.createElement('div')
        itemContainerEle.classList.add('item')
        itemContainerEle.classList.add('card')

        const itemHeadingEle = document.createElement('h3')
        itemHeadingEle.textContent = `${itemName} (${formattedPrice})`

        const itemDescEle = document.createElement('p')
        itemDescEle.textContent = itemDesc

        const quantityLabelEle = document.createElement('label')
        quantityLabelEle.setAttribute('for', `item-quantity-${index}`)
        quantityLabelEle.textContent = 'Quantity'

        const quantityInputEle = document.createElement('input')
        quantityInputEle.setAttribute('type', 'number')
        quantityInputEle.setAttribute('max', '5')
        quantityInputEle.setAttribute('min', '0')
        quantityInputEle.setAttribute('id', `item-quantity-${index}`)
        quantityInputEle.setAttribute('value', '0')

        quantityInputEle.addEventListener('input', () => {
            const orderSummary = document.getElementById('order-summary')
            const orderList = document.getElementById('order-list')
            const emptyOrder = orderSummary.getElementsByTagName('p')[0]

            if (orderList.hasChildNodes()) {
                emptyOrder.style.display = 'block'
            } else {
                emptyOrder.style.display = 'none'
            }

            if (isNaN(parseInt(quantityInputEle.value))) return

            const itemQuantity = quantityInputEle.value > 5 ? 5 : quantityInputEle.value
            const totalPrice = itemPrice * itemQuantity
            const formattedTotalPrice = USDollar.format(totalPrice)

            let order = document.getElementById(`order-number-${index}`)

            if (!order) {
                order = document.createElement('li')
                order.classList.add('order-form')
                order.setAttribute('id', `order-number-${index}`)
                order.textContent = `${itemName} (${itemQuantity} x ${formattedPrice} = ${formattedTotalPrice})`

                orderList.appendChild(order)
            }


            if (itemQuantity < 0) {
                orderList.removeChild(order)

            } else if (order) {
                itemsObjects["items"][item]['quantity'] = parseInt(itemQuantity)
                order.textContent = `${itemName} (${itemQuantity} x ${formattedPrice} = ${formattedTotalPrice})`
            }

        })

        itemContainerEle.appendChild(itemHeadingEle)
        itemContainerEle.appendChild(itemDescEle)
        itemContainerEle.appendChild(quantityLabelEle)
        itemContainerEle.appendChild(quantityInputEle)

        menuDiv.appendChild(itemContainerEle)
    })
}

function removeGifAndCreateMenuElements(items, createElementsAndDisplay) {
    createOrderSummaryList()

    const loader = document.getElementById('loader')
    loader.style.display = "none"

    itemsObjects = items
    createElementsAndDisplay(items.items)
}

fetch('http://localhost:8000/menu')
    .then(res => res.json())
    .then(res => removeGifAndCreateMenuElements(res, createElementsAndDisplay))

document.getElementById('order-form').addEventListener('submit', (e) => {
    e.preventDefault()

    const orderSummary = document.getElementById('order-summary')
    const orderList = document.getElementById('order-list')

    if (!orderList.hasChildNodes()) return
    const ob = {}
    const temp = []
    Object.keys(itemsObjects.items).forEach(itemKey => {
        if (itemsObjects.items[itemKey]['quantity'] > 0) {
            temp.push(itemsObjects.items[itemKey])
        }
    })

    ob["items"] = temp
    fetch('http://localhost:8000/orders',
        {
            method: "POST",
            headers: new Headers({'content-type': 'application/json'}),
            body: JSON.stringify(ob)
        }).then(res => res.json()).then(res => console.log(res))
})

const getLastOrder = document.getElementById('get-last-order-button')

const getDataFromJsonAsArr = (jsonData) =>{
    const arr = Object.keys(jsonData.items).map((dataKey) =>{
        const temp = [jsonData['items'][dataKey]]
        return arr.push(temp)
    })
    console.log(arr)

}
function displayMostRecentOrder(orderData) {
    const latestOrderInfo = document.getElementById('latest-order-info')
    getDataFromJsonAsArr(orderData)

}

getLastOrder.addEventListener('click', ()=>{
    fetch('http://localhost:8000/latest-order').then(res => res.json()).then(res => displayMostRecentOrder(res))

})