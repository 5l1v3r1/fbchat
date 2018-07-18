# -*- coding: UTF-8 -*-

# Imports Client, Thread, Group, Page, User and Message
from fbchat import *

# Login, using your email and credentials
client = Client('<email>', '<password>')

# Display data about you
print(client, vars(client))

# Send a message to yourself
message = client.send_text(client, 'Hi me!')

# Display data about the sent message
print(message, vars(message))
