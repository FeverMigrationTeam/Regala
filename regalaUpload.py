import json
import logging
from libs import pymysql
from datetime import datetime

db_info = {
    "host": 'fever-db.cy76xlw8fwhe.ap-northeast-2.rds.amazonaws.com',
    "user": 'admin',
    "password": 'admin1234',
    "port": 3306,
    "db": 'fever',
}


connection = pymysql.connect(host=db_info["host"], 
            user=db_info["user"], 
            password=db_info["password"], 
            port=db_info["port"], 
            db=db_info["db"]
            )

cursor = connection.cursor()

query = """
    insert into 
    video(user_user_idx, stadium_stadium_idx, video_url, video_title) 
    values (%s, %s, %s, %s)
"""


class Form:
    def __init__(self, body):
        now = datetime.now()
        strnow = now.strftime("%Y%m%d%H%M%S")
        self._user_id = body['user_id']
        self._stadium_id = body['stadium_id']
        self._url = body['url']
        self._title = f'{self._user_id}{self._stadium_id}{strnow}'

    def getUserId(self):
        return self._user_id
    def getStadiumId(self):
        return self._stadium_id
    def getUrl(self):
        return self._url
    def getTitle(self):
        return self._title
    def getData(self):
        return {
            "user_user_idx": self.getUserId,
            "stadium_stadium_idx": self.getStadiumId,
            "video_url": self.getUrl,
            "video_title": self.getTitle
        }


def lambda_handler(event, context):
    form = Form(event)

    try:
        cursor.execute(query, (
            form.getUserId(),
            form.getStadiumId(),
            form.getUrl(),
            form.getTitle(),
        )) # excute() : 쿼리문 날리기
        
        connection.commit()
            
        return {
            "statusCode": 200,
            "message": "success",
            "data": form.getData()
        }
    except:
        return {
            "statusCode": 400,
            "message": "request fail"
        }
    