#! /usr/bin/python3
import sys
from time import sleep
from random import shuffle

print('welcome to Arnav Rock-paper-scicor 1.1 game')

#waiting function
def wait(t):
	sleep(0.5)

# writing effect function
def write(s):
	for char in s:
		sleep(0.1)
		sys.stdout.write(char)
		sys.stdout.flush()
write('|||||||||||||||||||||||||||||||||||||||||||')
print('\n\n\n\n')
wait(1)
print('how to play-')
print('after rock paper scicor enter')
write('for scicor enter "s"\nfor paper enter "p"\nfor rock enter "r"\n')

while True:
	try:
		point = 0
		com_point = 0
		draw = 0
		k = int(input('number of times you want to play-'))
		number = k
		obj = ['rock', 'paper', 'scicor']
		print("let's play")
		while k>=1:
		    write('____________________\n')
		    shuffle(obj)
		    for i in obj:
		        print("rock..\n")
		        wait(1)
		        print("paper..\n")
		        wait(1)
		        print('scicor..\n')
		        play = input()
		        wait(1)
		        
		        # Draw
		        if i == 'rock' and play == 'r':
		            write('Draw\n\n')
		            draw+=1
		            break
		            
		        elif i == 'paper' and play == 'p':
		            write('Draw\n\n')
		            draw+=1
		            break
		            
		        elif i == 'scicor' and play =='s':
		            write('Draw\n\n')
		            draw+=1
		            break

		        # Win
		        elif i == 'rock' and play == 'p':
		            write('you win\n\n')
		            point+=1
		            print('your point-',point,'\n\n')
		            break
		        
		        elif i == 'paper' and play == 's':
		            write('you win\n\n')
		            point+=1
		            print('your point-',point,'\n\n')
		            break

		        elif i == 'scicor' and play == 'r':
		            write('you win\n\n')
		            point+=1
		            print('your point',point,'\n\n')
		            break
		            
		        #lose
		        elif i == 'rock' and play == 's':
		            write('you lose\n\n')
		            com_point+=1
		            print("computer's point",com_point,'\n\n')
		            break

		        elif i == 'paper' and play == 'r':
		            write('you lose\n\n')
		            com_point+=1
		            print("computer's point",com_point,'\n\n')
		            break

		        elif i == 'scicor' and play == 'p':
		            write('you lose\n\n')
		            com_point+=1
		            print("computer's point",com_point,'\n\n')
		            break
		        
		        elif i == 'e':
		            print('enter again for exit')
		            break
		        else:
		            print('wrong input :(')
		            print()
		            continue
		        print('computer makes---->',i,'\n\n')
		        	
		        
		    if play == 'e':
		        write('Bye thank u for play')
		        break
		    
		    k-=1

		print("\n\n\n ")
		write("Result")
		print("\ncomputer's point",com_point)
		print("Your point",point)
		print("Number time match draw",draw)
		print("Number of times you played-",number)
		if com_point<point:
		    print('\n\nyou win')
		    break
		elif com_point>point:
		    print('\n\ncomputer win')
		    break
		else:
		    print("\n\nmatch Draw")
		    break

	except ValueError:
		print('Invaild input :(\n\n')
		continue
