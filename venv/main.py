from UI.UI import UI
from Service.EventService import EventService
from Service.ParticipantService import ParticipantService
from Repository.Repository import Repository

event_repository = Repository()
participant_repository = Repository()
event_service = EventService(event_repository)
participant_service = ParticipantService(participant_repository, event_service)
ui = UI(event_service, participant_service)
ui.run()
