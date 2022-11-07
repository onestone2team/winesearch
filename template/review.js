console.log("자바스크립트 불러왔음!!")



window.onload = async function loadComment(){
    const response = await fetch('http://127.0.0.1:8000/detail/', {method:'GET'})

    response_json = await response.json()

    console.log(response_json)

    const review = document.getElementById("review")

    response_json.forEach(element => {
        const newComment = document.createElement("review")
        newComment.innerText = element.comment
        review.appendChild(newComment)

    });


}