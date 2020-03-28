from abc import abstractmethod, ABC
from typing import Optional, Union

from chapter7.e2.connection import Connection
from chapter7.e2.customer import Customer
from chapter7.e2.speaker import SpeakerInterface, Message


class CallCenter:
    def __init__(self):
        self.respondents = [Respondent()]
        self.managers = [Manager()]
        self.director = [Director()]

    def connect(self, caller: SpeakerInterface):
        connection = Connection(receivers=[caller])
        answerer = self.dispatch_call()

        connection.add_receiver(answerer)
        answerer.join(connection)

        return connection

    def dispatch_call(self) -> "Respondent":
        return self.respondents[0]

    def dispatch_boss(self) -> Union["Manager", "Director"]:
        if len(self.managers) > 0:
            return self.dispatch_manager()
        else:
            return self.dispatch_director()

    def dispatch_manager(self) -> "Manager":
        return self.managers[0]

    def dispatch_director(self) -> "Director":
        return self.director[0]


class Employee(SpeakerInterface, ABC):
    def __init__(self):
        super().__init__()
        self.connection: Optional[Connection] = None

    def join(self, connection: Connection):
        self.connection = connection
        self.connection.add_receiver(self)
        self.speak(f"Hi, I'm a {self.__class__.__name__}.")

    def leave(self):
        self.connection.remove_receiver(self)
        self.connection = None

    def speak(self, msg: str) -> None:
        print(f"{self.__class__.__name__}:", msg)
        self.connection.send(Message(self, msg))

    @abstractmethod
    def receive(self, msg: "Message") -> None:
        pass


class Respondent(Employee):
    def receive(self, msg: Message) -> None:
        if isinstance(msg.speaker, Customer):
            if "fuck" in msg.body:
                self.speak("I will put my boss on the phone.")
                self.escalate()

            else:
                self.speak("I'm Sorry.")

    def escalate(self):
        manager = CALL_CENTER.dispatch_boss()
        manager.join(self.connection)
        self.leave()


class Manager(Employee):
    def receive(self, msg: "Message") -> None:
        if isinstance(msg.speaker, Customer):
            if "fuck" in msg.body:
                self.speak("I will put our director on the phone.")
                self.escalate()

            else:
                self.speak("I'm Sorry")

    def escalate(self):
        director = CALL_CENTER.dispatch_director()
        director.join(self.connection)
        self.leave()


class Director(Employee):
    def receive(self, msg: "Message") -> None:
        if isinstance(msg.speaker, Customer):
            if "fuck" in msg.body:
                self.speak(
                    "You speaks a little dirt language. You don't seem our customer. Good Bye."
                )

                self.leave()
            else:
                self.speak("Excuse me ?")


CALL_CENTER = CallCenter()
