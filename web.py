from flask import Flask,render_template

app = Flask(__name__)

#创建网址/show/info和函数index的对应关系
#用户访问/show/info的时候自动执行index函数
@app.route('/show/info')
def index():
    return render_template("Index.html")

@app.route('/get/news')
def get_news():
    return render_template("get_news.html")

@app.route('/charactor/list')
def get_charcher():
    return render_template("chalist.html")

@app.route('/register')
def register():
    return render_template("register.html")

if __name__ == '__main__':
    app.run()


