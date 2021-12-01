from flask import Flask, render_template

app = Flask(__name__)

# 127.0.0.1:5000
@app.route('/')
def index():
    return render_template('index.html')

# 127.0.0.1/loopindex
@app.route('/loopindex')
def loopindex():
    items = ['a', 'b', 'c', 'd']
    return render_template('loopindex.html', items = items)

# 127.0.0.1/node
@app.route('/node')
def node():
    return render_template('node.html')

# 127.0.0.1:5000/nodeimg
@app.route('/nodeimg')
def nodeimg():
    return render_template('nodeimg.html')


app.run()