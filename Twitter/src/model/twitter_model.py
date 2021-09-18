from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
ma= Marshmallow()


class User(db.Model):
    __tablename__ = "user"
    # defining columns for the table user
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    username = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    accountname = db.Column(db.String(250), nullable=False)


    def __init__(self, username, password,accountname):
        self.username = username
        self.password = password
        self.accountname = accountname


class UserSchema(ma.Schema):
    class Meta:
        fields = ("username","password","accountname")

class Tweet(db.Model):
    __tablename__ = "tweet"
    # defining columns for the table tweet
    tweetid = db.Column(db.Integer, primary_key=True,autoincrement=True)
    #userid = db.Column(db.Integer, nullable=False)
    userid = db.Column(db.Integer, db.ForeignKey('user.id'),
                            nullable=False)
    category = db.relationship('User',
                               backref=db.backref('tweet', lazy=True))
    message= db.Column(db.String(250), nullable=True)
    retweet_status=db.Column(db.Boolean, unique=False,nullable=True,default=False)
    retweet_user_id=db.Column(db.Integer, nullable=True)

    def __init__(self, tweetid,userid,message,retweet_status,retweet_user_id,retweet_id):
        self.tweetid = tweetid
        self.userid = userid
        self.message = message
        self.retweet_status =retweet_status
        self.retweet_user_id=retweet_user_id
        self.retweet_id=retweet_id


class TweetSchema(ma.Schema):
    class Meta:
        fields = ("userid","message","retweet_user_id")
