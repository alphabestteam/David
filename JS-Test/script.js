/*
List of endpoints:
  GET - http://localhost:8000/hello -> {'Hello': 'World'} Here as an example
  GET - http://localhost:8000/menu -> {'items': menu} A dict of the menu
  POST - http://localhost:8000/latest-order -> A dict of the latest order
  POST - http://localhost:8000/orders -> An endpoint to handle an order. The order is in the http body as so: { 'items': items }

*/

let itemsObjects = null
let USDollar = new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
});

createOrderSummaryList = () => {
    const orderSummary = document.getElementById('order-summary')
    const unorderedList = document.createElement('ul')

    unorderedList.setAttribute('id', 'order-list')
    orderSummary.appendChild(unorderedList)
}

createShoppingElementsAndDisplay = (items) => {
    const menuDiv = document.getElementById('menu')
    const itemKeys = Object.keys(items)

    itemKeys.forEach((item, index) => {
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


            if (isNaN(parseInt(quantityInputEle.value))) return

            const itemQuantity = quantityInputEle.value > 5 ? 5 : quantityInputEle.value
            const totalPrice = itemPrice * itemQuantity
            const formattedTotalPrice = USDollar.format(totalPrice)

            let orderedElement = document.getElementById(`order-number-${index}`)

            if (!orderedElement) {
                orderedElement = document.createElement('li')
                orderedElement.classList.add('order-form')
                orderedElement.setAttribute('id', `order-number-${index}`)
                orderedElement.textContent = `${itemName} (${itemQuantity} x ${formattedPrice} = ${formattedTotalPrice})`

                orderList.appendChild(orderedElement)
            }

            if (itemQuantity <= 0) {
                orderList.removeChild(orderedElement)
                itemsObjects["items"][item]['quantity'] = 0

            } else if (orderedElement) {
                itemsObjects["items"][item]['quantity'] = parseInt(itemQuantity)
                orderedElement.textContent = `${itemName} (${itemQuantity} x ${formattedPrice} = ${formattedTotalPrice})`
            }

            const emptyOrder = orderSummary.getElementsByTagName('p')[0]
            if (!orderList.hasChildNodes()) {
                emptyOrder.style.display = 'block'
            } else {
                emptyOrder.style.display = 'none'
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
    const loader = document.getElementById('loader')
    loader.style.display = "none"

    createOrderSummaryList()

    itemsObjects = items
    createElementsAndDisplay(items.items)
}

function displayMostRecentOrder(orderData) {
    const latestOrderInfoElement = document.getElementById('latest-order-info')

    const notFoundElement = latestOrderInfoElement.getElementsByTagName('p')[0]
    notFoundElement.style.display = 'none'

    let outerUlElement = document.getElementById('recent-order-list')
    if (!outerUlElement) {
        outerUlElement = document.createElement('ul')
        outerUlElement.setAttribute('id', 'recent-order-list')
    } else {
        outerUlElement.innerHTML = ""
    }

    latestOrderInfoElement.appendChild(outerUlElement)
    orderData["items"].sort((a, b) => b.price - a.price)

    Object.keys(orderData["items"]).forEach(key => {

        const currItem = orderData["items"][key]
        const name = currItem.name
        const price = USDollar.format(currItem.price)
        const description = currItem.description
        const quantity = currItem.quantity
        const id = currItem.id

        const outerLiElement = document.createElement('li')
        outerLiElement.textContent = `${name}`

        const innerUlElement = document.createElement('ul')

        const liPrice = document.createElement('li')
        const liDesc = document.createElement('li')
        const liQuantity = document.createElement('li')
        const liId = document.createElement('li')


        liPrice.textContent = `price: ${price}`
        liDesc.textContent = `description: ${description}`
        liQuantity.textContent = `quantity: ${quantity}`
        liId.textContent = `ID: ${id}`

        innerUlElement.appendChild(liPrice)
        innerUlElement.appendChild(liDesc)
        innerUlElement.appendChild(liQuantity)
        innerUlElement.appendChild(liId)

        outerLiElement.appendChild(innerUlElement)
        outerUlElement.appendChild(outerLiElement)
    })


}

noOrdersInOrderList = () => {
    const orderList = document.getElementById('order-list') // Was created at the beginning of the code
    return !orderList.hasChildNodes()
}
sendOutOrder = () => {

    if (noOrdersInOrderList()) return

    const orderObject = {}
    const orderArray = []
    Object.keys(itemsObjects["items"]).forEach(itemKey => {
        if (itemsObjects.items[itemKey]['quantity'] > 0) {
            orderArray.push(itemsObjects.items[itemKey])
        }
    })

    orderObject["items"] = orderArray
    fetch('http://localhost:8000/orders',
        {
            method: "POST",
            headers: new Headers({'content-type': 'application/json'}),
            body: JSON.stringify(orderObject)
        }).then(res => res.json()).then(res => console.log(res))
}


fetch('http://localhost:8000/menu')
    .then(res => res.json())
    .then(res => removeGifAndCreateMenuElements(res, createShoppingElementsAndDisplay));


const orderForm = document.getElementById('order-form')
orderForm.addEventListener('submit', (e) => {
    e.preventDefault()
    sendOutOrder()
})

const getLastOrderBtn = document.getElementById('get-last-order-button')

async function getLastOrder() {
    const res = await fetch('http://localhost:8000/latest-order')

    if (!res.ok) {
        console.log("An error occurred while trying to get last order", res.status)
    }
    const lastOrder = await res.json()
    displayMostRecentOrder(lastOrder)
}

getLastOrderBtn.addEventListener('click', getLastOrder)
