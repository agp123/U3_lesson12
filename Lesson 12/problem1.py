import time 
import random

print('-' * 65)
print("Welcome to magic eight Ball")
print()

question = input ('What is your question? ')
time.sleep(0.7)
print('Shaking')
time.sleep(0.7)
print('...thinking...')
time.sleep(0.7)
print('...thinking...')
time.sleep(0.7)

choice = random.randint(1,6)

if choice == 1:
	print('yes')
elif choice == 2:
	print('no')
elif choice == 3:
	print('maybe')
elif choice == 4:
	print('ask later')
elif choice == 5:
	print('definitely NO!')
elif choice == 6:
	print('sureeeee....')

print('-' * 65)