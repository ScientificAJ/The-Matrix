import random
import string
import time
import sys
from termcolor import colored, cprint
from playsound import playsound
# TODO - Update:- Automatically on after 10 minutes idle time																																																																																																																																																																																																																																																															")
print("Inititiating the Matrix")
time.sleep(1)
print("...")
time.sleep(1)
print("...")
time.sleep(1)
print("...")
time.sleep(1)
print("Done!", colored("😈", "red"))
playsound("/home/AruJ/Downloads/Matrix.mp3")
playsound("/home/AruJ/Downloads/Trinity.mp3")
time.sleep(0.5)
duration = 14
while 1:
	start_time = time.time()
	playsound("/home/AruJ/Downloads/TheMatrix.mp3", block=False)
	while time.time() - start_time < duration:
		choose = random.choice([1, 2])
		letters = str(random.choice(["  ", " ", "                                 ", "         ", "                                                   ", "                                                                                                               ", "                                                     ", "                                                                                           ", "                                                                       ", "																									", "																			", "													"]) + random.choice(string.ascii_letters))
		time.sleep(0.00000001)
		if choose == 1:
			print(colored(letters, random.choice(["green", "blue"])))
		else:
			print(colored(random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), random.choice(["green", "blue"])))




