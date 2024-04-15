import time
import sys
loadingwidth = 22
quittingwidth = 22
print('Welcome to blinmaker')
print('Blinmaker is loading...')
#Some loading bar from stack overflow cause im lazy to make it myself ('https://stackoverflow.com/questions/3160699/python-progress-bar')
sys.stdout.write("[%s]" % (" " * loadingwidth))
sys.stdout.flush()
sys.stdout.write("\b" * (loadingwidth+1))
for i in range(loadingwidth):
time.sleep(0.1)
sys.stdout.write("-")
sys.stdout.flush()
sys.stdout.write("]\n")
print('')
def math(milk, flour, eggs):
minMilk = int(200)
minFlour = int(100)
minEggs = int(1)
milk = int(milk)
flour = int(flour)
eggs = int(eggs)
if milk < minMilk:
print('Not enough milk')
pass
elif flour < minFlour:
print('Not enough flour')
pass
elif eggs < minEggs:
print('Not enough eggs')
pass
portmilk = milk / minMilk
portflour = flour / minFlour
porteggs = eggs / minEggs
if portmilk <= portflour and portmilk <= porteggs:
return int(portmilk)
elif portflour <= portmilk and portflour <= porteggs:
return int(portflour)
elif porteggs <= portmilk and porteggs <= portflour:
return int(porteggs)
print('How much milk in mililiters do you have?')
milk = input('')
print('How much flour in grams do you have?')
flour = input('')
print('How many eggs do you have?')
eggs = input('')
a = math(milk,flour,eggs)
if a == 1:
egg = 'egg'
else:
egg = 'eggs'
print(f'You can make {a*4} blins')
print('')
print(f'You will need {200*a} mililiters of milk')
print(f'You will need {100*a} grams of flour')
print(f'You will need {1*a} {egg}')
time.sleep(1)
print('')
print('Приятного аппетита') #If you don't know russian, Приятного аппетита translates to 'Enjoy your meal'
print('Blinmaker shutting down...')
sys.stdout.write("[%s]" % (" " * quittingwidth))
sys.stdout.flush()
sys.stdout.write("\b" * (quittingwidth+1))
for i in range(quittingwidth):
time.sleep(0.05)
sys.stdout.write("-")
sys.stdout.flush()
sys.stdout.write("]\n")