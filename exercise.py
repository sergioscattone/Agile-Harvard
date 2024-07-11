from typing import List


class Exercise():
    def __init__(self, id: int, name: str, description: str):
        self.id = id
        self.name = name
        self.description = description

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


Bicep_Curl = Exercise(1, 'Bicep Curl', 'Curling exercise working the biceps brachii muscle where the elbow is stationary and the arm slowly bends from an overstretched position to a folded one.')
Jacknife_Situps = Exercise(2, 'Jacknife Situps', 'Exercise where a person laying on a flat surface folds their body such that the tip of their toes touches the tip of the fingers.')
Swimming = Exercise(3, 'Swimming', 'A popular recreational exercise that involves moving in a body of water. Useful for cardio and training of the whole body, with an emphasis on upper body.')
Jogging = Exercise(4, 'Jogging', 'TODO')
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
