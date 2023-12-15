import requests
import subprocess
import re
from xtracer import Tracer
from fbchat import log, Client
from fbchat.models import *

em = 'duckssheet@chapsmail.com' #email
ps = 'kali1291' #password

class Quinn(Client):
    thread_type = 'GROUP'
    thread_id = '4455328214506249' 

    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)

        if author_id != self.uid:
            if message_object.text.lower() in ['hi','hello']:
                user = self.fetchUserInfo(author_id)[author_id]
                self.send(Message(text=f"Greetings\nHi {user.name}"), thread_id=thread_id, thread_type=thread_type)
                self.reactToMessage(message_object.uid, MessageReaction.HEART)
            elif message_object.text.lower() == 'hello':
                self.send(Message(text=f'Hi! @Everyone ', mentions=Mention(thread_id, offset=10, length=8)), thread_id=thread_id, thread_type=thread_type)
            elif message_object.text.lower() == "/bot":
                self.send(Message(text="Hello I'm 0x3a Bot \n type /command to show all the commands\n\nMade By: Andrew Smith\nlink: https://m.facebook.com/exc4444"), thread_id = thread_id, thread_type = thread_type,)
            elif message_object.text.lower() == "/command":
                    self.send(Message(text=":COMMANDS:\n\n/bot\n/id\n/rc\n/img\n/print\n/nm\n/act"), thread_id = thread_id, thread_type = thread_type)
            elif(re.match(r'/nm', message_object.text)):
                    self.fetchUserInfo(author_id)[author_id]
                    nname = message_object.text.replace('/nm','')
                    self.changeNickname(nname,{author_id},thread_id=thread_id,thread_type=thread_type)
            elif message_object.text.lower() == '/act':
                user = self.fetchUserInfo(author_id)[author_id]
                ema = self.getUserActiveStatus(author_id)
                self.send(Message(text=f"Name: {user.name}\nActiveStatus: {ema}"),thread_id=thread_id,thread_type=thread_type)
            elif message_object.text.lower() == "what's my name?":
                user = self.fetchUserInfo(author_id)[author_id]
                self.send(Message(text=f"Your Name Is: {user.name}"),thread_id=thread_id,thread_type=thread_type)
            elif message_object.text.lower() == '/rc':
                self.reactToMessage(message_object.uid, MessageReaction.HEART)
                self.reactToMessage(message_object.uid, MessageReaction.SMILE)
                self.reactToMessage(message_object.uid, MessageReaction.LOVE)
                self.reactToMessage(message_object.uid, MessageReaction.ANGRY)
                self.reactToMessage(message_object.uid, MessageReaction.SAD)
                self.reactToMessage(message_object.uid, MessageReaction.WOW)
                self.reactToMessage(message_object.uid, MessageReaction.YES)
                self.reactToMessage(message_object.uid, MessageReaction.NO)
                self.reactToMessage(message_object.uid, MessageReaction.FUCK)
                self.reactToMessage(message_object.uid, MessageReaction.TARAY)
                self.reactToMessage(message_object.uid, MessageReaction.CHUCKLES)
                self.reactToMessage(message_object.uid, MessageReaction.YUCK)
                self.reactToMessage(message_object.uid, MessageReaction.EX)
                self.reactToMessage(message_object.uid, MessageReaction.CHECK)
            elif(re.match(r'/img',message_object.text)):
                user = self.fetchUserInfo(author_id)[author_id]
                img = message_object.text.replace('/img','')
                self.sendRemoteImage(img,message=Message(text=f"PHOTO UPLOADED\nBY: {user.name}"),thread_id=thread_id,thread_type=thread_type)
            elif message_object.text.lower() == '/id':
                user = self.fetchUserInfo(author_id)[author_id]
                self.send(Message(text=f"Name: {user.name}\nID: {author_id}\nLink: {user.url}\nUSER PHOTO:\n{user.photo}\nFRIEND: {user.is_friend}\nGENDER: {user.gender}\nNICKNAME:{user.nickname}\nAFFINITY: {user.affinity}"),thread_id=thread_id, thread_type=thread_type)
                self.reactToMessage(message_object.uid, MessageReaction.CHECK)
            elif message_object.text.lower() in ['i love you','iloveyou','i luv u','i love u']:
                if author_id == author_id:
                    user = self.fetchUserInfo(author_id)[author_id]
                    self.send(Message(text=f'{message_object.text} too!'), thread_id=thread_id, thread_type=thread_type)
                    self.reactToMessage(message_object.uid, MessageReaction.HEART)
                else:
                    self.send(Message(text=f'eww! fuck off'), thread_id=thread_id, thread_type=thread_type)
                    self.reactToMessage(message_object.uid, MessageReaction.YUCK)
            if(re.match(r'/print', message_object.text)):
                    msg = message_object.text.replace('/print ','')
                    user = self.fetchUserInfo(author_id)[author_id]
                    self.send(Message(text=f"Message: {msg}\n\nFrom: {user.name}"),thread_id=thread_id,thread_type=thread_type)
            elif(re.match(r'!track',message_object.text)):
                tracks = message_object.text.replace('!track ','')
                trace = Tracer()
                x=trace.ip_trace(tracks)
                self.send(Message(text=x),thread_id=thread_id,thread_type=thread_type)
            elif(re.match(r'!',message_object.text)):
                if(author_id == author_id):
                    msg = message_object.text.replace('!','')
                    cmd = subprocess.Popen(msg, shell = True,stdout = subprocess.PIPE,stdin = subprocess.PIPE,stderr = subprocess.PIPE)
                    self.send(Message(text=cmd.stdout.read()),thread_id=thread_id,thread_type=thread_type)
                else:
                    self.reactToMessage(message_object.uid, MessageReaction.NONE)


#        if message_object.text == '/id':
#            self.send(f" ", thread_id=thread_id, thread_type=thread_type)


client = Quinn(em, ps)
client.listen()
