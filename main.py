from flask import Flask, render_template, redirect, url_for, request, flash
import pymysql
app = Flask(__name__, static_folder="static")


con = pymysql.connect(host='localhost',
                      user='root',
                      password='',
                      db='test',
                      charset='utf8',
                      cursorclass=pymysql.cursors.DictCursor)


@app.route('/')
def index():
    cur = con.cursor()
    cur.execute("SELECT * FROM orders ORDER BY id DESC")
    rows = cur.fetchall()
    return render_template('index.html', rows=rows)


@app.route('/insert', methods=['POST', 'GET'])
def insert():
    if request.method == 'POST':
        user = request.form['user']
        user_order = request.form['user_order']
        date = request.form['date']

        with con.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `orders` (`user`, `user_order`, `date`) VALUES (%s, %s, %s)"
            cursor.execute(sql, (user, user_order, date))
            con.commit()

        flash("Данные добавлены")
        return redirect(url_for('index'))


if __name__ == "__main__":
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    app.run(port=500, debug=True)
