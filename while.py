# import the mean function to laterwok out the average of total numbers entered
from statistics import mean

#ask user for a number and instuct them to enter -1 to calculate average. 
number = int(input("please enter the numbers.\nEnter -1 to calcu;ate average of numbers "))

#creat a variablel with empty list to store user inputs
number_list = [number,]

#create a while loop to check number is more than -1 and prompt user enter another number 
while number > -1:
    next_number = int(input("Enter next number: "))

#add and store user input inlist
    number_list.append(next_number)

#creat an if statment to check if number entered is equal to -1
    if next_number == -1:
#When number entered is -1, calculate the average of total numbers entered convert result to a string and print result
        print('the average of the total numbers entered is: ' + str(mean(number_list)))
        break
