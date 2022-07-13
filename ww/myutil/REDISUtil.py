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
        self.password = st['password']
        self.conn = redis.Redis(host=self.host, port=self.port, password=self.password, decode_responses=True)

    def query_key(self,key):
        return self.conn.get(key)

    def query_list(self, key):
        try:
            if self.conn.exists(key):
                if self.conn.type(key) == "hash":
                    rs = self.conn.hgetall(key)
                    print("hash11")
                    return rs
                elif self.conn.type(key) == "zset":
                    rs = self.conn.zrange(key, 0, -1, desc=True, withscores=True)
                    print(rs)
                    return rs
                elif self.conn.type(key) == "string":
                    pass
                    rs = self.conn.get(key)
                    return rs
        except:
            pass

    def delete_key(self, key):
        self.conn.delete(key)

    def query_all(self):
        return self.conn.keys()

    def close_redis(self):
        self.conn.close()

    def test(self):
        pass
