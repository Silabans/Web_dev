import sqlalchemy

class User(db.model):
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    user_id = db.Column(db.Integer, primary_key=True)


class Task:
    def __init__(self, content, flag, key):
        self.content = content
        self.flag = flag
        self.