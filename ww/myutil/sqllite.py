# @Date    : 2022/7/10
# @Author  : Jin chunlong (chunlong.jin@westwell-lab.com)
# @Project : 
# @File : 
# @Software:
import sqlite3

con = sqlite3.connect("db")
sql = "create table main.lcj_record(id identity ,title varchar(200),content_html varchar(1000000) )"
# sql = "select * from  lcj_record"
c = con.cursor()
c.execute(sql)
for i in c.fetchall():
    print(i)
con.commit()
con.close()