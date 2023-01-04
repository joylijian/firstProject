from flask import Flask

app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     a = input("请输入：")
#     b = input("请输入：")
#     return 'hello world'
#
#
# if __name__ == '__main__':
#     app.run(host='127.0.0.1', port=5000)

# @app.route('/login')
# def login():
#     return 'Login'
#
#
# if __name__ == '__main__':
#     app.run()


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello')
def hello():
    return 'Hello, World'


@app.route('/world')
def hello():
    return 'this a new  World'


if __name__ == '__main__':
    app.run()
