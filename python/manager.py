from python.stomp_ws.client import Client
from response import Response


class Manager:
    response: Response = None
    clients: dict[str, Client] = {}

    @classmethod
    def get_response_instance(cls) -> Response:
        if cls.response is None:
            cls.response = Response()
        return cls.response

    @classmethod
    def get_client_instance(cls, url: str) -> Client:
        if url not in cls.clients:
            new_client = Client(url)
            new_client.connect(timeout=0)
            cls.clients[url] = new_client

        return cls.clients[url]


