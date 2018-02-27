# importing the module
import tweepy
 
# personal details
consumer_key ="apdPQUyAqqS78zEOrBopeE7tG"
consumer_secret ="TPPjdgULefjAb3T7epA398oKkFhX7MOOJSbxjga60sbdr6q2Uk"
access_token ="967252253877981184-8jF8xAQyCI47NyuGD5Vlll1iDmqjWEx"
access_token_secret ="SfNWgldMVWbLsHCX4kdcEF6no2mSlCIiy8kUyaveNwkik"
 
# authentication of consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
 
# authentication of access token and secret
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
 
# update the status
api.update_status(status ="Hello Everyone !")
