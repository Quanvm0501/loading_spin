import loading_text
def loading_spin(text: str, times):
	from time import sleep as TIME_SLEEP
    for _ in range(times_loop):
		for tmp1 in ["\\", "|", "/", "-"]:
			print(text, tmp1, end="\r")
			TIME_SLEEP(0.1)
	print(text,"\r", end = " ")
	print(text,"\r", end = "")
if __name__ == "__main__":
	loading_spin("Text", 10)
