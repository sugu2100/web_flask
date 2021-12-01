from flask import Flask, render_template, request

app = Flask(__name__)

# 메인 페이지
@app.route("/")
def main():
    return render_template('main.html')
    #return 'Hello~ Flask'

# 회원 가입
@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        id = request.form['memberid']
        pwd = request.form['passwd']
        name = request.form['name']
        age = request.form['age']
        return render_template('member_list.html', id=id, pwd=pwd, name=name, age=age)
    else:
        return render_template('register.html')

# 로그인
@app.route("/login", methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        uid = request.form['uid']
        passwd = request.form['passwd']
        return render_template('login_result.html', id=uid, pwd=passwd)
    else:
        return render_template('login.html')

#  loop - index
@app.route("/loop_index", methods = ['GET'])
def get_loopindex():
    items = ['a', 'b', 'c', 'd']
    return render_template('loop_index.html', items = items)

# 짝수 / 홀수 판정
@app.route("/even_odd", methods = ['GET', 'POST'])
def even_odd():
    if request.method == 'POST':
        try:
            num = int(request.form['num'])
        except ValueError:
            error_message = "숫자를 입력해주세요"
            return render_template('even_odd.html', error_message=error_message)
        else:
            if num % 2 == 0:
                result = "짝수입니다."
            else:
                result = "홀수입니다."
            return render_template('calc_result.html', num=num, result=result)
    else:
        return render_template('even_odd.html')

if __name__ == "__main__":
    app.run(debug=True)

