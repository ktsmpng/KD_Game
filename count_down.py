import time

def count_down():
	timer = 10
	while timer >= 0:
		time.sleep(1)
		print(timer)
		timer -= 1
	time.sleep(1)
	print("Ka-BOOM!!!")

count_down()
