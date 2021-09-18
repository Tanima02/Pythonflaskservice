

from src.model.twitter_model import User, Tweet, db

from sqlalchemy import update

class Twitter_repo:
    def add_tweet(self, userid:int,message:str)->int:
        try:
            new_tweet= Tweet(userid, message)
            db.session.add(new_tweet)
            db.session.commit()
            return new_tweet.id
        except Exception as e:
            print(f"Exception in creating add_tweet method in repository", str(e))
            return None

    def check_tweet_present_or_not(self,tweetid:int)->bool:
        try:
            tweetidentification = Tweet.query.filter(Tweet.tweetid == "tweetid")
            if tweetidentification is None:
                return False
            else:
                return True
        except Exception as e:
            print(f"Exception in check_tweet_present_or_not method in repository",str(e))
            return False



    def update_tweet(self, tweetid,userid) -> bool:
        try:
            values=Tweet.query.filter_by(tweetid='tweetid')
            #Copying old message to variable
            message=values.message
            #Copying old tweetid to variable
            retweet_id=tweetid
            twitter_id=Twitter_repo.add_tweet(userid,message)
            update_= Tweet.query.filter_by(tweetid='tweetid').\
                                  update({"retweet_id":twitter_id,"message":message,
                                          "retweet_user_id": userid,"retweet_status":True})
            db.session.commit()
            return True
        except Exception as e:
            print(f"Exception in update_tweet method in repository", str(e))
            return False


class User_repo:
    def add_user(self, username: int, password: str,accountname:str) -> int:
        try:
            new_account = User(username, password,accountname)
            db.session.add(new_account)
            db.session.commit()
            return new_account.id
        except Exception as e:
            print(f"Exception in creating add_user method in repository ", str(e))
            return None



