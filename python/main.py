import asyncio
from manager import Manager
from dto.pi_sign_up_dto import PiSignUpDto
from handlers import handle_pi_init, handle_set_dashboard
from mac_address import get_mac_address
import asyncio
import json

# for testing
mac = get_mac_address()


async def main():
    # add all handlers
    response = Manager().get_response_instance()
    response.add_handler("init-pi", handle_pi_init)
    response.add_handler("set-dashboard", handle_set_dashboard)

    # open transport
    client = Manager().get_client_instance("ws://localhost:8080/chat")

    # subscribe to back-end pending
    sub_id, unsubscribe = client.subscribe(f"/topic/init-pi/{mac}", callback=response.handle_response)
    response.add_subscription(sub_id=sub_id, unsubscribe=unsubscribe, path=f"/topic/init-pi/{mac}")

    # send sign-up call to back-end
    client.send("/app/sign-up-pi", body=json.dumps(PiSignUpDto(mac).__dict__))

    print("signed up, going to sleep now..")
    try:
        while True:
            await asyncio.sleep(300)
    except asyncio.CancelledError:
        print("Cancelled by KeyboardInterrupt, cleaning up")
        raise
    finally:
        Manager.exit()
        print("Cleanup complete.")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Program stopped by user.")
