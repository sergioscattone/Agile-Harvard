from typing import List


class Exercise():
    def __init__(self, id: int, name: str, description: str):
        self.id = id
        self.name = name
        self.description = description
        self.cite = ""

    def update(self, name: str, description: str):
        self.name = name
        self.description = description
        return self

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def show(self):
        print(self.name)
        print(self.description)

    def __repr__(self):
        return f' {self.exercise}'

    def get_dis(self):
        return self.description

    def set_cite(self, dis):
        self.cite = dis

Bicep_Curl = Exercise(1, 'Bicep Curl', 'Balabala')
Jacknife_Situps = Exercise(2, 'Jacknife Situps', 'Balabala')
Swimming = Exercise(3, 'Swimming', 'Balabala')
Jogging = Exercise(4, 'Jogging', 'Balabala')
Hiking = Exercise(5, 'Hiking', 'Balabala')
Table_Tennis = Exercise(6, 'Table Tennis', 'Balabala')
More = Exercise(7, 'More', 'Balabala')
exercises: List[Exercise] = [
    Bicep_Curl,
    Jacknife_Situps,
    Swimming,
    Jogging,
    Hiking,
    Table_Tennis,
    More
]
