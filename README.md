# Assemble-Back
> ## 해야할 일
> 1. 홍진이 형 레포 멤버 추가하기
> 2. Postman과 친해지기
> 3. 배포해서 링크 만들기
> 4. Figma 보면서 필요한 DB 및 기능 무엇인지 파악하기
> 5. url 및 api 작성하기 + 기능 구현
---
> ## 구현 현황
> 1. 로그인 이전 메인 페이지 (O)  
> <pre><code>GET: http://127.0.0.1:8000
>{
>    
>}
>
>{
>    "test_message": "Here is First page"
>}
></code></pre>  
> 2. 회원가입 페이지 (X)
> <pre><code>POST: http://127.0.0.1:8000/signup/
>
>{
>    "username":"username1",
>    "password":"0000",
>    "confirm":"0000",
>    "email":"username1@google.com",
>    "phone":"01000000000",
>    "gender":"male",
>    "birthday":"2001-01-01"
>}
>   
>{
>    "message": "success", 
>    "username": username1"
>}
></code></pre>
> 다시 회원가입 시도 시 다음과 같은 에러 발생. auth를 이용한 회원가입 및 로그인은 안 되는 것 같음. Serializer 로 구현해보자.
><pre><code>{
>    "detail": "CSRF Failed: CSRF token missing."
>}</code></pre>