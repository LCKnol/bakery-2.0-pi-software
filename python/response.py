from typing import Callable
from stomp_ws.frame import Frame
import json


class Response:
    def __init__(self) -> None:
        self.handlers = {}
        self.subs = {}
        return
    
    def add_handler(self, instruction: str, handler: Callable[[dict], None]) -> None:
        self.handlers[instruction] = handler
        return
    
    def remove_handler(self, instruction: str) -> None:
        self.handlers.pop(instruction)
        return

    def add_subscription(self, sub_id: int, unsubscribe, path: str):
        self.subs[path] = [sub_id, unsubscribe]
        return

    def handle_response(self, frame: Frame) -> None:
        print("got new response :)")
        command = frame.command
        headers = frame.headers
        body = json.loads(frame.body)
        instruction = body.get('instruction')
        if self.handlers.get(instruction):
            handler_func = self.handlers.get(instruction)
            handler_func(body.get('body'))
        return

    def unsubscribe(self, path: str) -> None:
        subscription = self.subs.get(path)
        unsub = subscription[1]
        unsub()

    def unsubscribe_all(self) -> None:
        for key in self.subs:
            unsub = self.subs.get(key)[1]
            unsub()
        return

