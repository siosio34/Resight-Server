from app import app
# TODO edit app name


def initialize_controller():
    from app.Controller.AppStoreController import appStoreBluePrint
    app.register_blueprint(appStoreBluePrint)
