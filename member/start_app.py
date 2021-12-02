from flask import Flask, render_template, request, redirect, session, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = "abcde"   #암호키 발행해야함

def getconn():
    conn = sqlite3.connect("c:/pydb/testdb.db")
    return conn

@app.route("/")
def main():
    if "userID" in session:  #login()에서 세션 발급
        return render_template("index.html", username=session.get("userID"))
    else:
        return render_template('index.html')

# 회원 목록
@app.route("/memberlist")
def memberlist():
    conn = getconn()
    cur = conn.cursor()
    sql = "SELECT * FROM member"
    cur.execute(sql)
    rs = cur.fetchall()
    conn.close()
    if "userID" in session:
        return render_template('memberlist.html', username=session.get("userID"), rs=rs)
    else:
        return render_template('memberlist.html')

# 회원 등록
@app.route("/register", methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        id = request.form['memberid']
        pwd = request.form['passwd']
        name = request.form['name']
        age = request.form['age']
        date = request.form['regdate']

        conn = sqlite3.connect("c:/pydb/testdb.db")
        cur = conn.cursor()
        sql = "INSERT INTO member VALUES ('%s', '%s', '%s', '%s', '%s')" % (id, pwd, name, age, date)
        cur.execute(sql)
        conn.commit()
        conn.close()
        return redirect(url_for('main'))
    else:
        return render_template("register.html")

# 회원 상세 보기
@app.route('/member_view/<string:id>')
def member_view(id):
    conn = getconn()
    cur = conn.cursor()
    sql = "SELECT * FROM member WHERE memberid = '%s' " % (id)
    cur.execute(sql)
    rs = cur.fetchone()
    print(rs)
    conn.close()
    if "userID" in session:
        return render_template('member_view.html', username=session.get("userID"), rs=rs)
    else:
        return render_template('member_view.html')

# 로그인
@app.route("/login", methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        id = request.form['memberid']
        pwd = request.form['passwd']

        conn = getconn()
        cur = conn.cursor()
        sql = "SELECT * FROM member WHERE memberid = '%s' AND passwd = '%s' " % (id, pwd)
        cur.execute(sql)
        rs = cur.fetchone()
        if rs:
            session['userID'] = id  #세션 발급
            return redirect(url_for('main'))
        else:
            error = "아이디나 비밀번호가 일치하지 않습니다."
            return render_template("login.html", error=error)
    else:
        return render_template("login.html")

# 로그 아웃
@app.route('/logout')
def logout():
    session.pop("userID")  # 세션 삭제
    return redirect(url_for('main'))

# 회원 삭제
@app.route('/member_delete/<string:id>')
def member_delete(id):
    conn = getconn()
    cur = conn.cursor()
    sql = "DELETE FROM member WHERE memberid = '%s' " % (id)
    cur.execute(sql)
    conn.commit()
    conn.close()
    return redirect(url_for('memberlist'))

# 회원 수정
@app.route('/member_edit/<string:id>', methods = ['GET', 'POST'])
def member_edit(id):
    if request.method == 'POST':
        pwd = request.form['passwd']
        name = request.form['name']
        age = request.form['age']
        date = request.form['regdate']

        conn = getconn()
        cur = conn.cursor()
        sql = "UPDATE member SET passwd = '%s', name = '%s', age = '%s', regdate = '%s' WHERE memberid='%s' " % (pwd, name, age, date, id)
        cur.execute(sql)
        conn.commit()
        conn.close()
        return redirect(url_for('member_view', id=id))
    else:
        conn = getconn()
        cur = conn.cursor()
        sql = "SELECT * FROM member WHERE memberid = '%s' " % (id)
        cur.execute(sql)
        rs = cur.fetchone()
        conn.close()

        if "userID" in session:
            return render_template('member_edit.html', username=session.get("userID"), rs=rs)
        else:
            return render_template('member_edit.html')

# 게시판 목록
@app.route("/boardlist", methods = ['GET'])
def boardlist():
    conn = getconn()
    cur = conn.cursor()
    sql = "SELECT * FROM board"
    cur.execute(sql)
    rs = cur.fetchall()
    conn.close()
    return render_template('boardlist.html', rs=rs)

# 게시글 등록
@app.route("/board_write", methods = ['GET', 'POST'])
def board_write():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        id = session['userID']

        conn = sqlite3.connect("c:/pydb/testdb.db")
        cur = conn.cursor()
        sql = "INSERT INTO board VALUES ('%s', '%s', '%s') " % (title, content, id)
        cur.execute(sql)
        conn.commit()
        conn.close()
        return redirect(url_for('boardlist'))
    else:
        if "userID" in session:
            return render_template('board_write.html', username=session.get("userID"))
        else:
            return render_template('board_write.html')

# 게시글 상세 보기
@app.route("/board_view/<string:title>")
def board_view(title):
    conn = getconn()
    cur = conn.cursor()
    sql = "SELECT * FROM board WHERE title = '%s' " % (title)
    cur.execute(sql)
    rs = cur.fetchone()
    conn.close()
    if "userID" in session:
        return render_template('board_view.html', username=session.get("userID"), rs=rs)
    else:
        return render_template('board_view.html')

# 게시글 삭제
@app.route('/board_delete/<string:title>')
def board_delete(title):
    conn = getconn()
    cur = conn.cursor()
    sql = "DELETE FROM board WHERE title = '%s' " % (title)
    cur.execute(sql)
    conn.commit()
    conn.close()
    return redirect(url_for('boardlist'))

# 게시글 수정
@app.route('/board_edit/<string:title>', methods = ['GET', 'POST'])
def board_edit(title):
    if request.method == 'POST':
        content = request.form['content']

        conn = getconn()
        cur = conn.cursor()
        sql = "UPDATE board SET content = '%s' WHERE title = '%s' " % (content, title)
        cur.execute(sql)
        conn.commit()
        conn.close()
        return redirect(url_for('board_view', title=title))
    else:
        conn = getconn()
        cur = conn.cursor()
        sql = "SELECT * FROM board WHERE title = '%s' " % (title)
        cur.execute(sql)
        rs = cur.fetchone()
        conn.close()

        if "userID" in session:
            return render_template('board_edit.html', username=session.get("userID"), rs=rs)
        else:
            return render_template('board_edit.html')


app.run()