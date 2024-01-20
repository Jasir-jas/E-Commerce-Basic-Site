
let updateBtn = document.getElementsByClassName('update-cart')

for(let i = 0; i < updateBtn.length; i++){
    updateBtn[i].addEventListener('click', function () {
        let productId = this.dataset.product;
        let action = this.dataset.action;
        console.log('productId :',productId, 'action:',action);
        console.log('USER:',user);
        if(user === 'AnonymousUser'){
            addCookieItem(productId,action)
        }else{
            UpdateUserOrder(productId,action);
        }
    })   
}

// items are stored in cookies if user not loggin
function addCookieItem(productId,action){
    console.log('user is not logged in..');

    if( action == 'add' ){
        if(cart[productId] == undefined){
            cart[productId] = {'quantity': 1}
        }else{
            cart[productId] ['quantity'] += 1
    }
    }

    if( action == 'remove' ){
        cart[productId] ['quantity'] -= 1

        if( cart[productId] ['quantity'] <= 0){
            console.log('Remove item');
            delete cart[productId]
        }
    }
    console.log('Cart:',cart);
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
    location.reload()
}


// user click button update orders..
function UpdateUserOrder(productId,action){
    console.log('user logged in.sending data...');

    let url = '/update_items/'

    fetch(url,{
        method:'POST',

        // sending data
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },

        // mode: 'same-origin',

        // send data
        body: JSON.stringify({
            'productId': productId,
            'action': action,
        })
    })

    // promise method
    .then((response) => {
        return response.json()
    })

    .then((data) => {
        console.log('data:',data);
        location.reload()
    })
}


