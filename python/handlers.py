from manager import Manager
from mac_address import get_mac_address


def handle_pi_init(body: dict) -> None:
    accepted = body['isAccepted']

    mac_address = get_mac_address()

    # Unsubscribe from init-pi
    response = Manager().get_response_instance()
    response.unsubscribe(f"/topic/init-pi/{mac_address}")

    if accepted:
        print("this pi got accepted")

        # Subscribe to pi-listener
        client = Manager().get_client_instance("ws://localhost:8080/chat")
        client.subscribe(f"pi-listener/{mac_address}", callback=response.handle_response)
        print("subscribed to pi-listener")

    else:
        print("this pi got rejected")


