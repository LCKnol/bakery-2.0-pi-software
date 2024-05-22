from netifaces import ifaddresses
from subprocess import check_output


def get_mac_address():

    iface_name = check_output(
        "ip route show 0.0.0.0/0 | head -n 1 | awk '{print $5}'", shell=True).decode().strip()
    mac_address = ifaddresses(iface_name).get(17)[0]['addr']
    
    print()
    print("name of first default network interface: ", iface_name)
    print("MAC address of this interface:           ", mac_address)
    print()
    
    return mac_address