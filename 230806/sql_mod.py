import pandas as pd
import pymysql

class Database:
    # 생성자 함수 생성
    # DB 서버에 대한 정보를 입력
    def __init__(self, _host, _user, _pass, _db, _port):
        # db라는 변수 생성 (sql 서버에 접속을 하는 변수)
        self.db = pymysql.connect(
            user = _user, 
            password = _pass, 
            host = _host, 
            db = _db, 
            port = _port
        )
        # cursor 변수 생성
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)
    
    # 쿼리문을 실행하여 결과를 리턴해주거나 데이터베이스를 변경하는 함수
    def query(self, sql, value = []):
        self.cursor.execute(sql, value)
        
        if sql.strip().upper().startswith('SELECT'):
            result = self.cursor.fetchall() 
            result = pd.DataFrame(result)
        else:
            self.db.commit()
            result = "Query OK"
        
        return result
    
    # sql 서버와의 접속을 종료
    def sql_close(self):
        self.db.close()