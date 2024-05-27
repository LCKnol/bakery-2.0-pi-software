import os


def set_refresh_rate(refresh_rate: int):
    if (refresh_rate > 0):
        with open("/home/colossuspi/Documents/refresh_rate.txt", "w") as file:
            file.write(str(refresh_rate))

    else:
        if os.path.exists("refresh_rate.txt"):
            os.remove("refresh_rate.txt")
