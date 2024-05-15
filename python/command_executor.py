from subprocess import call 

def execute_command(command: str) -> None:

    call(command, shell=True)
