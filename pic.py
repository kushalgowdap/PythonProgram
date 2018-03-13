import os
import time
import tweepy

consumer_key ="apdPQUyAqqS78zEOrBopeE7tG"
consumer_secret ="TPPjdgULefjAb3T7epA398oKkFhX7MOOJSbxjga60sbdr6q2Uk"
access_token ="967252253877981184-8jF8xAQyCI47NyuGD5Vlll1iDmqjWEx"
access_token_secret ="SfNWgldMVWbLsHCX4kdcEF6no2mSlCIiy8kUyaveNwkik"
 


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)  


a=0

while a<=2:
   
    cmd="fswebcam -F 3 --fps 20 -r 800*600 /home/cs2017a121/img.jpg"
    os.system(cmd)
    img="/home/cs2017a121/img.jpg"
    print("pic taken")
    api.update_with_media(img, status="nice one")
    print('wait for five seconds for selfie')
    time.sleep(5)
    a+=1
  
    print('success')
