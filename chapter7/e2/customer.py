from chapter7.e2.connection import Connection
from chapter7.e2.speaker import SpeakerInterface, Message


class Customer(SpeakerInterface):
    def __init__(self):
        self.connection = None

    def call(self, target):
        print("Customer: I'm calling...")
        self.connection: Connection = target.connect(caller=self)

    def speak(self, msg: str):
        print("Customer:", msg)
        message = Message(self, msg)
        self.connection.send(message)

    def receive(self, msg: str):
        pass
