from abc import ABC, abstractmethod


class SpeakerInterface(ABC):
    @abstractmethod
    def speak(self, msg: "Message") -> None:
        pass

    @abstractmethod
    def receive(self, msg: "Message") -> None:
        pass


class Message:
    def __init__(self, speaker: SpeakerInterface, body: str):
        self.speaker: SpeakerInterface = speaker
        self.body: str = body
