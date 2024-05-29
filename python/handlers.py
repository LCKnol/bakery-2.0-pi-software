from manager import Manager
from mac_address import get_mac_address
from command_executor import execute_command
from platform import system
from connection import connectionUrl
from dto.pi_ping_dto import PiPingDto
from refresh_rate import set_refresh_rate
import json


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
        client = Manager().get_client_instance(connectionUrl)
        sub_id, unsubscribe = client.subscribe(
            f"/topic/pi-listener/{mac_address}", callback=response.handle_response)
        response.add_subscription(
            sub_id=sub_id, unsubscribe=unsubscribe, path=f"/topic/pi-listener/{mac_address}")
        print("subscribed to pi-listener")

    else:
        print("this pi got rejected")


# set-dashboard
def handle_set_dashboard(body: dict) -> None:
    print("Called handler setDashboard")
    url = body['url']
    refresh = body['refresh']
    # Unsubscribe from init-pi
    if url:
        print(f"Opening browser on {url}")
        # Subscribe to pi-listener
        if system() == "Windows":
            try:
                execute_command("taskkill /F /IM chrome.exe")
            except:
                print("error while closing browser")
            execute_command(f'start chrome --kiosk {url}')
        else:
            try:
                execute_command("pkill -f chromium-browser")
            except:
                print("error while closing browser")
            command = f'nohup chromium-browser --DISPLAY=:0 --no-sandbox --kiosk {url} &'
            execute_command(command)
            print("browser thing is afgesloten")
    else:
        print("this pi has no url")

    if refresh is not None:
        set_refresh_rate(refresh)
    else:
        print("No value for refresh rate was provided")


def handle_reboot_pi(_: dict) -> None:
    print("Pi is rebooting.")
    execute_command("sudo reboot")


def handle_ping_pi(_: dict) -> None:
    print("This pi got pinged by back-end")
    client = Manager().get_client_instance(connectionUrl)
    mac = get_mac_address()
    client.send("/app/ping", body=json.dumps(PiPingDto(mac).__dict__))
    print("Pi sent ping response to back-end")


def handle_set_tv(body: dict) -> None:
    print("Called handler set tv")
    option = body['option']
    if option == True:
        execute_command("echo 'on 0' | cec-client -s -d 1")
        print("Tv is turning on")
    elif option == False:
        execute_command("echo 'standby 0' | cec-client -s -d 1")
        print("Tv is turning off")


def update_pi(_: dict) -> None:
    execute_command("sudo apt update -y")
    print("Pi got updated now starting upgrade")
    execute_command("sudo apt upgrade -y")
    print("This pi got updated and upgraded")
