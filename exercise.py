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
Jogging = Exercise(4, 'Jogging', 'TODO')
Hiking = Exercise(5, 'Hiking', 'Balabala')
Table_Tennis = Exercise(6, 'Table Tennis', 'Table tennis (also known as ping-pong or whiff-whaff) is a racket sport derived from tennis but distinguished by its playing surface being atop a stationary table, rather than the court on which players stand. Either individually or in teams of two, players take alternating turns returning a light, hollow ball over the tables net onto the opposing half of the court using small rackets until they fail to do so, which results in a point for the opponent. Play is fast, requiring quick reaction and constant attention, and is characterized by an emphasis on spin relative to other ball sports, which can heavily affect the ball trajectory.')
Table_Tennis.set_cite("Wikipedia contributors. (2024a, June 6). Table tennis. Wikipedia. https://en.wikipedia.org/wiki/Table_tennis")
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
