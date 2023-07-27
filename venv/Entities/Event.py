class Event:
    def __init__(self, id, title, city, number_of_participants, maximum_places, start_date, final_date, website):
        """
        Constructor for the Event class
        :param id: (str) the event ID
        :param title: (str) the title of the event
        :param city: (str) the city of the event
        :param number_of_participants: (int) the number of participants
        :param maximum_places: (int) the maximum places available
        :param start_date: (datetime) the starting time of the event
        :param final_date: (datetime) the ending time of the event
        :param website: (qr) the qr code of the website of the event (the id converted to QR)
        """
        self.__id = id
        self.__title = title
        self.__city = city
        self.__number_of_participants = number_of_participants
        self.__maximum_places = maximum_places
        self.__start_date = start_date
        self.__final_date = final_date
        self.__website = website
        self.__participant_list = []

    def get_id(self):
        """
        Getter for the event ID
        :return:
        """
        return self.__id

    def set_id(self, new_id):
        """
        Setter for the event ID
        :param new_id: (str) the new ID
        :return:
        """
        self.__id = new_id

    def get_city(self):
        """
        Getter for the city of the event
        :return:
        """
        return self.__city

    def set_city(self, new_city):
        """
        Setter for the city of the event
        :param new_city: (str) the new city of the event
        :return:
        """
        self.__city = new_city

    def get_title(self):
        """
        Getter for the title of the event
        :return:
        """
        return self.__title

    def set_title(self, new_title):
        """
        Setter for the title of the event
        :param new_title: (str) the new title
        :return:
        """
        self.__title = new_title

    def get_number_of_participants(self):
        """
        Getter for the number of participants
        :return:
        """
        return self.__number_of_participants

    def set_number_of_participants(self, new_number_of_participants):
        """
        Setter for the number of participants
        :param new_number_of_participants: (int) new number of participants
        :return:
        """
        self.__number_of_participants = new_number_of_participants

    def get_maximum_places(self):
        """
        Getter for the maximum spots available
        :return:
        """
        return self.__maximum_places

    def set_maximum_places(self, new_maximum_places):
        """
        Setter for the maximum spots available
        :param new_maximum_places: (int) new number of maximum spots
        :return:
        """
        self.__maximum_places = new_maximum_places

    def get_start_date(self):
        """
        Getter for the event start date
        :return:
        """
        return self.__start_date

    def set_start_date(self, new_start_date):
        """
        Setter for the event start date
        :param new_start_date: (datetime) the start date
        :return:
        """
        self.__start_date = new_start_date

    def get_final_date(self):
        """
        Getter for the event ending date
        :return:
        """
        return self.__final_date

    def set_final_date(self, new_final_date):
        """
        Setter for the event final date
        :param new_final_date: (datetime) the final date
        :return:
        """
        self.__final_date = new_final_date

    def get_website(self):
        """
        Getter for the QR of the event
        :return:
        """
        return self.__website

    def get_participant_list(self):
        """
        Getter for the participants of the event
        :return:
        """
        return self.__participant_list

    def __repr__(self):
        """
        Representation of the Event Object
        :return:
        """
        i = self.get_id()
        c = self.get_city()
        t = self.get_title()
        np = self.get_number_of_participants()
        ms = self.get_maximum_places()
        s = self.get_start_date()
        f = self.get_final_date()
        return f"Event of id: {i}, title: {t}, city: {c}, number of participants: {np}, maximum spots available: {ms}, start date: {s}, end date: {f}"

    def __str__(self):
        """
        Readable representation of the Event object
        :return:
        """
        return str(repr(self))
