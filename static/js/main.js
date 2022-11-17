window.onload = () => {
    console.log("load")


    show_tag_fuc() // backend에서 tag 가져오기
    all_name = new Array(); // 전체 테그 담을 리스트 선언

}


async function show_tag_fuc() {
    const response = await fetch(`${backend_base_url}/?page=${pageNum}`, {
        headers: {
            'content-type': 'application/json',
        },
        method: 'GET',
    })
        .then(response => {
            return response.json();
        })
        .then(data => {
            var wines = document.getElementById("wine");
            for (i = 0; i < data["data"].length; i++) {
                const temp_html = `
                    <div class="card h-100">
                        <a href="detail.html?id=${data["data"][i]['id']}">
                        <img style="max-width: 150; height: 150;" src="${data["data"][i]['image']}"
                            class="card-img-top wine-image" alt="..." id="image" > </a>
                        <div class="card-body" id="winebody">
                            <h5 class="card-title" id="name">${data["data"][i]['name']}</h5>
                        </div>
                    </div>`;
                const temp = document.createElement('div');
                temp.className = "col";
                temp.innerHTML = temp_html;
                wines.appendChild(temp);
                total_page = data["max_page"]
            }
        });
}

async function mainpageMove() {
    const response = await fetch(`${backend_base_url}/?page=${pageNum}`, {
        headers: {
            'content-type': 'application/json',
        },
        method: "GET",
    })
        .then(response => {
        return response.json();
        })
        .then(data => {
            var wines = document.getElementById("wine");
            while (wines.hasChildNodes()) {
                wines.removeChild(wines.firstChild);
            }
            for (i = 0; i < data["data"].length; i++) {
                const temp_html = `
                    <div class="card h-100" id = "wine_view">
                        <a href="detail.html?id=${data["data"][i]['id']}">
                        <img style="width: 200px; height: 300px;" src="${data["data"][i]['image']}"
                            class="card-img-top" alt="..." id="image" > </a>
                        <div class="card-body" id="winebody">
                            <h5 class="card-title" id="name">${data["data"][i]['name']}</h5>
                        </div>
                    </div>`;

                const temp = document.createElement('div');
                temp.className = "col";
                temp.innerHTML = temp_html;
                wines.appendChild(temp);
            }
        });
}

function pageNext1() {
    if (pageNum > 0 && pageNum < total_page) {
        ++pageNum
        mainpageMove()
    }
}

function pagePreview1() {
    if (pageNum > 1) {
        --pageNum
        mainpageMove()
    }
}