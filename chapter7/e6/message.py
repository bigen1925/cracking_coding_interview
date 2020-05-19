from abc import ABC
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Optional

from session import SessionManager, Session
from utilities import SequenceGenerator, IdGenerator


@dataclass()
class Message:
    body: str
    sender: str
    send_at: Optional[datetime] = None


class MessageManager:
    message_repository: "MessageRepository"
    session_manager: SessionManager

    def __init__(
        self, session_manager: SessionManager, repository: "MessageRepository" = None
    ):
        if repository is None:
            repository = InMemoryMessageRepository()

        self.message_repository = repository
        self.session_manager = session_manager

    def store(self, message: Message) -> None:
        self.message_repository.add(message)

    def deliver(self, message: Message):
        message.send_at = datetime.now()

        sessions = self.session_manager.get_sessions()

        for session in sessions:
            content = f"{message.sender} : {message.body}"
            session.send(content)

    def speak(self, body: str, session: Session) -> None:
        message = Message(body=body, sender=session.user_name)
        self.deliver(message)
        self.store(message)

    def hello(self, session: Session) -> None:
        message = Message(
            body=f"'{session.user_name}' joined to us!\n", sender="System"
        )
        self.deliver(message)
        self.store(message)

    def bye(self, session: Session) -> None:
        message = Message(
            body=f"'{session.user_name}' leaved from us!\n", sender="System"
        )
        self.deliver(message)
        self.store(message)


class MessageRepository(ABC):
    def add(self, message: Message) -> Message:
        pass


class InMemoryMessageRepository(MessageRepository):
    id_generator: IdGenerator
    messages: Dict[int, Message]

    def __init__(self):
        self.id_generator = SequenceGenerator()
        self.messages = {}

    def add(self, message: Message) -> None:
        message.id = self.id_generator.generate()

        self.messages[message.id] = message
