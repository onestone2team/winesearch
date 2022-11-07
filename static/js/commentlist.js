console.log("자바스크립트 불러왔음!!")



window.onload = async function loadComment(){
    const response = await fetch('http://127.0.0.1:8000/user/review/', {
        headers:{'content-type':'application/json',
                 'Authorization': 'Bearer ' + localStorage.getItem('access')
    },

        method: "GET",

    })

   

    const review = document.getElementById("comment")

    response_json.forEach(element => {
        const newComment = document.createElement("div")
                    newComment.innerHTML = `<li class="list-group-item">
                                            <div class="comment-box">
                                                <div class="comment">
                                                    <p>${element.comment}</p>
                                                </div>
                                                <div class="progress">
                                                <div class="progress-bar" role="progressbar" aria-label="Example with label"
                                                        style="width:${element.grade}">${element.grade}</div>
                                                </div>
                                            </div>
                                        </li>`
        review.appendChild(newComment)  
            
    });

      
}