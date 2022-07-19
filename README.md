# Assemble-Back
> ## 해야할 일
> * 배포해서 링크 만들기 
> * Figma 보면서 필요한 DB 및 기능 무엇인지 파악하기 
> * url 및 api 작성하기 + 기능 구현
---
> ## 구현 현황
> 1. 로그인 이전 메인 페이지 (O)  
> <pre><code>GET: http://127.0.0.1:8000
>   
>{
>    "test_message": "Here is First page"
>}
></code></pre>  
> 2. 회원가입 페이지 (O)
> <pre><code>POST: http://127.0.0.1:8000/signup/
>
>{
>    "username":"username0",
>    "password":"0000",
>    "confirm":"0000",
>    "name":"이름",
>    "email":"username0@google.com",
>    "phone":"01000000000",
>    "gender":"male",
>    "birthday":"2001-01-01"
>}
>   
>{
>    "id": 6,
>    "username": "username0",
>    "confirm": null,
>    "name": "이름",
>    "email": "username0@google.com",
>    "phone": "01000000000",
>    "gender": "male",
>    "birthday": "2001-01-01"
>}
></code></pre>
> 3. 로그인 페이지 (X)
> 4. To Do List 생성
> <pre><code>POST: http://127.0.0.1:8000/create_tdl/
>
>{
>    "title":"밥먹기",
>    "body":"오후 1시에 학식 먹기",
>    "enddate":"2022-07-22"
>}
>   
>{
>    "id": 4,
>    "title": "밥먹기",
>    "body": "오후 1시에 학식 먹기",
>    "enddate": "2022-07-22",
>    "writtendate": "2022-07-19",
>    "is_first": null,
>    "is_end": null
>}
></code></pre>
> 5. To Do List 정보 불러오기
> <pre><code>GET: http://127.0.0.1:8000/tdl/1(<= ToDoList의 id값에 해당하는 정수)
>   
>{
>    "message": "Details of To Do List",
>    "id": 1,
>    "title": "회의하기",
>    "body": "강남역에서 회의하기",
>    "enddate": "2022-07-19",
>    "writtendate": "2022-07-18",
>    "is_first": 1,
>    "is_end": null
>}
></code></pre>
> 6. To Do List에 우선순위 설정
><pre><code>POST: http://127.0.0.1:8000/tdl/priority/1(<= ToDoList의 id값에 해당하는 정수)
>   
> # 처음 실행하면 우선순위 부여
>{
>    "message": "This list is priority page",
>    "title": "회의하기",
>    "Priority": true
>}
>
> # 다시 실행하면 우선순위 제거
>{
>    "message": "This is priority page",
>    "title": "회의하기",
>    "Priority": null
>}
></code></pre>
> 7. To Do List 삭제
><pre><code>POST: http://127.0.0.1:8000/delete_tdl/3(<= ToDoList의 id값에 해당하는 정수)
>   
> # 다시 실행하면 우선순위 제거
>{
>    "message": "This is priority page",
>    "title": "회의하기",
>    "Priority": null
>}
></code></pre>
> 8. 메인 화면 
><pre><code>GET: http://127.0.0.1:8000/main/
>
>{
>    "message": "This list is deleted"
>}
>
> # 이후 GET: http://127.0.0.1:8000/main/ 접속 시 id가 3이었던 To Do List는 사라짐
>{
>    "To Do Lists": [
>        {
>            "id": 1,
>            "title": "회의하기",
>            "body": "강남역에서 회의하기",
>            "enddate": "2022-07-19",
>            "writtendate": "2022-07-18",
>            "is_first": 1,
>            "is_end": null
>        },
>        {
>            "id": 2,
>            "title": "회의하기",
>            "body": "강남역에서 회의하기",
>            "enddate": "2022-07-19",
>            "writtendate": "2022-07-18",
>            "is_first": null,
>            "is_end": null
>        },
>        {
>            "id": 4,
>            "title": "밥먹기",
>            "body": "오후 1시에 학식 먹기",
>            "enddate": "2022-07-22",
>            "writtendate": "2022-07-19",
>            "is_first": null,
>            "is_end": null
>        }
>    ]
>}
></code></pre>