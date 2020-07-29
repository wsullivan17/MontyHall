import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import random

from Door_Class import Doors

#This is a little program to test the Monty Hall problem with Python.
#Monty Hall problem: Under the standard assumptions, contestants who switch have a 2/3 chance of winning the car, 
#while contestants who stick to their initial choice have only a 1/3 chance. https://en.wikipedia.org/wiki/Monty_Hall_problem
#Willard Sullivan, 7/27/2020

print("Monty Hall says..... ")
runs = int(input("How many Let's Make a Deal games do you want to play? Enter an integer. "))
guesses = np.full(runs, 0) #0 = first try, 1 = no switch, 2 = switch (has the car)

no_switch = 0
switch = 0

a = 0
b = 0
c = 0

for x in range(0, runs):

    car =  np.random.randint(2, size=3) #used to generate a random door which has the car. 1 = car, 0 = no car.
    car_sum = np.sum(car)

    while car_sum != 1:
        car = np.random.randint(2, size=3)
        car_sum = np.sum(car)
        
    #print(car)

    doora = Doors("doora", "a", car[0])
    doorb = Doors("doorb", "b", car[1])
    doorc = Doors("doorc", "c", car[2])

    doors = ["a", "b", "c"]
    doors_id = [doora, doorb, doorc]

    choice_one = random.choice(doors) #chooses a door - a, b, or c.
    print(doora.car)
    print(doorb.car)
    print(doorc.car)
    print(choice_one)
    print(doors)
    
    
    for y in doors_id:   
        if choice_one == y.ID:
            
            remove = random.choice(doors)

            for w in doors_id:
                if w.car == 1:
                    doors.remove(w.ID)
                elif w.ID == y.ID:
                    doors.remove(w.ID)
                
            remove = random.choice(doors)
            print(remove)
            doors = ["a", "b", "c"]                   
            doors.remove(remove)

            choice_two = random.choice(doors)
            print(doors)
            print(choice_two)

            for z in doors_id:
                if choice_one == z.ID and choice_two == z.ID: #no switch
                    if z.car == 1 and choice_two == z.ID: #no switch - car
                        no_switch += 1
                        print("Car with no switch. ")
                    
                    elif z.car == 0 and choice_two == z.ID: #no switch - no car
                        switch += 1
                        print("Car with switch. ")
                    
                elif choice_one != z.ID or choice_two != z.ID: #switch made
                    if z.car == 1 and choice_two == z.ID: #switch - car
                        switch += 1
                        print("Car with switch. ")
                    
                    elif z.car == 0 and choice_two == z.ID: #switch - no car
                        no_switch += 1
                        print("Car with no switch. ")                   
    print("\n")    
    if doora.car == 1:
        a += 1
    elif doorb.car == 1:
        b += 1
    elif doorc.car == 1:
        c += 1
'''
print(a)
print(b)
print(c)
'''
no_switch = (no_switch/runs)*100
switch = (switch/runs)*100
print(no_switch)
print(switch)

#Pie chart 
labels = "Car with switch!", "Car with no switch!"
sizes = [switch, no_switch]

fig1, pie1 = plt.subplots()
pie1.pie(sizes, labels = labels, autopct='%1.1f%%')
pie1.set_title("Switch Versus No Switch Wins: " + str(runs) + " games.")
plt.show()

            
            

