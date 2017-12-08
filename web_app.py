from flask import Flask, render_template
import pymysql

from settings import MYSQL_SETTINGS


app = Flask(__name__)


@app.route('/')
def home():
    conn = pymysql.connect(**MYSQL_SETTINGS)

    with conn.cursor() as cursor:
        sql = 'SELECT floor, screen_name, content, created_at ' \
              'FROM posts ' \
              'WHERE screen_name=%s'
        cursor.execute(sql, ('逆流之河',))
        result = cursor.fetchall()

    return render_template('home.html', result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
