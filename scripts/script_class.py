from flask_socketio import SocketIO
from typing import Callable


class Script:

    def __init__(self, name : str, is_a_page : bool = False) -> None:
        self.name : str = name
        self.is_a_page : bool = is_a_page
        self.socketio : SocketIO | None = None
        self.socketio_events : list[tuple[str, Callable]] = []

    def action(self) -> str:
        print(f"[{self.name}] No action defined")
        return ''

    def add_socket_event(self, event_name: str, func: Callable) -> None:
        self.socketio_events.append((f"{self.name}.{event_name}", func))

    def init_socketio_events(self, socketio: SocketIO) -> None:
        self.socketio = socketio
        for event in self.socketio_events:
            self.socketio.on_event(event[0], event[1])

