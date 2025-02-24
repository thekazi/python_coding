import time

def timer():
	seconds = int(input("Enter the countdown in seconds: "))
	for i in range(seconds, 0, -1):
		print(f"Time left: {i} seconds")
		time.sleep(1)
	print("Time's up!")

timer()
