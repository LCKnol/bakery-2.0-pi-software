

def handle_pi_init(body: dict) -> None:
    mac_address = body['macAddress']
    accepted = body['isAccepted']

    if mac_address is not None:
        if accepted:
            # TODO subscribe to working pi's
            print("this pi got accepted")
        else:
            print("this pi got rejected")
