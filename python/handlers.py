from manager import Manager
from mac_address import get_mac_address
from command_executor import execute_command
from platform import system

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
        client = Manager().get_client_instance("ws://colossus.loca.lt/chat")
        sub_id, unsubscribe = client.subscribe(f"/topic/pi-listener/{mac_address}", callback=response.handle_response)
        response.add_subscription(sub_id=sub_id, unsubscribe=unsubscribe, path=f"/topic/pi-listener/{mac_address}")
        print("subscribed to pi-listener")

    else:
        print("this pi got rejected")

# set-dashboard
def handle_set_dashboard(body: dict) -> None:
    print("Called handler setdashboard")
    url = body['url']
    # Unsubscribe from init-pi
    if url:
        print(f"Opening browser on {url}")
        # Subscribe to pi-listener
        if system() == "Windows":
         execute_command("taskkill /F /IM chrome.exe")
         execute_command(f'start chrome --kiosk {url}')
        else:
         execute_command("pkill -e -i 'chrome|firefox'")
         execute_command(f'chromium-browser --kiosk {url}')
         print("subscribed to pi-listener")
    else:
        print("this pi has no url")
