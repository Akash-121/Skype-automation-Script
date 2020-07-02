# Skype-automation-Script
Go to the link and clone the project into the pc.
git clone https://bitbucket.org/ashrafulbd/skype-automation.git

then go to project directory.
cd skype-automation/

Now type "python3" for checking that it is installed or not.
if it installed then we have to make a vartual environment to install the project dependencies and run the project.

python3 -m venv venv

if it not installed the the following message will be displayed!
" The virtual environment was not created successfully because ensurepip is not
available.  On Debian/Ubuntu systems, you need to install the python3-venv
package using the following command.

    apt-get install python3-venv"

install the venv with sudo command and run the "python3 -m venv venv" command and go to the following directory "source venv/bin/activate"

source venv/bin/activate

we have another file named requirments. it has listed all project dependencies. we will install all of those by once by using the following command::

pip install -r requirements.txt

all requirements will be installed successfully.

Now we will edit the main_task file and set the time of scheduled message. there has two parts. one for morning and another for evening. we will scheduled the message for evening at 17:00 and check that Active is N or M in the lower portion of file.

Run the main_task file with python command and it will show the scheduled timer and after a while with successful message. :)

If we want to set another group id, then we have to run some command within the running script. we will edit the main_task file with an editor and add one extra line in last "break". It will run the script but break the successful message. so we will run the project "python -i main_task.py" with this command.

python -i main_task.py

then inner command input will appeared. we will call some prebuild functions for getting group id by importing some pakage dependencies and using username and password!

(venv) akash@akash:~/skype-automation$ python -i main_task.py
-1 day, 22:54:06
>>> import schedule
>>> import time
>>> from skpy import Skype
>>> from datetime import datetime
>>>
>>> USERNAME = 'regam39177@mailnd7.com'
>>> PASSWORD = 'Akash.vua.1'
>>> sk = Skype(USERNAME, PASSWORD)
>>> sk.chats.recent()

the json format result will be shown as output.
we have to find group chat id with topic name. Topic == GroupName.

{'8:aakash.paul9': SkypeSingleChat(id='8:aakash.paul9', alerts=True, userId='aakash.paul9'), '19:27345049cc4e4e59acdce464374febb4@thread.skype': SkypeGroupChat(id='19:27345049cc4e4e59acdce464374febb4@thread.skype', alerts=True, topic='auto test', creatorId='live:.cid.df3bd3356e2b57d', userIds=['aakash.paul9', 'live:.cid.abcb688bae9f4b1c', 'live:.cid.df3bd3356e2b57d'], adminIds=['aakash.paul9', 'live:.cid.abcb688bae9f4b1c', 'live:.cid.df3bd3356e2b57d'], open=True, history=True), '8:live:.cid.abcb688bae9f4b1c': SkypeSingleChat(id='8:live:.cid.abcb688bae9f4b1c', alerts=True, userId='live:.cid.abcb688bae9f4b1c')}

now set the group chat id and remove the "break" word in the last portion of the file. FRIEND_ID = 'aakash.paul9' message will be sent from this ID.

Now run the main_task file with python command. Task is done. :)


Go to the link and clone the project into the pc.
git clone https://bitbucket.org/ashrafulbd/skype-automation.git

then go to project directory.
cd skype-automation/

Now type "python3" for checking that it is installed or not.
if it installed then we have to make a vartual environment to install the project dependencies and run the project.

python3 -m venv venv

if it not installed the the following message will be displayed!
" The virtual environment was not created successfully because ensurepip is not
available.  On Debian/Ubuntu systems, you need to install the python3-venv
package using the following command.

    apt-get install python3-venv"

install the venv with sudo command and run the "python3 -m venv venv" command and go to the following directory "source venv/bin/activate"

source venv/bin/activate

we have another file named requirments. it has listed all project dependencies. we will install all of those by once by using the following command::

pip install -r requirements.txt

all requirements will be installed successfully.

Now we will edit the main_task file and set the time of scheduled message. there has two parts. one for morning and another for evening. we will scheduled the message for evening at 17:00 and check that Active is N or M in the lower portion of file.

Run the main_task file with python command and it will show the scheduled timer and after a while with successful message. :)

If we want to set another group id, then we have to run some command within the running script. we will edit the main_task file with an editor and add one extra line in last "break". It will run the script but break the successful message. so we will run the project "python -i main_task.py" with this command.

python -i main_task.py

then inner command input will appeared. we will call some prebuild functions for getting group id by importing some pakage dependencies and using username and password!

(venv) akash@akash:~/skype-automation$ python -i main_task.py
-1 day, 22:54:06
>>> import schedule
>>> import time
>>> from skpy import Skype
>>> from datetime import datetime
>>>
>>> USERNAME = 'regam39177@mailnd7.com'
>>> PASSWORD = 'Akash.vua.1'
>>> sk = Skype(USERNAME, PASSWORD)
>>> sk.chats.recent()

the json format result will be shown as output.
we have to find group chat id with topic name. Topic == GroupName.

{'8:aakash.paul9': SkypeSingleChat(id='8:aakash.paul9', alerts=True, userId='aakash.paul9'), '19:27345049cc4e4e59acdce464374febb4@thread.skype': SkypeGroupChat(id='19:27345049cc4e4e59acdce464374febb4@thread.skype', alerts=True, topic='auto test', creatorId='live:.cid.df3bd3356e2b57d', userIds=['aakash.paul9', 'live:.cid.abcb688bae9f4b1c', 'live:.cid.df3bd3356e2b57d'], adminIds=['aakash.paul9', 'live:.cid.abcb688bae9f4b1c', 'live:.cid.df3bd3356e2b57d'], open=True, history=True), '8:live:.cid.abcb688bae9f4b1c': SkypeSingleChat(id='8:live:.cid.abcb688bae9f4b1c', alerts=True, userId='live:.cid.abcb688bae9f4b1c')}

now set the group chat id and remove the "break" word in the last portion of the file. FRIEND_ID = 'aakash.paul9' message will be sent from this ID.

Now run the main_task file with python command. Task is done. :)

