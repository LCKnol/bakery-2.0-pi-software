from command_executor import execute_command


def set_refresh_rate(refresh_rate: int):
    execute_command(f'export BROWSER_REFRESH_RATE={int(refresh_rate)}')