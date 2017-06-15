from flask import Blueprint, request, jsonify

handLearnBluePrint = Blueprint('handLearnBluePrint', __name__)


# 텍스트 파일에 저장
@handLearnBluePrint.route("/api/save_text", methods=['GET', 'POST'])
def save_data_text_file():
    data = request.get_json()

    import os
    cur_dir = os.getcwd()
    save_file_path = cur_dir + ('/Data/{}.txt'.format(data['userId'] + data['motionCode']))

    with open(save_file_path, 'a') as f:
        for sensor_data in data['sensors']:
            f.write(str(sensor_data['1']) + '\t' + str(sensor_data['2']) + '\t' + str(sensor_data['3']) + '\t'
                    + str(sensor_data['4']) + '\t' + str(sensor_data['5']) + '\t' + str(sensor_data['6']))
            f.write('\n')
            # f.write(sensor_data['data'])

    return 'save_data_to_test'


@handLearnBluePrint.route("/api/save_mysql", methods=['GET', 'POST'])
def save_data_mysql():
    return

