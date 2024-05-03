import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 5478  # The port used by the server


while True:
    print("\nWelcome to the timezone converter! This program will allow you to enter a time and a US state.\nThe program will tell you the equivalent time in whatever state you choose! It will take roughly 30 seconds to a minute to use.\nPlease enter 'Help' for more information.\nOr to start, please enter the two-letter state code for a US state (or DC for Washington DC):")
    state1 = str(input())
    if state1 == "Help":
        print("You have requested additional information about the program!\nThis program takes a time and a state in the United States and returns the equivalent time in another state of your choosing.\nTo use this program, all you need to do is enter a time, a starting state name, and ending state name.\nYou will also be asked to verify the ending state name to ensure you did not make a mistake.\nYou also have the option to return to the Home page at any time by pressing 0.\nPlease note that some states are between two timezones, and the program will return the time that the majority of the state falls into.\nPlease enter 0 or type 'return' to return to the Home page now.")
        return_input = str(input())
        if return_input == str(0) or return_input == 'return':
            continue
        else:
            print("Invalid entry. Press 0 or enter 'return' to return to the Home screen")
            return_input = int(input())
            
    states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
    #send first state to microservice 1        
    else:  
        if state1 in states:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                s.sendall(state1.encode())
                timezone1 = s.recv(1024).decode()

    #enter a second state and send to microservice 1
    # verify = 'Y'
    # while verify == 'Y':
    #     print("Please enter the two-letter state code for the US state you'd like to know the time in (or enter 'DC' for Washington DC):")
    #     state2 = str(input())
    #     # # verify
    #     # print("Are you sure? Enter Y for yes, or N to go back and change your answers")
    #     # verify = str(input())
    #     # if verify == 'N':
    #     #     continue
        # if state1 in states:
        #     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            #     s.connect((HOST, PORT))
            #     s.sendall(state2.encode())
            #     timezone2 = s.recv(1024).decode()


    print("To return to the Home page and use the program again, press 0.")
    restart = int(input())
    if restart == 0:
        continue
    else:
        print("Invalid entry. Please try again. Enter 0 to return to the Home page.")
        restart = int(input())

    
    
    
    myMessage = input("Enter '1' or '2' to get a response from the microservice: ")
    if myMessage == '1' or myMessage == '2':

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(myMessage.encode())
            data = s.recv(1024).decode()
            print(data)


from datetime import datetime
def time_parser(time_string):
    error_msg = "Invalid entry"
    format_data = "%H:%M"
    time_data = datetime.strptime(time_string, format_data)
    hour = str(time_data.hour)
    minute = str(time_data.minute).zfill(2)
    #fix error handling later
    # if 0 < time_data.hour < 24 or 0 < time_data.minute < 60:
    #     return error_msg
    return hour + ":" + minute
