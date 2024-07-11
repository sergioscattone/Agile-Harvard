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

Bicep_Curl = Exercise(1, 'Bicep Curl', 'Curling exercise working the biceps brachii muscle where the elbow is stationary and the arm slowly bends from an overstretched position to a folded one.')
Jacknife_Situps = Exercise(2, 'Jacknife Situps', 'Exercise where a person laying on a flat surface folds their body such that the tip of their toes touches the tip of the fingers.')
Swimming = Exercise(3, 'Swimming', 'A popular recreational exercise that involves moving in a body of water. Useful for cardio and training of the whole body, with an emphasis on upper body.')
Jogging = Exercise(4, 'Jogging', 'A form of running at a specific pace, typically done for cardio exercise. This will primarily focus on cardiovascular and leg endurance.')
Hiking = Exercise(5, 'Hiking', 'An outdoor activity that involves walking up trails or natural paths, typically on an incline. This is a leisure activity done for cardio exercise and focuses primarily on legs.')
Table_Tennis = Exercise(6, 'Table Tennis', 'Table tennis, often known as ping pong, is a sport played indoors on a special table.')
More = Exercise(7, 'More', 'Placeholder section to add more exercise')
exercises: List[Exercise] = [
    Bicep_Curl,
    Jacknife_Situps,
    Swimming,
    Jogging,
    Hiking,
    Table_Tennis,
    More
]
