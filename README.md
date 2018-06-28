# whats-py 
It's a minimal python library to use whatsappweb in your python scripts

# Installation

* Using PyPi
`pip install whats-py`

* From Github
```
git clone https://github.com/darshkpatel/whats-py.git
cd whats-py
python3 setup.py
```

# Usage

### Example
This sends the message `HaHa` to the group `Buddies` 100 times.

 
```
import whats-py
webLogin()
sendText("buddies","Haha",100)
webLogout()
```

### Functions
* `webLogin()`
   
    Is used to login into the whatsappweb interface on your whatsapp account. The library finds the QR code and displays it on a webserver on your local host running on port 8080, you can find it on `http://127.0.0.1:8080`

* `checkOnline(contact)` 
   
    This dunction takes one argument ie. Contact . Contact should be the phone number of the person wihout the country code in the format XXXXXXXXXX . Function returns True if the contact is online False otherwise
    
*  `sendText(contact, text, times)`
 
 This function sends `text` as message to `contact` , `times` number of times. 
you can also put in a group name instead of the reciepients phone number to send a message inside a group.
Please note that whatsapp rate limits the number of outgoing messages , and thus You'd notice after 50 messages  the sending symbol appears next to the remaining texts and are sent at one message per 5 seconds.

* `webLogout()`

Logs you out of the whatsapp web session. 




## Limitation
The phone has to manually scan the qr code and should be connected to the internet.


## Legal
This code is in no way affiliated with, authorized, maintained, sponsored or endorsed by WhatsApp or any of its affiliates or subsidiaries. This is an independent and unofficial software. Use at your own risk. Nor should i be responsible for misuse of the code.