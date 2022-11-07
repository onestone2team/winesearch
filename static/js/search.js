const urlParameter = window.location.search;
var searchData = urlParameter.split('=')[1]

const frontend_base_url = "http://127.0.0.1:5500/templates"
const backend_base_url = "http://127.0.0.1:8000"

let pageNum = 1

window.onload = async function test(){

    

    const response = await fetch(`${backend_base_url}/search/?search=${searchData}&page=${pageNum}`,{
        headers:{
            'content-type':'application/json',
        },
        method:"GET",
    })  
    .then(response => { 
        return response.json();
      })
    .then(data => {
        var wines= document.getElementById("wine");
        for (i=0; i < data.length; i++){
            const temp_html=`
                    <div class="card h-100" id = "wine_view">
                        <a href="detail.html?id=${data[i]['id']}">
                        <img style="width: 200px; height: 300px;" src="${data[i]['image']}"
                            class="card-img-top" alt="..." id="image" > </a>
                        <div class="card-body" id="winebody">
                            <h5 class="card-title" id="name">${data[i]['name']}</h5>
                            <p class="card-text" id="content">${data[i]['id']}</p>
                        </div>
                    </div>
                </div>
                </div>`;
            const temp=document.createElement('div');
            temp.className="col";
            temp.innerHTML=temp_html;
            wines.appendChild(temp);
        }
    });
}

async function searchpageMove(){
    const response = await fetch(`${backend_base_url}/search/?search=${searchData}&page=${pageNum}`,{
        headers:{
            'content-type':'application/json',
        },
        method:"GET",
    })  
    .then(response => { 
        return response.json();
      })
    .then(data => {
        var wines= document.getElementById("wine");
        while (wines.hasChildNodes()) {
            wines.removeChild(wines.firstChild);
        }
        

        for (i=0; i < data.length; i++){
            const temp_html=`
                    <div class="card h-100" id = "wine_view">
                        <a href="detail.html?id=${data[i]['id']}">
                        <img style="width: 200px; height: 300px;" src="${data[i]['image']}"
                            class="card-img-top" alt="..." id="image" > </a>
                        <div class="card-body" id="winebody">
                            <h5 class="card-title" id="name">${data[i]['name']}</h5>
                            <p class="card-text" id="content">${data[i]['id']}</p>
                        </div>
                    </div>
                </div>
                </div>`;
            
            const temp=document.createElement('div');
            temp.className="col";
            temp.innerHTML=temp_html;
            wines.appendChild(temp);
        }
    });
    console.log(pageNum)
}
    

function pageNext(){
    ++pageNum
    searchpageMove()

    
}

async function pagePreview(){
    --pageNum
    searchpageMove()
}




async function searchclick(){
    var inputvalue = document.getElementById('Search').value;
    const url=`${frontend_base_url}/search.html?search=${inputvalue}`
    location.href=url
    

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
