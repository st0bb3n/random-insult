from pynput.keyboard import Key, Controller
import random
import time

kb = Controller()

fh = open('insults.txt', 'r')					#file handling
words = [line.rstrip() for line in fh]			#generates array from txt file
fh.close()										#closes file handling

while True:										#types out random insult from txt file and sends it
    insult = random.choice(words)
    kb.type(insult + '\n')
    time.sleep(1)								#delay