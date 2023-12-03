
let updateBtn = document.getElementsByClassName('update-cart')

for(let i = 0; i < updateBtn.length; i++){
    updateBtn[i].addEventListener('click', function () {
        let productId = this.dataset.product;
        let action = this.dataset.action;
        console.log('productId :',productId, 'action:',action);
        console.log('USER:',user);
        if(user === 'AnonymousUser'){
            console.log('user not logged in');
        }else{
            UpdateUserOrder(productId,action);
        }
    })   
}

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


