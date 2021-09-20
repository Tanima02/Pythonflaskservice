
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.orm import sessionmaker

from src.model.twitter_model import db, ma
from src.service.twitter_service import Twitterservice,Userservice

#Init flask
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@127.0.0.1:3307/twitterdb"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
db.init_app(app)
ma.init_app(app)
#ma = Marshmallow(app)


# Init app

app.config["SQLALCHEMY_ECHO"] = True


@app.route("/", methods=["GET"])
def get():
    return jsonify({"msg": "Hello World"})


@app.route("/user", methods=["POST"])
def add_user():
    username = request.json["username"]
    password = request.json["password"]
    accountname = request.json["accountname"]
    userserv = Userservice()
    id = userserv.add_user(username, password,accountname)
    return (f"User created with id2->{id}")


@app.route("/tweet/add_tweet", methods=["POST"])
def add_tweet_retweet():
    userid = request.json["userid"]
    message = request.json["message"]
    tweeterserv=Twitterservice()
    id = tweeterserv.add_tweet(userid, message)
    return (f"Twitter created with id->{id}")

@app.route("/tweet/retweet/{userid}/{tweetid}", methods=["GET"])
def do_retweet():
    tweeterserv=Twitterservice()
    tweet_retweet=tweeterserv.retweet("userid", "tweetid")
    return {"Data":tweet_retweet}




# Run server
if __name__ == "__main__":
    app.run(debug=True)
