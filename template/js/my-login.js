

window.onload = () => {
    console.log("로딩 굿")
}

const frontend_base_url = "http://127.0.0.1:5500/template"
const backend_base_url = "http://127.0.0.1:8000"

async function loginissue() {
    const username = document.getElementById("username").value
    const password = document.getElementById("password").value
    console.log(username, password)

    const response = await fetch('http://127.0.0.1:8000/user/api/token/', {
        headers:{
        "content-type": "application/json",
        },
        method: "POST",
        body: JSON.stringify({
            "username": username,
            "password": password
        })
    })
    console.log(response)

    const response_json = await response.json() //** 우리가 읽을 수 있고. 원하는 형태인 json형태로 바꾸어 줌! */
    console.log(response_json.access)
    localStorage.setItem("access", response_json.access);
    localStorage.setItem("refresh", response_json.refresh);

    const base64Url = response_json.access.split('.')[1];
    const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    const jsonPayload = decodeURIComponent(atob(base64).split('').map(function(c){
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
    }).join(''));

    localStorage.setItem("payload", jsonPayload);

    if (response.status == 200){
		alert(response.status)
		console.log(response)
        window.location.replace(`${frontend_base_url}/main.html`);
    }
	else{
		alert(response.status)
	}


}

async function signupissue() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const password2 = document.getElementById("password2").value;
    const email = document.getElementById("email").value;
    const profilename = document.getElementById("profilename").value;
    console.log(username, password, profilename, email);
	
    const response = await fetch(`${backend_base_url}/user/signup/`, {
        headers:{
        "content-type": "application/json",
        },
        method: "POST",
        body: JSON.stringify({
            "username": username,
            "password": password,
            "password2": password2,
            "email": email,
            "profilename": profilename

        })
    })

    if (response.status == 201){
		alert(response.status)
        window.location.replace(`${frontend_base_url}/signin.html`);
    }
	else{
		alert(response.status)
	}
    
}


