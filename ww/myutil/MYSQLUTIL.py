# @Date    : 2022/6/26
# @Author  : Jin chunlong (chunlong.jin@westwell-lab.com)
# @Project : 
# @File : 
# @Software:
import pymysql


# 打开数据库连接
def open_db(host, user_name, password, db_name):
    # 打开数据库连接
    db = pymysql.connect(host, user_name, password, db_name)
    return db


# 获取游标
def get_cursor(db):
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    return cursor


# 执行sql(创建、修改、删除)
def sql_commit(db, cursor, sql, param=None):
    try:
        # 执行sql语句
        cursor.execute(sql, param)
        # 提交到数据库执行
        db.commit()
    except Exception as e:
        print(e)
        # 如果发生错误则回滚
        db.rollback()
        return False

    return True


# 查询
def sql_fetch(cursor, sql):
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    return results


# 关闭数据库连接
def close_db(db, cursor):
    cursor.close()
    db.close()