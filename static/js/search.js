console.log("서치html접속")
window.onload =async function (){
    const response=await fetch("http://127.0.0.1:8000/tweetlist/", {method:"GET"})

    response_json = await response.json()
    // console.log(response_json)

    const search =document.getElementById("search")
    response_json.forEach(element => {
        // console.log(element.name)
        const newsearch = document.createElement("div")
        newsearch.innerHTML=element.name
        search.appendChild(newsearch)
        
    });
    

}

async function searchclick(){
    console.log("Search 함수실행")
    var inputvalue = document.getElementById('Search').value;
    console.log(inputvalue)
    console.log('http://127.0.0.1:8000/search/?search=${inputvalue}')
    const response = await fetch(`http://127.0.0.1:8000/search/?search=${inputvalue}`,{
        headers:{'content-type':'application/json',
    },
    method:"GET",
    
})

    response_json=await response.json()
    console.log(response_json)
    const search =document.getElementById("search")
    response_json.forEach(element => {
        // console.log(element.name)
        const newsearch = document.createElement("div")
        newsearch.innerHTML=element.name
        // search.remove();
        // search.replaceWith(newsearch)
        search.prepend(newsearch)
    
});

}
function enterkey() {
    if (window.event.keyCode == 13){
        searchclick()
    }
}