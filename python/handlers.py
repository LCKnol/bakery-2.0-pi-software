from manager import Manager
from mac_address import get_mac_address
from command_executor import execute_command

# init-pi
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

# set-dashboard
def handle_set_dashboard(body: dict) -> None:
    url = body['url']
    # Unsubscribe from init-pi
    if url:
        print(f"Opening browser on {url}")
        # Subscribe to pi-listener
        execute_command(f'python -m webbrowser "{url}"')
        print("subscribed to pi-listener")
    else:
        print("this pi has no url")


if __name__ == "__main__":
    try:
        body = {'url': 'https://www.youtube.com/watch?v=wPElVpR1rwA'}
        handle_set_dashboard(body)
    except KeyboardInterrupt:
        print("Program stopped by user.")