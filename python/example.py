from stomp_ws.client import Client
from handle_response import Response
import time
import json


def print_frame(frame):
    body = json.loads(frame.body)
    print(body['instruction'], body['body'])


def main():
    response = Response()
    response.add_handler("sign up", lambda body: {print(body)})

    # open transport
    client = Client("ws://localhost:8080/chat")

    # connect to the endpoint
    client.connect(timeout=0)

    # subscribe channel
    sub_id, unsubscribe = client.subscribe("/topic/greetings", callback=response.handle_response)
    
    # send msg to channel
    client.send("/app/greetings", body="Koen")

    time.sleep(3)

    # client.disconnect()
    
if __name__ == "__main__":
    main()