class PiSignUpDto:
    def __init__(self, mac_address: str, ip_address: str) -> None:
        self.macAddress: str = mac_address
        self.ipAddress: str = ip_address

    def get_mac_adress(self) -> str:
        return self.macAddress

    def set_mac_adress(self, mac_address: str) -> None:
        self.macAddress = mac_address

    def get_ip_address(self) -> str:
        return self.ipAddress
    
    def set_ip_address(self, ip_address: str) -> None:
        self.ipAddress = ip_address