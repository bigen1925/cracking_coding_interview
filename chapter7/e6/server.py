import socket as py_socket
import threading
import traceback

from message import MessageManager
from session import SessionManager, Session


# noinspection DuplicatedCode
class Server:
    def __init__(self):
        self.session_manager = SessionManager()
        self.message_manager = MessageManager(session_manager=self.session_manager)

    def serve(self):
        server_socket = py_socket.socket(py_socket.AF_INET, py_socket.SOCK_STREAM)
        server_socket.setsockopt(py_socket.SOL_SOCKET, py_socket.SO_REUSEADDR, 1)
        server_socket.bind(("localhost", 8001))
        server_socket.listen(5)
        print(f"server: listening.")
        while True:
            client_socket, address = server_socket.accept()
            client_socket.settimeout(300)
            print("server: accepted.")

            session = Session(client_socket, address)
            receiver = ReceiverThread(
                session, self.session_manager, self.message_manager
            )

            receiver.start()


class ReceiverThread(threading.Thread):
    def __init__(
        self,
        session: Session,
        session_manager: SessionManager,
        message_manager: MessageManager,
        *args,
        **kwargs,
    ):
        self.session = session
        self.session_manager = session_manager
        self.message_manager = message_manager

        self.session_manager.join(session)

        super().__init__(*args, **kwargs)

    def run(self):
        self.send_server_announce("please enter your name.")

        name = self.session.receive().strip()
        self.session.set_name(name)

        self.send_server_announce(f'Welcome "{name}"!')
        self.message_manager.hello(self.session)

        while True:
            try:
                if received := self.session.receive():
                    self.message_manager.speak(body=received, session=self.session)
                else:
                    print(f"(Session {self.session.id}) Client closed connection.")
                    break

            except Exception as e:
                print(f"(Session {self.session.id}) Receiver caught exception :: {e}")
                traceback.print_exc()
                break

        self.session_manager.leave(self.session)
        self.message_manager.bye(self.session)
        print(f"(Session {self.session.id}) Receiver will terminate.")

    def send_server_announce(self, msg: str):
        self.session.socket.send(f"========= SERVER: {msg}=========\n".encode())


if __name__ == "__main__":
    Server().serve()
