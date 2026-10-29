def choose_parking_slot(number):

    for index in range(len(parking_space)):

        if index == number:
        
            parking_space[index] = '1'

         
def remove_parking_space(number):

    for index in range(len(parking_space)):
    
            if index == number:

                parking_space[index] = '0'


            
def choose_to_stop(word):

       if word  == 'no':

           return True
       else:
            return False
    

parking_space = ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']


while True:
    
    space = int(input("Hello, these are the parking slots avaialable, kindly select one between 0 and 19: "))
    
    choose_parking_slot(space)
 


    for slot in parking_space:
    
        print(slot)

    remove_parking_space(space)

    choice = input("Would you like to select another slot?: ")
    if(choose_to_stop(choice)== True):
        break
   
    




