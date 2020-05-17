import socket as py_socket
from abc import abstractmethod, ABC
from dataclasses import dataclass
from typing import Dict, Optional, List

from utilities import SequenceGenerator, IdGenerator


@dataclass
class Session:
    socket: py_socket.socket
    address: tuple
    id: Optional[int] = None
    user_name: str = ""

    def set_name(self, name: str):
        self.user_name = name

    def receive(self):
        return self.socket.recv(4096).decode()

    def send(self, msg: str):
        return self.socket.send(msg.encode())

    def close(self):
        return self.socket.close()


class SessionManager:
    def __init__(self, repository: "SessionRepository" = None):
        if repository is None:
            repository = InMemorySessionRepository()

        self.session_repository = repository

    def get_sessions(self) -> List[Session]:
        return self.session_repository.get_all()

    def join(self, session: Session) -> None:
        self.session_repository.add(session)

    def leave(self, session: Session) -> None:
        session.close()
        self.session_repository.remove(session)


class SessionRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Session]:
        pass

    @abstractmethod
    def add(self, session: Session) -> Session:
        pass

    @abstractmethod
    def remove(self, session: Session) -> None:
        pass


class InMemorySessionRepository(SessionRepository):
    id_generator: IdGenerator
    sessions: Dict[int, Session]

    def __init__(self, id_generator: IdGenerator = None):
        if id_generator is None:
            id_generator = SequenceGenerator()

        self.id_generator = id_generator
        self.sessions = {}

    def get_all(self) -> List[Session]:
        return list(self.sessions.values())

    def add(self, session: Session) -> Session:
        session.id = self.id_generator.generate()

        self.sessions[session.id] = session

        return session

    def remove(self, session: Session) -> None:
        if not getattr(session, "id"):
            raise ValueError("Session could not be removed. Id does not exist.")
        del self.sessions[session.id]
