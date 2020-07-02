import schedule
import time
from skpy import Skype
from datetime import datetime

USERNAME = 'aakashpaul@hotmail.com'
PASSWORD = 'akash420'

TIME_AND_MESSAGE = {
    "m": {
        "time": "10:03:00",
        "message": "Good Morning Everyone"
    },
    "n": {
        "time": "17:26:00",
        "message": "Signing Out"
    }
}
M, N = TIME_AND_MESSAGE.get('m'), TIME_AND_MESSAGE.get('n')

FRIEND_ID = 'aakash.paul9'
GROUP_ID = '19:bbc5789c1a3245e18e4c32a9f83c0061@thread.skype'


#  N for Night
#  M for Morning

ACTIVE = N


def send_message_task():
    sk = Skype(USERNAME, PASSWORD)

    chat_obj = sk.chats[GROUP_ID]
    chat_obj.sendMsg(ACTIVE.get("message"))

    print("Message Sent!")
    exit()

    # sk.chats.recent()     # to find out the group id and topic

    ''' 
    sk.user # you
    sk.contacts # your contacts
    sk.chats # your conversations

    ch = sk.chats.create(["joe.4", "daisy.5"]) # new group conversation
    ch = sk.contacts["joe.4"].chat # 1-to-1 conversatione
    ch.sendMsg(content) # plain-text message
    ch.sendFile(open("song.mp3", "rb"), "song.mp3") # file upload
    ch.sendContact(sk.contacts["daisy.5"]) # contact sharing

    ch.getMsgs() # retrieve recent messages
    '''


schedule.every().day.at(ACTIVE.get('time')).do(send_message_task)

while True:
    now = datetime.now()

    remaining = datetime.strptime(ACTIVE.get('time'), '%H:%M:%S') - \
                datetime.strptime(f'{now.hour}:{now.minute}:{now.second}', '%H:%M:%S')

    schedule.run_pending()
    time.sleep(1)
    print(remaining)



