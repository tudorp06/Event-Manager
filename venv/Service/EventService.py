from Repository.Repository import Repository
from Entities.Event import Event
from datetime import datetime


class EventService:
    def __init__(self, event_repository: Repository):
        """
        The EventService class, responsible for the service of the events, that takes an event_repository Repository
        object as its attribute."
        :param event_repository: Repository object that stores the event list and operations
        """
        self.__event_repository = event_repository
        event1 = Event("ev1", "Poveste la film", "Cluj-Napoca", 60, 100, datetime(2023, 3, 10, 16),
                       datetime(2023, 3, 10, 18), None)
        event2 = Event("ev2", "Tete-a-Tete", "Cluj-Napoca", 40, 60, datetime(2023, 5, 26, 13),
                       datetime(2023, 5, 28, 19), None)
        event3 = Event("ev3", "Guns-N-Roses Concert", "Bucharest", 100000, 100005, datetime(2023, 7, 16, 16),
                       datetime(2023, 7, 16, 17), None)
        self.add_event(event1)
        self.add_event(event2)
        self.add_event(event3)

    def add_event(self, event):
        """
        Function that adds a parametered event to the repository list of events
        :param event: Event object (Event)
        :return: None
        """
        if event.get_maximum_places() < event.get_number_of_participants():
            raise Exception("This event has exceeded its number of places!")
        self.__event_repository.add(event)

    def find_event_by_id(self, event_id):
        """
        Function that searches an event by ID in the event list.
        :param event_id: The ID of the event (str)
        :return:
        """
        for event in self.get_all_events():
            if event.get_id() == event_id:
                return event
        raise Exception("Could not find event by ID!")

    def delete_event(self, event_id):
        """
        Finds an event by ID and deletes it from the list.
        :param event_id: The ID of the event (str)
        :return:
        """
        if self.find_event_by_id(event_id):
            event = self.find_event_by_id(event_id)
            self.__event_repository.delete(event)
            return True
        else:
            raise Exception("Could not find event by ID!")

    def get_all_events(self):
        """
        Returns the list of events from the repository
        :return: The list of events (list)
        """
        return self.__event_repository.get_all()

    def update_event(self, event_id, new_title, new_city, new_number_of_participants, new_maximum_places,
                     new_start_date, new_final_date):
        """
        Finds an event by its ID and then updates its data.
        :param event_id: The ID of the event (str)
        :param new_title: The new title of the event (str)
        :param new_city: The new city of the event (str)
        :param new_number_of_participants: The new number of participants at the event (int)
        :param new_maximum_places: The new number of available spots (int)
        :param new_start_date: The new start date (date)
        :param new_final_date: The new final date (date)
        :return:
        """
        if self.find_event_by_id(event_id):
            event = self.find_event_by_id(event_id)
            event.set_title(new_title)
            event.set_city(new_city)
            event.set_number_of_participants(new_number_of_participants)
            event.set_maximum_places(new_maximum_places)
            event.set_start_date(new_start_date)
            event.set_final_date(new_final_date)
            if event.get_maximum_places() < event.get_number_of_participants():
                raise Exception("This event has exceeded its number of places!")
        else:
            raise Exception("Could not find event by ID!")

    def get_events_by_city(self, city):
        """
        Returns the list of events that take place in a given city
        :param city: The given city (str)
        :return: city_list (list)
        """
        event_list = self.get_all_events()
        city_list = []
        ok = False
        for event in event_list:
            if event.get_city() == city:
                city_list.append(event)
                ok = True
        if ok is False:
            raise Exception("There are no events in this city!")
        return city_list

    def get_events_by_start_date(self):
        """
        Returns the list of events that take place in the next 7 days, sorted by the maximum number of spots available.
        :return: sorted_list (list)
        """
        event_list = self.get_all_events()
        next_days_list = []
        for event in event_list:
            timespan = int(event.get_start_date().timestamp()) - int(datetime.now().timestamp())
            if 604800 >= timespan >= 0:
                next_days_list.append(event)
        sorted_list = sorted(next_days_list, key=lambda x: x.get_maximum_places())
        if len(sorted_list) == 0:
            raise Exception("There are no events in the next 7 days!")
        return sorted_list

    def get_events_by_month(self, month):
        """
        Returns the list of events that take place in a given month, sorted decreasingly by their duration.
        :param month: the given month (int)
        :return:
        """
        event_list = self.get_all_events()
        start_month_list = []
        ok = False
        for event in event_list:
            if event.get_start_date().month == month:
                start_month_list.append(event)
                ok = True
        sorted_list = sorted(start_month_list, key=lambda x: (x.get_final_date().day - x.get_start_date().day))
        if ok is False:
            raise Exception("There are no events in that month!")
        return sorted_list

    def get_event_participants(self, event_id):
        if self.find_event_by_id(event_id):
            event = self.find_event_by_id(event_id)
            return event.get_participant_list()
        else:
            raise Exception("Could not find event by ID!")

    def has_participants(self, event):
        if len(event.get_participant_list()) > 0:
            return True
        return False

    def get_events_with_participants(self):
        event_list = self.get_all_events()
        events_with_participants = []
        exists = False
        for event in event_list:
            if self.has_participants(event):
                events_with_participants.append(event)
                exists = True
        if exists is False:
            raise Exception("There are no events with participants!")
        sorted_list = sorted(events_with_participants, key= lambda x:x.get_number_of_participants(), reverse = True)
        return sorted_list

