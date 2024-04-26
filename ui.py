

while True:
    print("Welcome to your online patient scheduling portal! This portal will allow you to manage your doctor's appointments online.\nBy pressing 1, you may view existing appointment.\nBy pressing 2, you can schedule a new appointment.\nAnd by pressing 3, you can delete a scheduled appointment.\nFor more information about these options, press 4.\n")
    input1 = int(input())
    if input1 == 1:  #view
        print("View your appointments:\n")
        #from microservice 1: if text file containing scheduled appts is empty, print("No appointments scheduled"). Else, display table
        print("Please press 0 to return to the Home screen")
        input2 = int(input())
        if input2 == 0:
            #return to Home screen
        else:
            print("ERROR: please press 0 to return to the Home screen")




    elif input1 == 2:  #schedule
        print("Schedule an appointment:\nPlease view the list of available appointment times below, and type the corresponding number to schedule:")
        #microservice 1: generate random list of 3 day/time tuples (1: Wednesday, 1:00pm). write to a text file?
        print("Please press 0 to return to the Home screen")
        input2 = int(input())
        if input2 == 1:
            #return to Home screen
        else:
            print("ERROR: please press 0 to return to the Home screen")



    elif input1 == 3:  #delete
        print("Delete an appointment:\nPlease view the list of scheduled appointments, and press the number corresponding to the appointment you want to delete:")
        #display table again
        print("Please press 0 to return to the Home screen")
        input2 = int(input())
        if input2 == 0:
            #return to Home screen
        elif 


    elif input1 == 4:  #more information
        print("You have selected to view additional information!\nIf you select to view your appointments, you will see a list of appointments on the schedule. If there are none, you will see a note 'No appointments scheduled'.\nIf you'd like to schedule a new appointment online, you will be given open appointment times to choose from. If you select one, you will be added to your provider's schedule. You will also be able to view this appointment in your portal. Please note, you will only be able to schedule a maximum of 3 appointments at a time.\nIf you need to delete an appointment, you have that option as well! Cancelling online will remove you from your provider's schedule and remove the appointment from your scheduled appointments list.")
        print("Please press 0 to return to the Home screen")
        input2 = int(input())
        if input4 == 0:
            #route back to home page
        else: 
            print("ERROR: please press 0 to return to the Home screen")



#microservice 1:


#microservice 2:


#microservice 3:


#microservice 4:


#microservice 5:


