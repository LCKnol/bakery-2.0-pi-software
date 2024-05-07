from stomp_ws.client import Client
from response import Response
import asyncio
import json


def print_frame(frame):
    body = json.loads(frame.body)
    print(body['instruction'], body['body'])


async def main():
    response = Response()
    response.add_handler("sign up", lambda body: {print(body)})

    # open transport
    client = Client("ws://localhost:8080/chat")

    # connect to the endpoint
    client.connect(timeout=0)

    # subscribe channel
    sub_id, unsubscribe = client.subscribe("/topic/greetings", callback=response.handle_response)

    await asyncio.sleep(300)

    # client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
