from typing import Callable
from stomp_ws.frame import Frame
import json
class Response:
    def __init__(self) -> None:
        self.handlers = {}
        return
    
    def add_handler(self, instruction: str, handler: Callable[[dict], None]) -> None:
        self.handlers[instruction] = handler
        return
    
    def remove_handler(self, instruction: str) -> None:
        self.handlers.pop(instruction)
        return

    def handle_response(self, frame: Frame) -> None:
        command = frame.command
        headers = frame.headers
        body = json.loads(frame.body)
        instruction = body.get('instruction')
        if self.handlers.get(instruction):
            handler_func = self.handlers.get(instruction)
            handler_func(body.get('body'))
        return