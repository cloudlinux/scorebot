from sys import argv
from slackclient import SlackClient

token = argv[1]
username = argv[2]

slack = SlackClient(token)
if not slack.rtm_connect():
    print("Cannot connect to Slack.com")

all_users = slack.api_call("users.list")['members']
print(list((u['id'], u['name'])
           for u in all_users if u['name'] == username))
