from app import app
# TODO edit app name


def initialize_controller():
    from app.Controller.AppStoreController import appStoreBluePrint
    from app.Controller.SensorDataController import handLearnBluePrint
    app.register_blueprint(appStoreBluePrint)
    app.register_blueprint(handLearnBluePrint)
