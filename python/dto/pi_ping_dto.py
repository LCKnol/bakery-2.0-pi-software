class PiPingDto:
    def __init__(self, mac_address: str) -> None:
        self.macAddress: str = mac_address

    def get_mac_adress(self) -> str:
        return self.macAddress

    def set_mac_adress(self, mac_address: str) -> None:
        self.macAddress = mac_address