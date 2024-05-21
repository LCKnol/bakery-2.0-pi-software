from netifaces import ifaddresses
from subprocess import check_output


def get_ip_address():

    ifaceName = check_output(
        "ip route show 0.0.0.0/0 | head -n 1 | awk '{print $5}'", shell=True).decode().strip()
    ipAddress = ifaddresses(ifaceName).get(2)[0]['addr']

    print()
    print("name of first default network interface: ", ifaceName)
    print("IP address of this interface:            ", ipAddress)
    print()

    return ifaddresses('wlp3s0').get(2)[0]['addr']
