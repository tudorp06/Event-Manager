class Participant:
    def __init__(self, name, photo_link, list_of_events):
        self.__name = name
        self.__photo_link = photo_link
        self.__list_of_events = []

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_photo_link(self):
        return self.__photo_link

    def set_photo_link(self, new_link):
        self.__photo_link = new_link

    def get_list_of_events(self):
        return self.__list_of_events

    def __repr__(self):
        return "Participant of name: " + self.get_name() + ", photo link: " + self.get_photo_link() + ", list of events: " + str(self.get_list_of_events())

    def __str__(self):
        return str(repr)
