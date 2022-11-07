window.onload = ()=>{
    console.log("load")


    show_tag_fuc() // backend에서 tag 가져오기
    all_name = new Array(); // 전체 테그 담을 리스트 선언

}   

// async function show_tag_fuc() {
//     const response = await fetch('http://127.0.0.1:8000/', {
//         headers:{
//             'content-type':'application/json',
//         },
//         method:'GET',
//     })
//     .then(response => { 
//         return response.json();
//       })
//     .then(data => {
//         var wines= document.getElementById("wine");
//         for (i=0; i < data.length; i++){
//             const temp_html=`
//                     <div class="card h-100">
//                         <a href="${data[i]['id']}">
//                         <img style="max-width: 150; height: 150;" src="${data[i]['image']}"
//                             class="card-img-top" alt="..." id="image" > </a>
//                         <div class="card-body" id="winebody">
//                             <h5 class="card-title" id="name">${data[i]['name']}</h5>
//                             <p class="card-text" id="content">${data[i]['id']}</p>
//                         </div>
//                     </div>
//                 </div>
//                 </div>`;
//             const temp=document.createElement('div');
//             temp.className="col";
//             temp.innerHTML=temp_html;
//             wines.appendChild(temp);
//         }
//     });
// }



