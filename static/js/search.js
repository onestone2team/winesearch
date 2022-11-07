console.log("서치html접속")
window.onload = ()=>{
    console.log("load")


    show_tag_fuc() // backend에서 tag 가져오기
    all_name = new Array(); // 전체 테그 담을 리스트 선언

}   

async function show_tag_fuc() {
    const response = await fetch('http://127.0.0.1:8000/tweetlist/', {
        headers:{
            'content-type':'application/json',
        },
        method:'GET',
    })
    // backend에서 받은 데이터 가져오기
    .then(response => { 
        return response.json();
      })
    // Promise 안에 담긴 데이터 꺼내오기
    .then(data => {

        // console.log(data) // tag 목록 확인
        var names= document.getElementById("all_names");
        for (i=0; i < data.length; i++){
            const name = document.createElement("button"); // 버튼 요소 생성
            name.setAttribute("class","mylabel") // css class 지정
            name.setAttribute("onclick","nameclick(this.innerText)") // 선택한 버튼 클릭 시 해당 함수 호출
            name.innerText = data[i]['name'] // 버튼이름 값 지정
            const names = all_names.appendChild(name) // all_name 안에 tag 추가
            // console.log(names)
        }
    });
}

async function searchclick(){
    console.log("Search 함수실행")
    var inputvalue = document.getElementById('Search').value;
    console.log("검색한 단어는"+inputvalue)
    // console.log('http://127.0.0.1:8000/search/?search=${inputvalue}')
    const response = await fetch(`http://127.0.0.1:8000/search/?search=${inputvalue}`,{
        headers:{'content-type':'application/json',
    },
    method:"GET",
    
})

    response_json=await response.json()
    // console.log(response_json)
    const search =document.getElementById("search")
    response_json.forEach(element => {
        // console.log(element.name)
        const newsearch = document.createElement("div")
        newsearch.innerHTML=`<div class="container">
                            <li>이름:${element.name}</li>`
                            // +`<li>소개:${element.content}</li>`
                            // +`<li>종류:${element.tag}</li>`
                            // +`<li>국가:${element.country}</li>`
                            +`<li><a  href="${element.id}"><img src="${element.image}"></a></li>
                            </div>`
        search.prepend(newsearch)

    
});

}
function enterkey() {
    if (window.event.keyCode == 13){
        searchclick()
    }
}

// tag 버튼 값 가져오기
async function nameclick(val) {
    nameclick(val);   
}


// 테그들 목록 백엔드로 POST 전달 <확인버튼>
async function nameclick() {
    // var str = ""
    // for (i=0; i < all_name.length; i++) {
    //     if (i == all_name.length-1) {
    //         str += all_name[i]
    //     }
    //     else {
    //         str += all_name[i]+","
    //     }
    // }
    console.log(all_name)
    const response = await fetch('http://127.0.0.1:8000/tweetlist/', {

        headers:{
            'content-type':'application/json',
        },
        method:'POST',
        body: JSON.stringify({

            "name":str
        })
    })
    const response_json = await response.json();
    return response_json

}