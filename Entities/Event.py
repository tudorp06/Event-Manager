class Event:
    def __init__(self,id,title,city,number_of_participants,maximum_places,start_date,final_date,website):
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
        return self.__id

    def set_id(self, new_id):
        self.__id = new_id

    def get_city(self):
        return self.__city

    def set_city(self, new_city):
        self.__city = new_city

    def get_title(self):
        return self.__title

    def set_title(self, new_title):
        self.__title = new_title

    def get_number_of_participants(self):
        return self.__number_of_participants

    def set_number_of_participants(self, new_number_of_participants):
        self.__number_of_participants = new_number_of_participants

    def get_maximum_places(self):
        return self.__maximum_places

    def set_maximum_places(self, new_maximum_places):
        self.__maximum_places = new_maximum_places

    def get_start_date(self):
        return self.__start_date

    def set_start_date(self, new_start_date):
        self.__start_date = new_start_date

    def get_final_date(self):
        return self.__final_date

    def set_final_date(self, new_final_date):
        self.__final_date = new_final_date

    def get_website(self):
        return self.__website

    def set_website(self, new_qr):
        self.__website = new_qr

    def get_participant_list(self):
        return self.__participant_list

    def __repr__(self):
        return "Event of id: {i}, title: {t}, city: {c}, number of participants: {np}, maximum spots available: {ms}, " \
               "start date: {s}, end date: {f}".format(i = self.get_id(), c = self.get_city(), t = self.get_title(),
                                                       np = self.get_number_of_participants(),
                                                       ms = self.get_maximum_places(), s = self.get_start_date(),
                                                       f = self.get_final_date())

    def __str__(self):
        return str(repr(self))
