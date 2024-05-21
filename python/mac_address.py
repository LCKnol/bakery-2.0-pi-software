from netifaces import ifaddresses
from subprocess import check_output


def get_mac_address():

    ifaceName = check_output(
        "ip route show 0.0.0.0/0 | head -n 1 | awk '{print $5}'", shell=True).decode().strip()
    macAddress = ifaddresses(ifaceName).get(17)[0]['addr']

    print()
    print("name of first default network interface: ", ifaceName)
    print("MAC address of this interface:           ", macAddress)
    print()

    return macAddress
