from Service.EventService import EventService
from Service.ParticipantService import ParticipantService
from datetime import datetime
from Entities.Event import Event
import qrcode
import os


class UI:
    def __init__(self, event_service: EventService, participant_service: ParticipantService):
        self.__event_service = event_service
        self.__participant_service = participant_service

    def clear_screen(self):
        os.system("cls")

    def __generate_qr(self, event_id):
        qr_code = qrcode.QRCode()
        qr_code.add_data(event_id)
        qr_code.make()
        qr_image = qr_code.make_image()
        return qr_image

    def __main_menu(self):
        print("Welcome to the TIPD event organiser! For starters, please choose your view mode:")
        print("1) Organiser mode")
        print("2) Participant mode")
        print("0) Exit")

    def __organiser_menu(self):
        print("---Organiser mode---")
        print("1) Add event")
        print("2) Delete event")
        print("3) Modify event")
        print("4) View events by city")
        print("5) View event participants")
        print("6) Sort events by participants")
        print("7) See event QR code")
        print("0) Back to main menu")

    def __participant_menu(self):
        print("---Participant mode---")
        print("1) View event list")
        print("2) Register for an event")
        print("3) View the next 7 day events")
        print("4) View events by month")
        print("0) Back to main menu")

    def run(self):
        while True:
            self.__main_menu()
            try:
                command = int(input("Choose your mode: "))
                if command == 1:
                        self.__organiser_menu()
                        option = int(input("Your option: "))
                        if option == 1:
                            self.clear_screen()
                            self.__add_event()
                        elif option == 2:
                            self.clear_screen()
                            self.__delete_event()
                        elif option == 3:
                            self.clear_screen()
                            self.__update_event()
                        elif option == 4:
                            self.clear_screen()
                            self.__print_events_by_city()
                        elif option == 5:
                            self.clear_screen()
                            self.__view_event_participants()
                        elif option == 6:
                            self.clear_screen()
                            self.__view_events_with_participants()
                        elif option == 7:
                            self.clear_screen()
                            self.show_qr()
                        elif option == 0:
                            self.__main_menu()

                elif command == 2:
                        self.__participant_menu()
                        option = int(input("Your option: "))
                        if option == 1:
                            self.clear_screen()
                            self.__print_event_list()
                        elif option == 2:
                            self.clear_screen()
                            self.__apply_to_event()
                        elif option == 3:
                            self.clear_screen()
                            self.__print_next_7_day_events()
                        elif option == 4:
                            self.clear_screen()
                            self.__view_events_by_month()
                        elif option == 0:
                            self.__main_menu()

                elif command == 0:
                    exit("Thank you for using this app!")
            except Exception as error:
                print("Caught an error: " + str(error))

    def __add_event(self):
        id = input("Enter the event ID: ")
        title = input("Enter the event title: ")
        city = input("Enter the city of the event: ")
        number_of_participants = int(input("Enter the number of participants: "))
        maximum_places = int(input("Enter the maximum spots available: "))
        start_date = input("Enter the start date of the event: ")
        final_date = input("Enter the end date of the event: ")
        start_date = datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S")
        final_date = datetime.strptime(final_date, "%Y-%m-%d %H:%M:%S")
        website = self.__generate_qr(id)
        event = Event(id, title, city, number_of_participants, maximum_places, start_date, final_date, website)
        self.__event_service.add_event(event)
        print("Succesfully added event!")

    def __delete_event(self):
        id = input("Enter the ID of the event that you would like to delete: ")
        self.__event_service.delete_event(id)
        print("Successfully deleted event!")

    def __update_event(self):
        id = input("Enter the ID of the event that you would like to update:")
        new_title = input("Enter the new title: ")
        new_city = input("Enter the new city: ")
        new_number_of_participants = int(input("Enter the new number of participants: "))
        new_maximum_places = int(input("Enter the new number of spots available: "))
        new_start_date = input("Enter the new start date: ")
        new_final_date = input("Enter the new end date: ")
        new_start_date = datetime.strptime(new_start_date, "%Y-%m-%d %H:%M:%S")
        new_final_date = datetime.strptime(new_final_date, "%Y-%m-%d %H:%M:%S")
        self.__event_service.update_event(id, new_title, new_city, new_number_of_participants, new_maximum_places,
                                          new_start_date, new_final_date)
        print("Successfully updated event!")

    def __print_event_list(self):
        event_list = self.__event_service.get_all_events()
        for event in event_list:
            print(str(event))

    def __print_events_by_city(self):
        city = input("Enter the city where you would like to see events: ")
        city_list = self.__event_service.get_events_by_city(city)
        for event in city_list:
            print(str(event))

    def show_qr(self):
        qr = None
        exists = False
        event_id = input("Enter the ID of the event whose QR code you'd like to see:")
        event_list = self.__event_service.get_all_events()
        for event in event_list:
            if event.get_id() == event_id:
                qr = event.get_website()
                exists = True
        if exists is not False:
            qr.show()
        else:
            raise Exception("Could not find event by ID!")

    def __print_next_7_day_events(self):
        next_7_days_list = self.__event_service.get_events_by_start_date()
        for event in next_7_days_list:
            print(str(event))

    def __view_events_by_month(self):
        month = int(input("Enter the month: "))
        event_by_month_list = self.__event_service.get_events_by_month(month)
        for event in event_by_month_list:
            print(str(event))

    def __apply_to_event(self):
        event_id = input("Please enter the ID of the event you'd like to register to: ")
        name = input("Please enter your name: ")
        photo_link = input("Please enter your photo link: ")
        apply = self.__participant_service.apply_to_event(event_id, name, photo_link)
        if apply:
	        print("Congrats, " + name + ", you succesfully registered for the event!")

    def __view_event_participants(self):
        event_id = input("Enter the ID of the event: ")
        participant_list = self.__event_service.get_event_participants(event_id)
        if len(participant_list) == 0:
            raise Exception("This event has no participants!")
        else:
            print("The participants of this event are: ")
            print(participant_list)

    def __view_events_with_participants(self):
        events_with_participants = self.__event_service.get_events_with_participants()
        for event in events_with_participants:
            print(event)
