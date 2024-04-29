from datetime import datetime

def time_parser(time_string):
    error_msg = "Invalid entry"
    format_data = "%H:%M"
    time_data = datetime.strptime(time_string, format_data)
    hour = str(time_data.hour)
    minute = str(time_data.minute).zfill(2)
    #fix error handling later
    if 0 < time_data.hour < 24 or 0 < time_data.minute < 60:
        return error_msg
    return hour + ":" + minute


while True:
    print("Welcome to the timezone converter! This program will allow you to enter a time and a US state.\nThe program will tell you the equivalent time in whatever state you choose!\nPlease enter 'Help' for more information.\nOr to start, please enter a time using 24-hour format (HH:MM):")
    input1 = str(input())
    print(time_parser(input1))
    if input1 == "Help":
        print("You have requested additional information about the program!\nThis program takes a time and a state in the United States and returns the equivalent time in another state of your choosing.\nTo use this program, all you need to do is enter a time, a starting state name, and ending state name.\nYou will also be asked to verify the ending state name to ensure you did not make a mistake.\nYou also have the option to return to the Home page at any time by pressing 0.\nPlease note that some states are between two timezones, and the program will return the time that the majority of the state falls into.\nPlease enter 0 to return to the Home page now.")
        return_input = int(input())
        if return_input == 0:
            continue
        else:
            print("Invalid entry. Press 0 to return to the Home screen")
            return_input = int(input())
    else:
        time_zone = 'none'
        while time_zone == 'none':
            print("Please enter the full name of a US state (or enter 'DC' for Washington DC):")
            state_input = str(input())
            if state_input == "Washington" or "Oregon" or "California" or "Nevada":
                time_zone = 'pst'
            elif state_input == "Montana" or "Idaho" or "Wyoming" or "Utah" or "Colorado" or "Arizona" or "New Mexico":
                time_zone = 'mst'
            elif state_input == "North Dakota" or "South Dakota" or "Nebraska" or "Kansas" or "Oklahoma" or "Texas" or "Minnesota" or "Iowa" or "Wisconsin" or "Illinois" or "Missouri" or "Arkansas" or "Tennessee" or "Louisiana" or "Mississippi" or "Alabama":
                time_zone = 'cst'
            elif state_input == "Michigan" or "Indiana" or "Ohio" or "Kentucky" or "Georgia" or "Florida" or "South Carolina" or "North Carolina" or "Virginia" or "West Virginia" or "DC" or "Maryland" or "Pennsylvania" or "Delaware" or "New Jersey" or "New York" or "Rhode Island" or "Connecticut" or "Massachusetts" or "New Hampshire" or "Vermont" or "Maine":
                time_zone = 'est'
            elif state_input == "Hawaii":
                time_zone = 'hawaii'
            elif state_input == "Alaska":
                time_zone = 'alaska'
            else:
                print("Invalid state. Please try again")

        #enter a second state
        verify = 'N'
        while verify == 'N':
            print("Please enter the state you'd like to know the time in (or enter 'DC' for Washington DC):")
            dest_state_input = str(input())
            if dest_state_input == "Washington" or "Oregon" or "California" or "Nevada":
                dest_time_zone = 'pst'
            elif dest_state_input == "Montana" or "Idaho" or "Wyoming" or "Utah" or "Colorado" or "Arizona" or "New Mexico":
                dest_time_zone = 'mst'
            elif dest_state_input == "North Dakota" or "South Dakota" or "Nebraska" or "Kansas" or "Oklahoma" or "Texas" or "Minnesota" or "Iowa" or "Wisconsin" or "Illinois" or "Missouri" or "Arkansas" or "Tennessee" or "Louisiana" or "Mississippi" or "Alabama":
                dest_time_zone = 'cst'
            elif dest_state_input == "Michigan" or "Indiana" or "Ohio" or "Kentucky" or "Georgia" or "Florida" or "South Carolina" or "North Carolina" or "Virginia" or "West Virginia" or "DC" or "Maryland" or "Pennsylvania" or "Delaware" or "New Jersey" or "New York" or "Rhode Island" or "Connecticut" or "Massachusetts" or "New Hampshire" or "Vermont" or "Maine":
                dest_time_zone = 'est'
            elif dest_state_input == "Hawaii":
                dest_time_zone = 'hawaii'
            elif dest_state_input == "Alaska":
                dest_time_zone = 'alaska'
            else:
                print("Invalid state. Please try again")
        
            #verify
            print("Are you sure? Enter Y for yes, or N for no")
            verify = str(input())
            if verify == 'Y':
                break
            else:
                print("Send to microservices! Feature coming soon!")
                end_time = 'tbd!'

    start_time = time_parser(input1)
    print(f"When it is {input1} in {state_input} it is {end_time} in {dest_state_input}.\n")

   