#class Spy declaration
class Spy:
    def __init__(self,name,gender,salutation,age,rate):
        self.name=name
        self.gender=gender
        self.salutation=salutation
        self.age=age
        self.rate=rate
        self.online=True
        self.current_status=None
        self.chats=[]



#class chat_message declaration
class chat_Message:

    def __init__(self,message,time,sent_by_me):
        self.message = message
        self.time = time
        self.sent_by_me = sent_by_me



#object spy of class Spy for default user
spy=Spy('SAHIL','MALE','MR.',19,4.8)