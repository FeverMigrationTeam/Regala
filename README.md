# Regala
리갈라 관련 피버팀 코드

## 고려사항
* 클라이언트에서 POST요청을 보낼 때, request body를 어떻게 읽어올건지
  * lambda POST 방법 찾아보기: 해결완료
* regala 기기에 실행 요청과 함께 보낼 인자를 어떻게 전달?
  * 태민형에게 .py 실행파일 받아서 실행
  * (+) 람다함수를 실행( .py 실행파일을 실행하는 것과 마찬가지 )
* 기기촬영시작 파일 실행시킨 뒤, callback을 어떻게 받음?
* regala record와 power가 다른점?
  * record : 영상 촬영 시작/종료 
  * power : 기기(카메라) 전원 상태 ON/OFF


## API
### regalaUpload
* end-point: https://b9zp60eqhd.execute-api.ap-northeast-2.amazonaws.com/regala/upload
* method: POST
* request:
  * body:
    ```json
      {
        "user_id": 1,
        "stadium_id": "1",
        "url": "playcarnival.regala.com/5"
      }
    ```
* response:
  ```python
  # json string
    "{\n  \"statusCode\": 200,\n  \"message\": \"success\",\n  \"data\": {\n    \"user_user_idx\": 1,\n    \"stadium_stadium_idx\": \"1\",\n    \"video_url\": \"playcarnival.regala.com/5\",\n    \"video_title\": \"1120220116134308\"\n  }\n}"
  ```

## ROS 
### jira link 
* 방법 3가지 : https://playcarnival.atlassian.net/wiki/spaces/P/pages/688140
