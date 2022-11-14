  # 🚩 project WineSearch 
  ## 👩‍💻 A2 일석이조

   ![image](https://i.ibb.co/CsrNLm5/unnamed.jpg)
  <p>
      <img src="https://img.shields.io/badge/Django-4.1.1-green"/>
  </p>

  ### 🍷 소개
  - 유저의 취향에 맞는 와인을 추천해주는 사이트
  - 노션 https://www.notion.so/S-A-1babf1e770e14575b9df9008e6c5e5c9
  
  ### 🍷 사용한 데이터셋 모델
  - https://www.kaggle.com/datasets/zynicide/wine-reviews
  
  ### 🍷 주요 기능 
  - ##### 찾고싶은 와인 검색
  - ##### 먹어본 와인에 대한 평점 및 리뷰 작성
  - ##### 작성한 평점 및 리뷰 모아보기
  - ##### 취향에 맞는 와인 북마크하기
  - ##### 북마크한 와인 모아보기
  - ##### 선호하는 와인 데이터를 기반의 추천 시스템
  
  
  ***


  ### 🍷 개발 일정
  
  **진행기간** 2022년 11월 2일 ~ 2022년 11월 8일

  **11월 2~3일** S.A 내용 작성,와이어 데이터 베이스 불러오기 

  **11월 3~4일** 회원가입,로그인,회원정보 수정 기능 구현 S.A 1차수정

  **11월 5~6일** 게시글 상세 페이지,리뷰작성,수정,삭제,게시글 북마크 기능

  **11월 7~8일** 내 프로필 북마크,검색기능,추천시스템
  
  **11월 8일** 추천 시스템 구현


  ### 🍷 프로젝트 참여한 명단 및 역할

  안범기: 게시글 상세 페이지,검색기능
  
  박효진 : 와인 데이터 베이스 불러오기,게시글 북마크 기능,내 프로필 북마크 모아보기
  
  장준표 : 와인 데이터 베이스 불러오기
  
  김명현 : 회원가입 ,로그인,회원정보 수정 기능
  
  유승주 : 프론트 리뷰 작성,수정,삭제

  ***


  ### 🍷 API 설계
  <details>
  <summary>접기/펼치기 버튼</summary>
  <div markdown="1">

  |페이지|기능|API URL|Method|Request(요청)|Response(응답)|
  |------|------|------|------|------|------|
  |로그인|계정 로그인|user/login/|POST, GET|{”username”:username,”password”:password}|{”username”:username,”password”:password}|
  |회원가입|계정 생성|user/signup/|GET,POST|{”username”:usernaeme,”password”:password,”profilename”:profilename,”profile”:profile,”email”:email}|{”username”:usernaeme,”password”:password,”profilename”:profilename,”profile”:profile,”email”:email}|
  |로그아웃|계정 로그아웃|user/logout/|POST|{”username”:username,”password”:password}|로그아웃(HTTP_200_OK)|
  |메인|------|------|------|------|------|
  |상세 페이지|게시글 상세보기|detail/<int:Review_id>/|GET|{”name”:name,”tag”:tag,”content”:content,”like”:like}|{”name”:name,”tag”:tag,”content”:content,”like”:like}|
  |------|와인 검색|------|GET|{”search”:search}|{”search”:search}|
  |------|댓글 수정|detail/<int:Review_id>/|PUT|{”username”:username,”content”:content,”grade”:grade,”created_time:created_time,}|{”username”:username,”content”:content,”grade”:grade,”created_time:created_time}|
  |------|댓글 삭제|detail/<int:Review_id>/|DELETE|{”username”:username, ”content”:content,”grade”:grade,”created_time:created_time,}|{”username”:username, ”content”:content,”grade”:grade,”created_time:created_time,}|
  |------|댓글 작성|detail/<int:Review_id>/|POST|{”username”:username,”content”:content,”grade”:grade,”created_time:created_time,}|{”username”:username,”content”:content,”grade”:grade,”created_time:created_time,}|
  |------|북마크추가,삭제|detail/<int:Review_id>/like/|POST|{”like”:like}|{ “message” : “북마크 성공”}|
  |프로필|프로필 작성및 보기|user/profile/|POST,GET|{”username”:username,”password”:password,”profilename”:profilename,”profile”:profile,”email”:email}|{”username”:username,”password”:password,”profilename”:profilename,”profile”:profile,”email”:email}|
  |------|프로필 수정|user/profile/|PUT|{”username”: usernaeme,”password”: password,”profilename”: profilename,”profile”: profile,”email”:email}|{”username”: usernaeme,”password”: password,”profilename”: profilename,”profile”: profile,”email”:email}|
  |리뷰 페이지|작성한 리뷰 모아보기|user/review/|GET|{”id”:id,”name”:name,”comment”:comment}|{”id”:id,”name”:name,”comment”:comment}|
  |북마크 페이지|저장한 북마크 모아보기|user/like/|GET|{”id”:id,”name”:name,”tag”:tag,”like”:like}|{”id”:id,”name”:name,”tag”:tag,”like”:like}|
  </div>
  </details>
  


  ### 🍷 와이어프레임
  <details>
  <summary>접기/펼치기 버튼</summary>
  <div markdown="1">
    
    
  ##  로그인페이지
  ![ex_screenshot](https://i.ibb.co/W5nX6s7/Untitled.png)
  ![image](https://i.ibb.co/W5nX6s7/Untitled.png)
   ##  회원가입 페이지
  ![image](https://i.ibb.co/7Wqp7hX/Untitled-2.png)
   ##  메인 페이지
  ![image](https://i.ibb.co/1v3rfWy/Untitled-3.png)
   ##  상세 페이지
  ![image](https://i.ibb.co/Lt87dnW/Untitled-4.png)
   ##  회원 정보
  ![image](https://i.ibb.co/Xk482YJ/Untitled-5.png)
   ##  나의 와인리스트
  ![image](https://i.ibb.co/7ScwCYN/Untitled-6.png)
   ##  내 리뷰 보기
  ![image](https://i.ibb.co/5RxtX0b/Untitled-7.png)
    
    
  </div>
  </details>

  ### 🍷 erd

  ![image](https://i.ibb.co/18YWrtj/ERD.jpg)
  


  <br/>

