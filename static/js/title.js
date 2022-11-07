window.onload = async function checkLogin(){
    var payload = localStorage.getItem("payload")
    var parsed_payload = await JSON.parse(payload)

    const loginoutUl = document.getElementById("loginout")

    if(parsed_payload){
        console.log(2)
        loginoutUl.innerText="logout"
        loginoutUl.setAttribute("onclick", "handleLogout()")
    }
    else{
        console.log('3')
        loginoutUl.innerText="login"
        loginoutUl.setAttribute("href", "../templates/signin.html")
    }
}

async function handleLogout(){
    localStorage.removeItem("access")
    localStorage.removeItem("refresh")
    localStorage.removeItem("payload")
    alert("로그아웃되었습니다.")
    location.reload()
}
