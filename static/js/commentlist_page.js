window.onload = () => {
    console.log('댓글리스트 페이지 요청됨')
    getCommentList().then()
}


async function getCommentList() {
    const response = await fetch(`${backend_base_url}/user/review/`, {

        headers: {
            'Authorization': 'Bearer ' + localStorage.getItem('access')
        },
        method: "GET",
    })
    comment_data = await response.json()
    frame = document.getElementById('comments')
    comment_data.forEach(element => {
        const comment = document.createElement('div')
        comment.innerHTML = `<li class="list-group-item">
                                <div class="comment-box">
                                    <div class="comment">

                                        <a href='${frontend_base_url}/detail.html?id=${element.winedata}'><p>${element.review}</p></a>

                                    </div>
                                    <div class="progress">
                                        <div class="progress-bar" role="progressbar" aria-label="Example with label"
                                            style="width: ${element.grade}%;">${element.grade}%</div>
                                    </div>
                                </div>
                            </li>`
        frame.appendChild(comment)
    })
}
