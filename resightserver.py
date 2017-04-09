from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:sjsdj123@localhost:3306/resight'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db_instance = SQLAlchemy(app)
from models import *
db_instance.create_all() 
db_instance.session.commit()

@app.route("/")
def hello():
    return "Hello world!"


@app.route('/app_store', methods=['GET', 'POST'])
def app_store_request():
    if request.method == 'GET':
        store_app_list = Store.query.all()
        print('---------------')
        print(store_app_list)
        print('---------------')
#       return store_app_list
        return 'ok'
    elif request.method == 'POST':
        result = request.get_json()
        print(result)
        app_name = result['app_name']
        app_store_link = result['app_store_link']
        app_image_link = result['app_image_link']
        store_ins = Store(app_name, app_store_link, app_image_link)
        store_ins.add_database()
        return 'post'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3338)


