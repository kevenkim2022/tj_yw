# @Date    : 2022/6/18
# @Author  : Jin Chun Long (chunlong.jin@westwell-lab.com)
# @Project : abort_vehicle
# @File : AbortVehicle.py
# @Software: PyCharm
import redis
from ww.myutil.FileSetting import get_conf as f


class my_redis:
    def __init__(self):
        st = f("database", "redis")
        self.host = st['host']
        self.port = st['port']
        self.conn = redis.Redis(host=self.host, port=self.port, decode_responses=True)

    def query_key(self,key):
        return self.conn.get(key)

    def query_list(self,key):
        return self.conn.hgetall(key)

    def delete_key(self,key):
        self.conn.delete(key)


    # 关闭REDIS连接
    def close_redis(self):
        self.conn.close()
