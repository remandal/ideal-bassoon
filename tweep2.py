

import tweepy
import json

# Authenticate to Twitter
auth = tweepy.OAuthHandler("sC9Leo83S05c2w5pQAEmBk5zs",
            "miOAPEfJJet5WaiIH3owmBlvgzBIAyo0lSiADfSrtiXWijQ0YO")
auth.set_access_token("1182908886627389440-ezZUWRh5EPAQ9k1rWOjMYADtE8LfOQ",
            "WOKgr1zPA2MgelKBmwWtSPGbilUcg134EdDg23F4VCpK7")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
            wait_on_rate_limit_notify=True)

# Verify credentials
try:
        api.verify_credentials()
            print("Authentication OK")
except:
        print("Error during authentication")


        MyFile=open('output.txt','a')
        user = api.get_user("mrhappymonkey32")



        def limit_handled(cursor):
                while True:
                            try:
                                            yield cursor.next()
                                                    except tweepy.RateLimitError:
                                                                    time.sleep(15 * 60)

                                                                    for follower in limit_handled(tweepy.Cursor(user.followers_ids).items()):
                                                                                print >>MyFile, follower


