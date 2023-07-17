class Repository:
    def __init__(self):
        self.__entity_list = []

    def find_entity(self, entity):
        for i in range(len(self.__entity_list)):
            if self.__entity_list[i] == entity:
                return i
        return None

    def add(self, entity):
        pos = self.find_entity(entity)
        if pos is not None:
            raise Exception("Entity already exists!")
        self.__entity_list.append(entity)

    def delete(self, entity):
        pos = self.find_entity(entity)
        if pos is None:
            raise Exception("Entity does not exist!")
        self.__entity_list.remove(entity)

    def get_all(self):
        if len(self.__entity_list) == 0:
            raise Exception("You have no entities!")
        return self.__entity_list
