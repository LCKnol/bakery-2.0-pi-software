from netifaces import ifaddresses
from subprocess import check_output


def get_ip_address():

    # iface_name = check_output(
    #     "ip route show 0.0.0.0/0 | head -n 1 | awk '{print $5}'", shell=True).decode().strip()
    # ip_address = ifaddresses(iface_name).get(2)[0]['addr']
    #
    # print()
    # print("name of first default network interface: ", iface_name)
    # print("IP address of this interface:            ", ip_address)
    # print()

    # return ip_address
    return "1.2.3.4"