# from flask import Flask
#
# app = Flask(__name__)
#
#
# # @app.route('/index')
# @app.route('/')
# def hello_world():
#     # return 'Hello World!'
#     return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'
#
# if __name__ == '__main__':
#     app.run()




# from flask import Flask, render_template,request
# from datetime import datetime
#
# app = Flask(__name__)
#
# @app.route('/<name>',methods=['get'])
# def index(name):
#     print(request.args)
#     return render_template('index.html', name=name)
#
#
# if __name__ == '__main__':
#     app.run(debug=True, port=8777)




from flask import url_for, escape,Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello'

@app.route('/user/<name>')
def user_page(name):
    return 'User: %s' % escape(name)

@app.route('/test')
def test_url_for():
    # 下面是一些调用示例（请在命令行窗口查看输出的 URL）：
    print(url_for('hello'))  # 输出：/
    # 注意下面两个调用是如何生成包含 URL 变量的 URL 的
    print(url_for('user_page', name='greyli'))  # 输出：/user/greyli
    print(url_for('user_page', name='peter'))  # 输出：/user/peter
    print(url_for('test_url_for'))  # 输出：/test
    # 下面这个调用传入了多余的关键字参数，它们会被作为查询字符串附加到 URL 后面。
    print(url_for('test_url_for', num=2))  # 输出：/test?num=2
    return 'Test page'

if __name__ == '__main__':
    app.run(debug=True)
