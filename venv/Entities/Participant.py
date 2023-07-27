class Participant:
    def __init__(self, name, photo_link, list_of_events):
        """
        Constructor for the Participant class
        :param name: (str) the name of the participant
        :param photo_link: (str) the link to the participant's photo
        :param list_of_events: (list) the list of the events that the participant has applied to
        """
        self.__name = name
        self.__photo_link = photo_link
        if list_of_events is None:
            self.__list_of_events = []
        else:
            self.__list_of_events = list_of_events

    def get_name(self):
        """
        Getter for the participant name
        :return:
        """
        return self.__name

    def set_name(self, new_name):
        """
        Setter for the participant name
        :param new_name: (str) the new name
        :return:
        """
        self.__name = new_name

    def get_photo_link(self):
        """
        Getter for the photo link
        :return:
        """
        return self.__photo_link

    def set_photo_link(self, new_link):
        """
        Setter for the photo link
        :param new_link: (str) the new link
        :return:
        """
        self.__photo_link = new_link

    def get_list_of_events(self):
        """
        Getter for the list of events
        :return:
        """
        return self.__list_of_events

    def __repr__(self):
        """
        The representation of the Participant object
        :return:
        """
        return "Participant of name: " + self.get_name() + ", photo link: " + self.get_photo_link() + ", list of events: " + str(self.get_list_of_events())

    def __str__(self):
        """
        The readable, string representation of the Participant object
        :return:
        """
        return str(repr)
