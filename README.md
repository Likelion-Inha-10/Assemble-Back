# Assemble-Back
> ## 해야할 일
> * 생성된 그룹 리스트 반환하기
> * 명세서 만들기
> * 파일 다운로드 손보기
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
>}
>   
>{
>    "id": 4,
>    "title": "밥먹기",
>    "body": "오후 1시에 학식 먹기",
>    "writtendate": "2022-07-19",
>    "is_first": 0,
>    "is_end": 0
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
>    "writtendate": "2022-07-18",
>    "is_first": 1,
>    "is_end": 0
>}
></code></pre>
> 6. To Do List에 우선순위 설정
><pre><code>POST: http://127.0.0.1:8000/tdl/priority/1(<= ToDoList의 id값에 해당하는 정수)
>   
> # 처음 실행하면 우선순위 부여
>{
>    "message": "This list is priority page",
>    "title": "회의하기",
>    "is_first": true
>}
>
> # 다시 실행하면 우선순위 제거
>{
>    "message": "This is priority page",
>    "title": "회의하기",
>    "is_first": 0
>}
></code></pre>
> 7. To Do List 완료시 End List로 이동
><pre><code>POST: http://127.0.0.1:8000/tdl/end/1(<= ToDoList의 id값에 해당하는 정수)
>   
> # 처음 실행하면 마감여부 부여
>{
>    "message": "This is end list page",
>    "title": "모각코",
>    "is_end": true
>}
>
> # 다시 실행하면 마감여부 제거
>{
>    "message": "This is end list page",
>    "title": "모각코",
>    "is_end": 0
>}
></code></pre>
>
> 8. To Do List 삭제
><pre><code>POST: http://127.0.0.1:8000/delete_tdl/3(<= ToDoList의 id값에 해당하는 정수)
>   
>{
>    "message": "This list is deleted"
>}
></code></pre>
> 9. 메인 화면 (그룹 리스트도 반환하도록 업데이트됨!)
><pre><code>GET: http://127.0.0.1:8000/main/
>{
>    "To Do Lists": [
>        {
>            "id": 10,
>            "title": "내 생일",
>            "body": "내 생일임",
>            "writtendate": "2022-07-26",
>            "is_first": 1,     # 더 늦게 만들어졌지만 is_first 가 1이어서 위 쪽에 위치함
>            "is_end": 0
>        },
>        {
>            "id": 9,
>            "title": "멋사 MT",
>            "body": "멋사에서 MT를 갑니다",
>            "writtendate": "2022-07-26",
>            "is_first": 0,
>            "is_end": 0
>        }
>    ],
>    "End Lists": [
>        {
>            "id": 8,
>            "title": "모각코",
>            "body": "합정 투썸",
>            "writtendate": "2022-07-26",
>            "is_first": 0,
>            "is_end": 1        # is_end 가 1일 때는 End List로 따로 분류됨
>        }
>    ],
>    "Groups": [
>            {
>                "id": 1,
>                "title": "인하대학교 멋사 10기"
>            },
>            {
>                "id": 2,
>                "title": "인하대학교 멋사 10기"
>            },
>            {
>                "id": 3,
>                "title": "인하대학교 멋사 10기"
>            },
>            {
>                "id": 4,
>                "title": "인하대학교 멋사 10기"
>            },
>            {
>                "id": 5,
>                "title": "멋사 10기"
>            }
>    ]
>}
></code></pre>
> 10. 파일 업로드
><pre><code>POST: http://127.0.0.1:8000/upload/
>   
># Headers 부분 Key: Content-Disposition, Value: attachment; filename={파일 이름}
># Body 부분 Key: file, Value: {파일 지정}
>
>{
>    "message": "File is received"
>}
></code></pre>
> 11. 파일 다운로드
><pre><code>GET: http://127.0.0.1:8000/download/1
>   
>{
>    "File": {
>        "id": 1,
>        "myfile": "/media/image3_nISC4JX.png"
>    }
>}
></code></pre>
> 12. 그룹 생성
><pre><code>POST: http://127.0.0.1:8000/create_grp/
>   
>{
>    "title": "멋사 10기"
>}
>   
>{
>    "id": 5,
>    "title": "멋사 10기"
>}
></code></pre>
> 13. 프로젝트 페이지 (파일 리스트)
><pre><code>GET: http://127.0.0.1:8000/filelists/
>    
>{
>    "FileLists": [
>        {
>            "id": 1,
>            "myfile": "/media/image3_nISC4JX.png"
>        },
>        {
>            "id": 2,
>            "myfile": "/media/file01.docx"
>        },
>        {
>            "id": 3,
>            "myfile": "/media/file01.docx"
>        }
>    ]
>}
></code></pre>