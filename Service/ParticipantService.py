from Repository.Repository import Repository
from Service.EventService import EventService
from Entities.Participant import Participant


class ParticipantService:
    def __init__(self, participant_repository: Repository, event_service: EventService):
        self.__participant_repository = participant_repository
        self.__event_service = event_service
        participant1 = Participant("Tudor Pop", "uwsjb123.com", ["event1", "event2"])

    def find_participant_by_name(self, name):
        ok = 0
        for participant in self.get_all_participants():
            if participant.get_name() == name:
                ok = 1
                return participant
        if ok == 0:
            raise Exception("Could not find participant by name!")

    def get_all_participants(self):
        return self.__participant_repository.get_all()

    def apply_to_event(self, event_id, name, photo_link):
        event = self.__event_service.find_event_by_id(event_id)
        if event:
            if event.get_maximum_places() == 0:
                raise Exception("There are no more availables places for this event!")
            else:
                event.set_number_of_participants(event.get_number_of_participants() - 1)
                event.set_maximum_places(event.get_maximum_places() - 1)
                if self.find_participant_by_name(name):
                    participant = self.find_participant_by_name(name)
                    exists = False
                    for event in participant.get_list_of_events():
                        if event.get_id() == event_id:
                            exists = True
                            raise Exception("You have already registered for this event!")
                    if exists is False:
                        event.get_participant_list().append(participant)
                        participant.get_list_of_events().append(event)
                else:
                    event_list = [event]
                    participant = Participant(name, photo_link, event_list)
                    self.__participant_repository.add(participant)
                    event.get_participant_list().append(participant)
        else:
            raise Exception("Could not find event by ID!")
