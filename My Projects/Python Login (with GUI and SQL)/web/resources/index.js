const dateSpan = document.getElementById('dateSpan')
let email = document.getElementById('email')
let password = document.getElementById('password')
let btn = document.getElementById('submit')
let feedHub = document.getElementsByClassName('feed')


window.addEventListener("load", function(){
    const loaderBody = document.getElementById("loader-body")
    loaderBody.className += " loader-hidden"
})

//user login
function btnlogin(){
    let username = email.value
    let userpassword = password.value

    eel.btnLogin(username, userpassword)
}

eel.expose(login_return)
function login_return(status){
    if (status == 'success'){
        location.href = './admin.html'
    }
    else {
        feedHub.classList.add('show')
        setTimeout(function(){
            feedHub.classList.remove('show')
        }, 3000)
    }
}



btn.addEventListener('click', btnlogin())




;