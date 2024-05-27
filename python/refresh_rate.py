def set_refresh_rate(refresh_rate: int):
    file_path = "/home/colossuspi/Documents/refresh_rate.txt"

    with open(file_path, "w") as file:
        file.write(str(refresh_rate))
