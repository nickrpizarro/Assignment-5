# Name: Nicholas Pizarro
# OSU Email: pizarron@oregonstate.edu
# Course: CS361 - SOFTWARE ENGINEERING 1
# Assignment: 5 Milestone #1
# Due Date: 04/24/22

zip_code_message = "\nWelcome to the NYC Weather App!\nPlease enter the zip code for the forecast information " \
                   "you would like to view"

welcome_message_1 = "Welcome to the NYC Weather App!"

welcome_message_2 = "\nYou can use this tool to get forecast information about New York Ctiy.\n"\
                    "To navigate the menu, use the UP and DOWN ARROW keys, and press ENTER key to make selection.\n"

menu_hour_message = " 1. Show weather forecast for current hour:"
menu_day_message = "2. Show weather forecast for current day:"
menu_week_message = "3. Show weather forecast for week:"
menu_quit_message = "Quit (select this option to quit App)"

hour_forcast = "\n\nCurrent Weather in NYC:\n\nTemperature: 55°F (13°C)\nConditions:  Cloudy\nWind:        NW 8 mph" \
               "\nHumidity:    75%\nSunrise:     6:25 AM\nSunset:      7:41 PM"

day_forcast_1 = "\n\nHourly Weather in NYC:\n\n1 PM:  Partly Cloudy, 59°F (15°C), Wind W 9 mph, Humidity 69%" \
                "\n2 PM:  Partly Cloudy, 60°F (16°C), Wind W 10 mph, Humidity 68%\n3 PM:  Partly Cloudy, 61°F " \
                "(16°C), Wind W 11 mph, Humidity 67%\n4 PM:  Mostly Cloudy, 62°F (17°C), Wind W 12 mph, Humidity 66%" \
                "\n5 PM:  Mostly Cloudy, 62°F (17°C), Wind W 12 mph, Humidity 66%\n6 PM:  Mostly Cloudy, " \
                "61°F (16°C), Wind W 11 mph, Humidity 67%"

day_forcast_2 = "\nWeather in NYC until 11PM:\n\n7 PM:  Mostly Cloudy, 60°F (15°C), Wind W 10 mph, Humidity 68%" \
                "\n8 PM:  Mostly Cloudy, 59°F (15°C), Wind W 9 mph, Humidity 69%\n9 PM:  Partly Cloudy, 57°F (14°C), " \
                "Wind W 8 mph, Humidity 72%\n10 PM: Partly Cloudy, 56°F (13°C), Wind W 7 mph, Humidity 73%" \
                "\n11 PM: Clear, 54°F (12°C), Wind W 6 mph, Humidity 75%"

week_forcast = "\n\nWeather in NYC for the Week:\n\nMonday:    Partly Cloudy, High 65°F (18°C), Low 55°F (13°C), " \
               "Wind W 8 mph, Humidity 68%\nTuesday:   Rain, High 58°F (14°C), Low 47°F (8°C), Wind NE 12 mph, " \
               "Humidity 85%\nWednesday: Partly Cloudy, High 61°F (16°C), Low 50°F (10°C), Wind NW 9 mph, " \
               "Humidity 72%\nThursday:  Mostly Sunny, High 65°F (18°C), Low 53°F (12°C), Wind W 10 mph, " \
               "Humidity 65%\nFriday:    Partly Cloudy, High 67°F (19°C), Low 54°F (12°C), " \
               "Wind W 8 mph, Humidity 61%\nSaturday:  Mostly Cloudy, High 63°F (17°C), Low 53°F (12°C), " \
               "Wind W 9 mph, Humidity 72%\nSunday:    Rain, High 59°F (15°C), Low 49°F (9°C), " \
               "Wind E 10 mph, Humidity 80%"

back_to_menu = "\n\nPress ENTER to go back to selection"


user_zip_code = input(zip_code_message)

while True:

    print("\n")
    print(welcome_message_1)
    print("Current location selected Manhattan (Midtown)", user_zip_code)
    print(welcome_message_2)

    print(menu_hour_message, "\n", menu_day_message, "\n", menu_week_message, "\n\n\n", menu_quit_message)

    user_selection = input()

    if user_selection == "1":
        print(hour_forcast)
        input(back_to_menu)

    elif user_selection == "2":
        print(day_forcast_1)
        day_user_input = input("\nShow more...ENTER Y/N")
        if day_user_input == "Y" or day_user_input == "y":
            print(day_forcast_2)
        input(back_to_menu)

    elif user_selection == "3":
        print(week_forcast)
        input(back_to_menu)

    elif user_selection == "Q" or user_selection == "q":
        print("Quitting...")
        break

    else:
        print("Invalid selection, Please try again")
