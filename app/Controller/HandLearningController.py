from flask import Blueprint,request,jsonify

handLearnBluePrint = Blueprint('handLearnBluePrint', __name__)


# 텍스트 파일에 저
@handLearnBluePrint.route("/api/save_text", methods=['POST'])
def save_data_text_file():
    save_file_path = 'Data/sensor.txt'
    with open(save_data_text_file, 'a') as f:
        f.write()
    return 'save_data_to_test'


@handLearnBluePrint.route("api/save_mysql", methods=['GET','POST'])
def save_data_mysql():
    return

