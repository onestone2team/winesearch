window.onload = () => {
    console.log('추천리스트 페이지 요청됨')
    getBookmarkList()
}

async function getBookmarkList() {
    const response = await fetch(`${backend_base_url}/recommend/`, {
        headers: {
            'Authorization': 'Bearer ' + localStorage.getItem('access')

        },
        method: "GET",
    })
    
    bookmark_data = await response.json()
    frame = document.getElementById('bookmarks')
    bookmark_data.forEach(element => {
        const bookmark = document.createElement('div')
        bookmark.innerHTML = `<div class="col"style="height:400px">
                                    <div class="card h-100" >
                                        <a href="${frontend_base_url}/detail.html?id=${element.id}">
                                            <img src=${element.image} class="card-img-top" alt="..." style="height:250px">
                                        </a>
                                        <div class="card-body">
                                            <h5 class="card-title">${element.name}</h5>
                                        </div>
                                    </div>
                                </div>`
        frame.appendChild(bookmark)
    })
}
