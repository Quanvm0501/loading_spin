def loading_text(times_loop):
    from time import sleep as TIME_SLEEP
    for _ in range(times_loop):
        for tmp1 in ["\\", "|", "/", "-"]:
            print(tmp1, end="\r")
            TIME_SLEEP(0.1)
    print("\r", end = " ")
    print("\r", end = "")