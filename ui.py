

while True:
    print("Welcome to your online patient scheduling portal! This portal will allow you to manage your doctor's appointments online.\nPress 1 to view existing appointment.\nPress 2 to schedule a new appointment.\nPress 3 to delete a scheduled appointment.\nPress 4 for additional information about these options.\n")
    input1 = int(input())
    if input1 == 1:  #view
        print("View your appointments:\n")
        #from microservice 1: if text file containing scheduled appts is empty, print("No appointments scheduled"). Else, display table
        print("Please press 0 to return to the Home screen")
        input2 = int(input())
        if input2 == 0:
            print("feature coming soon")
            #return to Home screen
        else:
            print("ERROR: please press 0 to return to the Home screen")


    elif input1 == 2:  #schedule
        print("Schedule an appointment:\nPlease view the list of available appointment times below, and type the corresponding number to schedule:")
        #microservice 1: generate random list of 3 day/time tuples (1: Wednesday, 1:00pm). write to a text file?
        print("Please press 0 at any time if you would like to cancel and return to the Home screen")
        input3 = int(input())
        if input3 == 0:
            print("feature coming soon")
            #return to Home screen
        elif input3 == 1:
            print("feature coming soon")
            #delete entry 1
        elif input3 == 2:
            print("feature coming soon")
            #delete entry 2
        elif input3 == 3:
            print("feature coming soon")
            #delete entry 3
        else:
            print("Invalid entry")



    elif input1 == 3:  #delete
        print("Delete an appointment:\nPlease view the list of scheduled appointments, and press the number corresponding to the appointment you want to delete:")
        #display table again
        print("Please press 0 at any time if you would like to cancel and return to the Home screen")
        input4 = int(input())
        if input4 == 0:
            print("feature coming soon")
            #return to Home screen
        elif input4 == 1:
            print("Are you sure you want to delete this appointment? If yes, press 1. If no, press 0.")
            confirm = int(input())
            if confirm == 1:
                print("feature coming soon")
                #delete entry 1- call microservice
            else:
                print("feature coming soon")
                #return to Home screen
        elif input4 == 2:
            print("Are you sure you want to delete this appointment? If yes, press 1. If no, press 0.")
            confirm = int(input())
            if confirm == 1:
                print("feature coming soon")
                #delete entry 2- call microservice
            else:
                print("feature coming soon")
                #return to Home screen
        elif input4 == 3:
            print("Are you sure you want to delete this appointment? If yes, press 1. If no, press 0.")
            confirm = int(input())
            if confirm == 1:
                print("feature coming soon")
                #delete entry 3- call microservice
            else:
                print("Returning to Home screen")
                #return to Home screen
        else:
            print("Invalid entry")


    elif input1 == 4:  #more information
        print("You have selected to view additional information!\nIf you select to view your appointments, you will see a list of appointments on the schedule. If there are none, you will see a note 'No appointments scheduled")
        print("If you'd like to schedule a new appointment online, you will be given open appointment times to choose from. If you choose one, you will be added to your provider's schedule.")
        print("You will also be able to view this appointment in your portal. Please note, you will only be able to schedule a maximum of 3 appointments at a time.")
        print("If you need to delete an appointment, you have that option as well! Cancelling online will remove you from your provider's schedule and remove the appointment from your scheduled appointments list.")
        print("Please press 0 to return to the Home screen")
        input5 = int(input())
        if input5 == 0:
            print("feature coming soon")
            #route back to home page
        else: 
            print("ERROR: please press 0 to return to the Home screen")
            



#microservice 1: called by 'schedule'
    #generate 3 day/time tuples, and add to dictionary with ID numbers
    #format data as a table (geeksforgeeks)
    #add to text file "random_appointments.txt"
    #send to UI to display
    #receives text input back corresponding to which entry the user chose
    #sends that entry to new text file "scheduled_appts.txt"

#microservice 2: called by 'view'
    #pulls the table from text file "scheduled_appts.txt"
    #sends table to UI to display

#microservice 3: called by 'delete'
    #takes user input and removes corresponding line from "scheduled_appts.txt"
    

#microservice 4:


#microservice 5:


