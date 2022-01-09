import json
import logging
from libs import pymysql

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

 
def lambda_handler(event, context):
    cursor = connection.cursor()
    cursor.execute("select * from user") # excute() : 쿼리문 날리기
    
    rows = cursor.fetchall() # fetchall() : 결과값을 return 받음.
    
    for row in rows:
        print("{0} {1} {2}".format(row[0],row[1],row[2]))
        
    return "success lambda RDS"
    
