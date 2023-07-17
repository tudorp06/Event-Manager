import json
from Entities.Event import Event


class FileRepository():
    def __init__(self, file_path):
        self.__file_path = file_path

    def add_event(self, event):
        events = self.get_all_events()
        events.append(event)
        self._save_events(events)

    def delete_event(self, event_id):
        events = self.get_all_events()
        events = [e for e in events if e.get_id() != event_id]
        self._save_events(events)

    def get_all_events(self):
        try:
            with open(self.__file_path, 'r') as file:
                events_data = json.load(file)
                events = [Event(**data) for data in events_data]
                return events
        except FileNotFoundError:
            return []

    def _save_events(self, events):
        events_data = [event.__dict__ for event in events]
        with open(self.__file_path, 'w') as file:
            json.dump(events_data, file)
