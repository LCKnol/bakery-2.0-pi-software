from command_executor import execute_command


def set_refresh_rate(refresh_rate: int):
    if(refresh_rate > 0):
        execute_command(f'export BROWSER_REFRESH_RATE={int(refresh_rate)}')
    else:
        execute_command(f'unset BROWSER_REFRESH_RATE')
