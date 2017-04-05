from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello world!"

#TODO 파이어베이스 데이터 가져오기 + 안드로이드에 데이터주기.

@app.route('/resightapp', methods = ['GET','POST'])
def getAndroidAppLink():
    n







if __name__ == "__main__":
    app.run(host='0.0.0.0')
