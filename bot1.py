import praw
import time
import os
import requests

def bot_login():
    print("loggin in...")
    r=praw.Reddit(username="Enter your Username",
                  password="Enter your password",
                  client_id="ClienT ID is to be taken by steps in tutorial",
                  client_secret="ClienT secret is to be taken by steps in tutorial",
                  user_agent="Anything you want to add")
    print ("logged in!")
    return r


def run_bot(r,comm_r):
    print("Getting 10 new comments!!!\n")
    url="http://api.icndb.com/jokes/random"
    for comment in r.subreddit('test').comments(limit=10):
        if "joke" in comment.body and comment.id not in comment_R and not comment.author==r.user.me():
            joke=requests.get(url).json()['value']['joke']
            print(f'Joke is in comment in ID: {comment.id}')
            comment.reply(f"Chuck Norris Joke for you:{joke}\"[click here](http://api.icndb.com/jokes/random) \"to find more")
            print(f'Replied to comment with ID: {comment.id}\n')
            comment_R.append(comment.id)
            with open("comments_R.txt", "a") as f:
                f.write(f'\n{comment.id}')
    print("Bot sleeping for 10 seconds zZ\n")
    time.sleep(10)

def get_save_comm():
    if not os.path.isfile("comments_R.txt"):
        comments_R = []
    

    else:
        with open("comments_R.txt", "r") as f:
            comments_R = f.read().split('\n')

    return comments_R

r= bot_login()

comment_R=get_save_comm()
if comment_R!=[]:
    print(f'These comment IDs are replied already: {comment_R}')

else:
    print("No one was replied to comment yet!\n")

while True:
    run_bot(r,comment_R)
