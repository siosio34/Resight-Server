from config.database import db_instance


class Store(db_instance.Model):
    __tablename__ = 'stores'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    id = db_instance.Column(db_instance.Integer, primary_key=True)
    app_name = db_instance.Column(db_instance.String(50), unique=True)
    app_store_link = db_instance.Column(db_instance.String(50), unique=True)
    app_image_link = db_instance.Column(db_instance.String(50), unique=True)

    def __init__(self, app_name=None, app_store_link=None, app_image_link=None):
        self.app_name = app_name
        self.app_store_link = app_store_link
        self.app_image_link = app_image_link

    def __repr__(self):
        return '<User %r>' % self.app_name

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__columns}

    def add_database(self):
        db_instance.session.add(self)
        db_instance.session.commit()







