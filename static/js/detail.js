const changeColor = function(element) {
    element.querySelector('.js-icon').classList.toggle("active")
}

// window.onload = async function checkLogin(){
  
//     console.log("load")


//     show_tag_fuc() // backend에서 tag 가져오기
//     all_name = new Array(); // 전체 테그 담을 리스트 선언

    


// }

const frontend_base_url = "http://127.0.0.1:5500/templates"
const backend_base_url = "http://127.0.0.1:8000"

const urlParameter = window.location.search;
var wine_id = urlParameter.split('=')[1]

window.onload = async function testbutton(){

    

    const response = await fetch(`${backend_base_url}/detail/${wine_id}/`, {
          headers:{
              'content-type':'application/json',
          },
          method:'GET',
    })

    var payload = localStorage.getItem("payload")
    var parsed_payload = await JSON.parse(payload)

    console.log(parsed_payload)



    response_json=await response.json()
    page_data = response_json
    comment_data = page_data.comment_set
    console.log(page_data)
    console.log(comment_data)

    const search =document.getElementById("content")
    const winedata = document.createElement("div")

    

    winedata.innerHTML=`<div class="demo-area">
                            <img class="demo-trigger" src=${page_data.image}>
                            <div class="detail">
                                <section>
                                    <h3>${page_data.name}</h3>
                                    <p>tag : ${page_data.tag}</p>
                                    <p>description : ${page_data.content}</p>
                                    <p>contry : ${page_data.country}</p>
                                </section>
                                <div class = "button-container">
                                  <button type = "button" class="button__dark js-button" onclick="bookmark(${page_data.id})">
                                    <ion-icon name="bookmark" class="icon__dark js-icon" onclick=""></ion-icon>
                                    Bookmark
                                  </button>
                                </div>
                            </div>
                        </div>`
    search.prepend(winedata)

    const comment_put =document.getElementById("commment")
    const comment_user = document.createElement("div")


    comment_data.forEach(element => {
      const comment_user = document.createElement("div")
      
      comment_user.innerHTML=`
                              <!-- Comment - Dummy -->
                              <div class="comment">
                                <!-- Comment Avatar -->
                                <div class="comment-avatar">
                                  <img src=${element.username.profile}>
                                </div>

                                <!-- Comment Box -->
                                <div class="comment-box" >
                                  <div class="comment-text">${element.comment}</div>
                                    <div class="comment-footer">
                                      <div class="comment-info">
                                        <span class="comment-author">
                                          <a>${element.username.profilename}</a>
                                        </span>
                                        <span class="comment-date">${element.created_time}</span>
                                      </div>
                            
                                      <div class="comment-actions">
                                        <span>${element.grade}</span>
                                        <a>Reply</a>
                                      </div>

                                    </div>
                                  </div>
                                </div>
                              `
        comment_put.prepend(comment_user)
      });




}

async function addcommend(){
    const comment = document.getElementById("comment_input").value;
    const grade = document.getElementById("grade_input").value;
    console.log(comment, grade);

    const response = await fetch(`${backend_base_url}/detail/${wine_id}/`, {
      headers:{
      "content-type": "application/json",
      "Authorization": "Bearer " + localStorage.getItem("access")
      },
      method: "POST",
      body: JSON.stringify({
          "comment": comment,
          "grade": grade
      })
  })

  if (response.status == 201){
		alert(response.data)
    }
	else{
		alert(response.status)
	}



}

async function bookmark(wine_id){

  const response = await fetch(`${backend_base_url}/detail/${wine_id}/bookmark/`, {
    headers:{
    "content-type": "application/json",
    "Authorization": "Bearer " + localStorage.getItem("access")
    },
    method: "POST",
    
  })
  if (response.status == 200){
    alert(response.data)
    }
  else{
    alert(response.status)
  }




}