const changeColor = function(element) {
    element.querySelector('.js-icon').classList.toggle("active")
}



const frontend_base_url = "http://127.0.0.1:5500/templates"
const backend_base_url = "http://127.0.0.1:8000"

const urlParameter = window.location.search;
var winedata_id = urlParameter.split('=')[1]
console.log(winedata_id)

window.onload = async function testbutton(){
    const response = await fetch(`${backend_base_url}/detail/${winedata_id}/`, {
          headers:{
              'content-type':'application/json',
          },
          method:'GET',
    })

    

    var payload = localStorage.getItem("payload")
    var parsed_payload = await JSON.parse(payload)
    
  

    const response_user = await fetch(`${backend_base_url}/user/profile/`, {
      headers:{
          'content-type':'application/json',
          "Authorization": "Bearer " + localStorage.getItem("access")
      },
      method:'GET',
    })
    
    response_user_json=await response_user.json()
    console.log(response_user_json)

    const userImage =document.getElementById("user-img")
    userImage.setAttribute("src", response_user_json.profile)


    console.log(parsed_payload)

    response_json=await response.json()
    page_data = response_json
    comment_data = page_data.review_set
    

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
                                <div class = "button-container" id="bookmark-button" style="display:none;">
                                  <button type = "button" class="button__dark js-button" id= "button_dark" onclick="bookmark(${page_data.id})">
                                    <ion-icon name="bookmark" class="icon__dark js-icon" onclick=""></ion-icon>
                                    Bookmark
                                  </button>
                                </div>
                            </div>
                        </div>`
    search.prepend(winedata)
    console.log(page_data.name)

    const comment_put =document.getElementById("commment")


    comment_data.forEach(element => {
      const comment_user = document.createElement("div")
      
      comment_user.innerHTML=`
                              <!-- Comment - Dummy -->
                              <div class="comment">
                                <!-- Comment Avatar -->
                                <div class="comment-avatar">
                                  <img src=${element.username.profile} style="height:100%">
                                </div>

                                <!-- Comment Box -->
                                <div class="comment-box" >
                                  <div class="comment-text">${element.Review}</div>
                                    <div class="comment-footer">
                                      <div class="comment-info">
                                        <span class="comment-author">
                                          <a>${element.username.profilename}</a>
                                        </span>
                                        <span class="comment-date">${element.created_time}</span>
                                        <span>${element.grade}</span>
                                      </div>
                                      <div class="comment-actions" id="edit-button">
                                        <a onclick="commentUpdate(${element.id})">Edit</a>
                                        <span>/</span>
                                        <a onclick="commentDelete(${page_data.id},${element.id})">delete</a>
                                      </div>

                                    </div>
                                  </div>
                                </div>
                              `
        comment_put.prepend(comment_user)
        const editButton = document.getElementById("edit-button")
        if(parsed_payload.user_id == element.username.id){
          editButton.setAttribute("style", "display:flex;")
        }
        else{
          editButton.setAttribute("style", "display:none;")
        }
      });

    const commentbox = document.getElementById("comment-put")
    const bookmarkButton = document.getElementById("bookmark-button")

    if(parsed_payload){
      commentbox.setAttribute("style", "display:block;")
      commentbox.setAttribute("style", "display:block;")
      bookmarkButton.setAttribute("style", "display:flex;")

    }
    else{
      commentbox.setAttribute("style", "display:none;")
      bookmarkButton.setAttribute("style", "display:none;")
      
    }


    // 북마크 UI 기능
    user_id = parsed_payload.user_id
    bookmarklist = page_data.bookmark

    test = bookmarklist.indexOf(user_id)
    
    if(test == -1){
      const bookmark_button = document.getElementById("button_dark")
      bookmark_button.setAttribute("style", "color:gray; background-color:white;")
    }
    else{
      const bookmark_button = document.getElementById("button_dark")
      bookmark_button.setAttribute("style", "color:#6b0909; background-color:gray;")
    }

}

async function addcommend(){
    const comment = document.getElementById("comment_input").value;
    const grade = document.getElementById("grade_input").value;
    console.log(comment, grade);

    const response = await fetch(`${backend_base_url}/detail/${winedata_id}/`, {
      headers:{
      "content-type": "application/json",
      "Authorization": "Bearer " + localStorage.getItem("access")
      },
      method: "POST",
      body: JSON.stringify({
          "Review": comment,
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

async function bookmark(winedata_id){

  const response = await fetch(`${backend_base_url}/detail/${winedata_id}/bookmark/`, {
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

async function commentUpdate(review_id){
  alert("수정버튼 눌림")

}

async function commentDelete(Winedata_id,Review_id){
  console.log(Winedata_id)
  console.log(Review_id)
  const response = await fetch(`${backend_base_url}/detail/${Winedata_id}/${Review_id}/`, {
    headers:{
    "content-type": "application/json",
    "Authorization": "Bearer " + localStorage.getItem("access")
    },
    method: "Delete",
    
  })
  if (response.status == 200){
    alert("댓글을 삭제 했습니다.")
    }
  else{
    alert(response.status)
  }

}