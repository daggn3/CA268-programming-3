from _thread import start_new_thread

threadID = 1

def factorial(n):
	global threadID

	if n < 1:
		print ("{}: {}".format("Thread", threadID))
		threadID += 1
		return 1
	else:
		returnNumber = n * factorial(n - 1)
		print(str(n) + "! = " + str(returnNumber))

		return returnNumber

start_new_thread(factorial(5, ))
start_new_thread(factorial(6, ))

c = raw_input("Waiting for thread to return... \n")