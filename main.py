import loading_text
class Error(Exception):
	pass

class Loading_Failed(Error):
	pass

def loading_spin(text: str, times):
	from time import sleep as TIME_SLEEP
	for _ in range(times_loop):
		for tmp1 in ["\\", "|", "/", "-"]:
			print(text, tmp1, end="\r")
			TIME_SLEEP(0.1)
	print(text,"\r", end = " ")
	print(text,"\r", end = "")
	return True

if __name__ == "__main__":
	tmp = loading_spin("Text", 10)
	print("Finished!") if tmp == True else raise Loading_Failed("Loading Spin Text Failed!")
