from subprocess import call 
import threading

def execute_command(command: str) -> None:
    thread = threading.Thread(target=call(command, shell=True))
    thread.start
    return
    
