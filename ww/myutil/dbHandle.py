# @Date    : 2022/6/30
# @Author  : Jin chunlong (chunlong.jin@westwell-lab.com)
# @Project : 
# @File : 
# @Software:
import pymysql
from ww.myutil.FileSetting import get_conf as f

class dbHelper:

    def __init__(self):
        st = f("database", "mysql")
        self.host = st['host']
        self.username = st['user']
        self.password = st['password']
        self.port = st['port']
        self.dbname = st['database']
        self.conn = self.get_conn()

        if self.conn:
            self.cursor = self.conn.cursor()
        print(self.host)

    def get_conn(self):
        try:
            conn = pymysql.connect(host = self.host, user = self.username, password = self.password, db = self.dbname)

        except Exception as e:
            print(e)
            conn = False
        return conn

    def close_conn(self):
        if self.conn:
            try:
                if type(self.cursor) == object:
                    self.cursor.close()
                if type(self.conn) == object:
                    self.conn.close()
            except Exception:
                print("close failed")

    def query_sql(self, sql):
        if self.conn:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            fields = self.cursor.description

            res = format_data(fields, result)
            return res


def format_data(fields, result):
    field = []
    for i in fields:
        field.append(i[0])

    res = []
    for iter in result:
        line_data = {}
        for index in range(0, len(field)):
            line_data[field[index]] = iter[index]
        res.append(line_data)
    return res