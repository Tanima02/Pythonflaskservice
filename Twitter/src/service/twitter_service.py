
from typing import List

from marshmallow.fields import Boolean
from sqlalchemy import null

from src.model.twitter_model import Tweet
from src.repo.twitter_repo import Twitter_repo, User_repo


class Twitterservice:

    def retweet(self, userid: int,tweetid:int) ->Tweet:
        try:
            tweet_present_validation = Twitterservice.check_tweet_present_or_not("tweetid")
            if(tweet_present_validation):
                retweet_value= Twitterservice.update_tweet("tweetid","userid")
                if retweet_value:
                    pass
                else:
                    raise Exception("Error found in update")

            else:
             print(f"No tweet found with {tweetid}")
        except Exception as e:
            return None
            #return{"retweet_value":retweet_value,"tweet_value":tweet_value}

    def add_tweet(self, userid:int,message:str) -> int:
        try:
            new_tweet_id = Twitter_repo()
            return new_tweet_id.add_user(userid, message)
        except Exception as e:
            print(f"Exception in creating add_tweet method in service", str(e))
            return None

    def check_tweet_present_or_not(self, tweetid:int) ->Boolean:
        try:
            new_tweet_id = Twitter_repo()
            return new_tweet_id.check_tweet_present_or_not("tweetid")
        except Exception as e:
            print(f"Exception in update_tweet method in repository", str(e))
            return False

    def update_tweet(self, tweetid:int,userid:int) ->int:
        try:
            updated_tweet = Twitter_repo()
            return updated_tweet.update_tweet(tweetid,userid)
        except Exception as e:
            print(f"Exception in creating add_tweet method in service", str(e))
            return None


class Userservice:
    def add_user(self, username: int, password: str,accountname:str) -> int:
        new_user = User_repo()
        return new_user.add_user(username, password,accountname)

