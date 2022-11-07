window.onload = () => {
    console.log('북마크리스트 페이지 요청됨')
    getBookmarkList()
    // const url = window.location.href
    // console.log(url) 
    // http://127.0.0.1:5500/templates/bookmarklist.html#
}


async function getBookmarkList() {
    const response = await fetch("http://127.0.0.1:8000/recommend/", {
        headers: {
            'Authorization': 'Bearer ' + localStorage.getItem('access')
        
        },
        method: "GET",
    })
    
    bookmark_data = await response.json()
    frame = document.getElementById('bookmarks')
    bookmark_data.forEach(element =>{
    const bookmark = document.createElement('div')
            bookmark.innerHTML = `<div class="col"style="height:400px">
                                    <div class="card h-100" >
                                        <a href="http://127.0.0.1:5500/templates/detail.html?id=${element.tweet.id}">
                                          <img src=${element.tweet.image} class="card-img-top" alt="..." style="height:250px">
                                        </a>
                                        <div class="card-body">
                                            <h5 class="card-title">${element.tweet.name}</h5>
                                        </div>
                                    </div>
                                  </div>` 
    frame.appendChild(bookmark)
    })   
}
