import asyncio

from stomp_ws.client import Client
from handle_response import Response
from dto.pi_sign_up_dto import PiSignUpDto
from handlers import handle_pi_init
import asyncio
import json

# for testing
mac = "test:mac:address:2"


async def main():
    response = Response()
    response.add_handler("init-pi", handle_pi_init)

    # open transport
    client = Client("ws://localhost:8080/chat")

    # connect to the endpoint
    client.connect(timeout=0)

    # subscribe to back-end pending
    sub_id, unsubscribe = client.subscribe(f"/topic/init-pi/{mac}", callback=response.handle_response)
    response.add_subscription(sub_id=sub_id, unsubscribe=unsubscribe, path=f"/topic/init-pi/{mac}")

    # send sign-up call to back-end
    client.send("/app/sign-up-pi", body=json.dumps(PiSignUpDto(mac).__dict__))
    #
    await asyncio.sleep(300)
    #
    # client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
