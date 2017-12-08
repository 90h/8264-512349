import pymysql

from settings import MYSQL_SETTINGS


class MysqlPipeline:
    def get_conn(self):
        return pymysql.connect(**MYSQL_SETTINGS)

    def process_item(self, item, spider):
        conn = self.get_conn()

        try:
            with conn.cursor() as cursor:
                sql = "INSERT INTO posts (floor, content, created_at, " \
                      "screen_name, avatar, online_count, registered_at, " \
                      "space, reply_view, reply_count) " \
                      "VALUES " \
                      "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

                params = (item['floor'], item['content'], item['created_at'],
                          item['screen_name'], item['avatar'],
                          item['online_count'], item['registered_at'],
                          item['space'], item['reply_view'], item['reply_count'])

                cursor.execute(sql, params)
                conn.commit()
        finally:
            conn.close()
