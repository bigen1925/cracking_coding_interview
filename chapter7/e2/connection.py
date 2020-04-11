from copy import copy
from typing import Iterable, Dict

from chapter7.e2.speaker import SpeakerInterface, Message


class Connection:
    def __init__(self, receivers: Iterable[SpeakerInterface] = ()):
        self.receivers: Dict[int, SpeakerInterface] = {}

        for receiver in receivers:
            self.receivers[id(receiver)] = receiver

    def add_receiver(self, receiver: SpeakerInterface) -> None:
        self.receivers[id(receiver)] = receiver

    def remove_receiver(self, receiver: SpeakerInterface) -> None:
        if id(receiver) in self.receivers:
            del self.receivers[id(receiver)]

    def send(self, msg: Message) -> None:
        receivers = copy(self.receivers)

        if len(receivers) < 2:
            print("Connection: No one hear you.")

        for receiver in receivers.values():
            if receiver is not msg.speaker:
                receiver.receive(msg)
