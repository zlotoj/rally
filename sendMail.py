import pyOutlook

from pyOutlook import *
# or from pyOutlook.core.message import Message

account = OutlookAccount('')
message = Message(account, 'A body', 'A subject', [Contact('bartlomiej.kluza.ctr@sabre.com')])
message.attach(bytes('some bytes', 'utf-8'), 'bytes.txt')
message.send()