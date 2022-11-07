const urlParameter = window.location.search;
var searchData = urlParameter.split('=')[1]


window.onload = async function test(){
    const response = await fetch(`http://127.0.0.1:8000/search/?search=${searchData}`,{
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
                    <div class="card h-100">
                        <a href="${data[i]['id']}">
                        <img style="max-width: 150; height: 150;" src="${data[i]['image']}"
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
    




async function searchclick(){
    var inputvalue = document.getElementById('Search').value;
    const url=`http://127.0.0.1:5000/Frontend/template/search.html?search=${inputvalue}`
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



// response_json=await response.json()
//     console.log(response_json)
//     const search =document.getElementById("search")
//     var wines= document.getElementById("wine");
//     response_json.forEach(element => {
//         const temp_html=`
//                     <div class="card h-100">
//                         <a onclick="location.href="${element.id}">
//                         <img style="max-width: 150; height: 150;" src="${element.image}"
//                             class="card-img-top" alt="..." id="image" > </a>
//                         <div class="card-body" id="winebody">
//                             <h5 class="card-title" id="name">${element.name}</h5>
//                             <p class="card-text" id="content">${element.content}</p>
//                         </div>
//                     </div>
//                 </div>
//                 </div>`;
//             const temp=document.createElement('div');
//             temp.className="col";
//             temp.innerHTML=temp_html;
            
//             // wines.appendChild(temp);

        
//     });
//     console(element.id)

// }
