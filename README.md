  # ๐ฉ project WineSearch 
  ## ๐ฉโ๐ป A2 ์ผ์์ด์กฐ

   ![image](https://i.ibb.co/CsrNLm5/unnamed.jpg)
  <p>
      <img src="https://img.shields.io/badge/Django-4.1.1-green"/>
  </p>

  ### ๐ท ์๊ฐ
  - ์ ์ ์ ์ทจํฅ์ ๋ง๋ ์์ธ์ ์ถ์ฒํด์ฃผ๋ ์ฌ์ดํธ
  - ๋ธ์ https://www.notion.so/S-A-1babf1e770e14575b9df9008e6c5e5c9
  
  ### ๐ท ์ฌ์ฉํ ๋ฐ์ดํฐ์ ๋ชจ๋ธ
  - https://www.kaggle.com/datasets/zynicide/wine-reviews
  
  ### ๐ท ์ฃผ์ ๊ธฐ๋ฅ 
  - ##### ์ฐพ๊ณ ์ถ์ ์์ธ ๊ฒ์
  - ##### ๋จน์ด๋ณธ ์์ธ์ ๋ํ ํ์  ๋ฐ ๋ฆฌ๋ทฐ ์์ฑ
  - ##### ์์ฑํ ํ์  ๋ฐ ๋ฆฌ๋ทฐ ๋ชจ์๋ณด๊ธฐ
  - ##### ์ทจํฅ์ ๋ง๋ ์์ธ ๋ถ๋งํฌํ๊ธฐ
  - ##### ๋ถ๋งํฌํ ์์ธ ๋ชจ์๋ณด๊ธฐ
  - ##### ์ ํธํ๋ ์์ธ ๋ฐ์ดํฐ๋ฅผ ๊ธฐ๋ฐ์ ์ถ์ฒ ์์คํ
  
  
  ***


  ### ๐ท ๊ฐ๋ฐ ์ผ์ 
  
  **์งํ๊ธฐ๊ฐ** 2022๋ 11์ 2์ผ ~ 2022๋ 11์ 8์ผ

  **11์ 2~3์ผ** S.A ๋ด์ฉ ์์ฑ,์์ด์ด ๋ฐ์ดํฐ ๋ฒ ์ด์ค ๋ถ๋ฌ์ค๊ธฐ 

  **11์ 3~4์ผ** ํ์๊ฐ์,๋ก๊ทธ์ธ,ํ์์ ๋ณด ์์  ๊ธฐ๋ฅ ๊ตฌํ S.A 1์ฐจ์์ 

  **11์ 5~6์ผ** ๊ฒ์๊ธ ์์ธ ํ์ด์ง,๋ฆฌ๋ทฐ์์ฑ,์์ ,์ญ์ ,๊ฒ์๊ธ ๋ถ๋งํฌ ๊ธฐ๋ฅ

  **11์ 7~8์ผ** ๋ด ํ๋กํ ๋ถ๋งํฌ,๊ฒ์๊ธฐ๋ฅ,์ถ์ฒ์์คํ
  
  **11์ 8์ผ** ์ถ์ฒ ์์คํ ๊ตฌํ


  ### ๐ท ํ๋ก์ ํธ ์ฐธ์ฌํ ๋ช๋จ ๋ฐ ์ญํ 

  ์๋ฒ๊ธฐ: ๊ฒ์๊ธ ์์ธ ํ์ด์ง,๊ฒ์๊ธฐ๋ฅ
  
  ๋ฐํจ์ง : ์์ธ ๋ฐ์ดํฐ ๋ฒ ์ด์ค ๋ถ๋ฌ์ค๊ธฐ,๊ฒ์๊ธ ๋ถ๋งํฌ ๊ธฐ๋ฅ,๋ด ํ๋กํ ๋ถ๋งํฌ ๋ชจ์๋ณด๊ธฐ
  
  ์ฅ์คํ : ์์ธ ๋ฐ์ดํฐ ๋ฒ ์ด์ค ๋ถ๋ฌ์ค๊ธฐ
  
  ๊น๋ชํ : ํ์๊ฐ์ ,๋ก๊ทธ์ธ,ํ์์ ๋ณด ์์  ๊ธฐ๋ฅ
  
  ์ ์น์ฃผ : ํ๋ก ํธ ๋ฆฌ๋ทฐ ์์ฑ,์์ ,์ญ์ 

  ***


  ### ๐ท API ์ค๊ณ
  <details>
  <summary>์ ๊ธฐ/ํผ์น๊ธฐ ๋ฒํผ</summary>
  <div markdown="1">

  |ํ์ด์ง|๊ธฐ๋ฅ|API URL|Method|Request(์์ฒญ)|Response(์๋ต)|
  |------|------|------|------|------|------|
  |๋ก๊ทธ์ธ|๊ณ์  ๋ก๊ทธ์ธ|user/login/|POST, GET|{โusernameโ:username,โpasswordโ:password}|{โusernameโ:username,โpasswordโ:password}|
  |ํ์๊ฐ์|๊ณ์  ์์ฑ|user/signup/|GET,POST|{โusernameโ:usernaeme,โpasswordโ:password,โprofilenameโ:profilename,โprofileโ:profile,โemailโ:email}|{โusernameโ:usernaeme,โpasswordโ:password,โprofilenameโ:profilename,โprofileโ:profile,โemailโ:email}|
  |๋ก๊ทธ์์|๊ณ์  ๋ก๊ทธ์์|user/logout/|POST|{โusernameโ:username,โpasswordโ:password}|๋ก๊ทธ์์(HTTP_200_OK)|
  |๋ฉ์ธ|------|------|------|------|------|
  |์์ธ ํ์ด์ง|๊ฒ์๊ธ ์์ธ๋ณด๊ธฐ|detail/<int:Review_id>/|GET|{โnameโ:name,โtagโ:tag,โcontentโ:content,โlikeโ:like}|{โnameโ:name,โtagโ:tag,โcontentโ:content,โlikeโ:like}|
  |------|์์ธ ๊ฒ์|------|GET|{โsearchโ:search}|{โsearchโ:search}|
  |------|๋๊ธ ์์ |detail/<int:Review_id>/|PUT|{โusernameโ:username,โcontentโ:content,โgradeโ:grade,โcreated_time:created_time,}|{โusernameโ:username,โcontentโ:content,โgradeโ:grade,โcreated_time:created_time}|
  |------|๋๊ธ ์ญ์ |detail/<int:Review_id>/|DELETE|{โusernameโ:username, โcontentโ:content,โgradeโ:grade,โcreated_time:created_time,}|{โusernameโ:username, โcontentโ:content,โgradeโ:grade,โcreated_time:created_time,}|
  |------|๋๊ธ ์์ฑ|detail/<int:Review_id>/|POST|{โusernameโ:username,โcontentโ:content,โgradeโ:grade,โcreated_time:created_time,}|{โusernameโ:username,โcontentโ:content,โgradeโ:grade,โcreated_time:created_time,}|
  |------|๋ถ๋งํฌ์ถ๊ฐ,์ญ์ |detail/<int:Review_id>/like/|POST|{โlikeโ:like}|{ โmessageโ : โ๋ถ๋งํฌ ์ฑ๊ณตโ}|
  |ํ๋กํ|ํ๋กํ ์์ฑ๋ฐ ๋ณด๊ธฐ|user/profile/|POST,GET|{โusernameโ:username,โpasswordโ:password,โprofilenameโ:profilename,โprofileโ:profile,โemailโ:email}|{โusernameโ:username,โpasswordโ:password,โprofilenameโ:profilename,โprofileโ:profile,โemailโ:email}|
  |------|ํ๋กํ ์์ |user/profile/|PUT|{โusernameโ: usernaeme,โpasswordโ: password,โprofilenameโ: profilename,โprofileโ: profile,โemailโ:email}|{โusernameโ: usernaeme,โpasswordโ: password,โprofilenameโ: profilename,โprofileโ: profile,โemailโ:email}|
  |๋ฆฌ๋ทฐ ํ์ด์ง|์์ฑํ ๋ฆฌ๋ทฐ ๋ชจ์๋ณด๊ธฐ|user/review/|GET|{โidโ:id,โnameโ:name,โcommentโ:comment}|{โidโ:id,โnameโ:name,โcommentโ:comment}|
  |๋ถ๋งํฌ ํ์ด์ง|์ ์ฅํ ๋ถ๋งํฌ ๋ชจ์๋ณด๊ธฐ|user/like/|GET|{โidโ:id,โnameโ:name,โtagโ:tag,โlikeโ:like}|{โidโ:id,โnameโ:name,โtagโ:tag,โlikeโ:like}|
  </div>
  </details>
  


  ### ๐ท ์์ด์ดํ๋ ์
  <details>
  <summary>์ ๊ธฐ/ํผ์น๊ธฐ ๋ฒํผ</summary>
  <div markdown="1">
    
    
  ##  ๋ก๊ทธ์ธํ์ด์ง
  ![ex_screenshot](https://i.ibb.co/W5nX6s7/Untitled.png)
  ![image](https://i.ibb.co/W5nX6s7/Untitled.png)
   ##  ํ์๊ฐ์ ํ์ด์ง
  ![image](https://i.ibb.co/7Wqp7hX/Untitled-2.png)
   ##  ๋ฉ์ธ ํ์ด์ง
  ![image](https://i.ibb.co/1v3rfWy/Untitled-3.png)
   ##  ์์ธ ํ์ด์ง
  ![image](https://i.ibb.co/Lt87dnW/Untitled-4.png)
   ##  ํ์ ์ ๋ณด
  ![image](https://i.ibb.co/Xk482YJ/Untitled-5.png)
   ##  ๋์ ์์ธ๋ฆฌ์คํธ
  ![image](https://i.ibb.co/7ScwCYN/Untitled-6.png)
   ##  ๋ด ๋ฆฌ๋ทฐ ๋ณด๊ธฐ
  ![image](https://i.ibb.co/5RxtX0b/Untitled-7.png)
    
    
  </div>
  </details>

  ### ๐ท erd

  ![image](https://i.ibb.co/18YWrtj/ERD.jpg)
  


  <br/>

