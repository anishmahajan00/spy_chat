from datetime import datetime

class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('Anish', 'Mr.', 21, 4.7)

friend_one = Spy('Deepak', 'Mr.', 19, 21)
friend_two = Spy('Aneesh', 'Ms.', 21, 19)
friend_three = Spy('Ankush', 'Dr.', 20, 27)


friends = [friend_one, friend_two, friend_three]

