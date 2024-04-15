import time
import sys

toolbar_width = 20
tool_width_exit = 25

print('Welcome')
print('Blinmaker is starting')

#Some loading bar from stack overflow cause im lazy to make it myself ('https://stackoverflow.com/questions/3160699/python-progress-bar')
sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

for i in range(toolbar_width):
    time.sleep(0.1)
    sys.stdout.write("-")
    sys.stdout.flush()

sys.stdout.write("]\n") # this ends the progress bar

minMilk = int(200) #in ml
minFlour = int(100) #in grams
minEggs = int(1) #in well eggs

print('How much milk in ml do you have?')
milk = input('')
milk = int(milk)

print('How much flour in grams do you have?')
flour = input('')
flour = int(flour)

print('How many eggs do you have?')
eggs = input('')
eggs = int(eggs)

if milk < minMilk:
    print('You don\'t have enough milk')
elif flour < minFlour:
    print('You dont\'t have enough flour')
elif eggs < minEggs:
    print('you don\'t have enough eggs')

portflour = flour / minFlour
portflour = int(portflour)
## DEBUG:
#print(f'You have enough flour to make {portflour} blins')

portmilk = milk / minMilk
portmilk = int(portmilk)
## DEBUG:
#print(f'You have enough milk to make {portmilk} blins')

porteggs = eggs / minEggs
porteggs = int(porteggs)
## DEBUG:
#print(f'You have enough eggs to make {porteggs} blins')

if portflour <= portmilk and portflour <= porteggs:
    smallest = portflour
elif portmilk <= portflour and portmilk <= porteggs:
    smallest = portmilk
else:
    smallest = porteggs
print('')
print(f'You can make {smallest*4} blins')
print('')
print(f'You will need {smallest*minMilk} milk')
print(f'You will need {smallest*minFlour} flour')
print(f'You will need {smallest*minEggs} eggs')
print('')
print('Приятного аппетита') #If you don't know russian, Приятного аппетита translates to 'Enjoy your meal'
print('Blinmaker shutting down...')

sys.stdout.write("[%s]" % (" " * tool_width_exit))
sys.stdout.flush()
sys.stdout.write("\b" * (tool_width_exit+1)) # return to start of line, after '['

for i in range(tool_width_exit):
    time.sleep(0.05) # Little fast than the loading bar
    sys.stdout.write("-")
    sys.stdout.flush()

sys.stdout.write("]\n") # this ends the progress bar