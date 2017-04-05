from flask import Flask, request, jsonify
from models.store import Store


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello world!"


# TODO 파이어베이스 데이터 가져오기 + 안드로이드에 데이터주기.
@app.route('/app_store', methods=['GET', 'POST'])
def app_store_request():
    if request.method == 'GET':
        return 'ok'
    elif request.method == 'POST':
        result = request.get_json()
        app_name = result['app_name']
        app_store_link = result['app_store_link']
        app_image_link = result['app_image_link']
        store = Store(app_name, app_store_link, app_image_link)
        store.add_database()
        return 'post'


if __name__ == "__main__":
    app.run(host='0.0.0.0')

