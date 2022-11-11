
window.onload = async function ViewProfile() {

    var payload = localStorage.getItem("payload")
    var parsed_payload = await JSON.parse(payload)

    const response_user = await fetch(`${backend_base_url}/user/profile/`, {
        headers: {
            'content-type': 'application/json',
            "Authorization": "Bearer " + localStorage.getItem("access")
        },
        method: 'GET',
    })

    response_user_json = await response_user.json()
    console.log(response_user_json)

    const element = document.getElementById("username");
    const content = document.createTextNode(response_user_json.username);
    element.appendChild(content);

    // const username = document.getElementById("username")
    // username.setAttribute("text", response_user_json.username)
    const profilename = document.getElementById("profilename")
    profilename.setAttribute("value", response_user_json.profilename)
    const email = document.getElementById("email")
    email.setAttribute("value", response_user_json.email)
    const profileImage = document.getElementById("preview")
    profileImage.setAttribute("src", response_user_json.profile)
    console.log("로딩 굿")
}


async function updateuser() {
    // const password = document.getElementById("password").value;
    // console.log(password)
    // const password2 = document.getElementById("password2").value;
    // const email = document.getElementById("email").value;
    // const profilename = document.getElementById("profilename").value;
    // const profile = document.querySelector("input[type='file']");
    // console.log(password, profilename, email, profile);

    // var payload = localStorage.getItem("payload")
    // var parsed_payload = await JSON.parse(payload)


    const password = document.getElementById("password").value;
    const password2 = document.getElementById("password2").value;
    const email = document.getElementById("email").value;
    const profilename = document.getElementById("profilename").value;
    const profile = document.querySelector("input[type='file']");

    let formData = new FormData();
    formData.append("password", password);
    formData.append("password2", password2);
    formData.append("email", email);
    formData.append('profile', profile.files[0]);
    formData.append("profilename", profilename);
    console.log(formData);

    fetch(`${backend_base_url}/user/profile/`, {
        headers: {
            "Authorization": "Bearer " + localStorage.getItem("access")
        },
        method: "PUT",
        body: formData,
    })

    // const response = await fetch(`${backend_base_url}/user/profile/`, {
    //     headers:{
    //     "content-type": "application/json",
    //     "Authorization": "Bearer " + localStorage.getItem("access")
    //     },
    //     method: "PUT",
    //     body: JSON.stringify({
    //         "password": password,
    //         "password2": password2,
    //         "email": email,
    //         "profilename": profilename,
    //         "profile":profile

    //     })
    // })

    // if (response.status == 200){
    // 	alert(response.status)
    //     window.location.replace(`${frontend_base_url}/profile.html`);
    // }
    // else{
    // 	alert(response.status)
    // }

}