from typing import List


class Exercise():
    def __init__(self, id: int, name: str, description: str):
        self.id = id
        self.name = name
        self.description = description
        self.cite = ""
        self.bg = None

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

    def set_bg(self, bg):
        self.bg = bg

    def __repr__(self):
        return f' {self.exercise}'

    def get_dis(self):
        return self.description

    def set_cite(self, dis):
        self.cite = dis
    def have_bg(self):
        return (self.bg is not None)
Bicep_Curl = Exercise(1, 'Bicep Curl', 'Curling exercise working the biceps brachii muscle where the elbow is stationary and the arm slowly bends from an overstretched position to a folded one.')
Bicep_Curl.set_bg('url(/static/images/bc.jpg)')
Jacknife_Situps = Exercise(2, 'Jacknife Situps', 'Exercise where a person laying on a flat surface folds their body such that the tip of their toes touches the tip of the fingers.')
Jacknife_Situps.set_bg('url(/static/images/js.jpg)')
Swimming = Exercise(3, 'Swimming', 'A popular recreational exercise that involves moving in a body of water. Useful for cardio and training of the whole body, with an emphasis on upper body.')
Swimming.set_bg('url(/static/images/swim.jpg')
Jogging = Exercise(4, 'Jogging', 'A form of running at a specific pace, typically done for cardio exercise. This will primarily focus on cardiovascular and leg endurance.')
Hiking = Exercise(5, 'Hiking', 'An outdoor activity that involves walking up trails or natural paths, typically on an incline. This is a leisure activity done for cardio exercise and focuses primarily on legs.')
Table_Tennis = Exercise(6, 'Table Tennis', 'Table tennis, often known as ping pong, is a sport played indoors on a special table.')
More = Exercise(7, 'More', 'Placeholder section to add more exercise')
Jogging = Exercise(4, 'Jogging', 'Jogging is a form of trotting or running at a slow or leisurely pace. The main intention is to increase physical fitness with less stress on the body than from faster running but more than walking, or to maintain a steady speed for longer periods of time. Performed over long distances, it is a form of aerobic endurance training.')
Jogging.set_cite("Wikipedia contributors. (2024a, March 30). Jogging. Wikipedia. https://en.wikipedia.org/wiki/Jogging")
Jogging.set_bg('url(/static/images/jogging.jpeg')
Hiking = Exercise(5, 'Hiking', 'Hiking is a long, vigorous walk, usually on trails or footpaths in the countryside. Walking for pleasure developed in Europe during the eighteenth century. Religious pilgrimages have existed much longer but they involve walking long distances for a spiritual purpose associated with specific religions.')
Hiking.set_cite("Wikipedia contributors. (2024d, July 2). Hiking. Wikipedia. https://en.wikipedia.org/wiki/Hiking")
Hiking.set_bg('url(/static/images/hiking.jpeg')
Table_Tennis = Exercise(6, 'Table Tennis', 'Table tennis (also known as ping-pong or whiff-whaff) is a racket sport derived from tennis but distinguished by its playing surface being atop a stationary table, rather than the court on which players stand. Either individually or in teams of two, players take alternating turns returning a light, hollow ball over the tables net onto the opposing half of the court using small rackets until they fail to do so, which results in a point for the opponent. Play is fast, requiring quick reaction and constant attention, and is characterized by an emphasis on spin relative to other ball sports, which can heavily affect the ball trajectory.')
Table_Tennis.set_cite("Wikipedia contributors. (2024a, June 6). Table tennis. Wikipedia. https://en.wikipedia.org/wiki/Table_tennis")
Table_Tennis.set_bg('url(/static/images/Pingpang.jpeg')
Basketball = Exercise(7, "Basketball", "鸡你太美！")
Basketball.set_bg('url(/static/images/img.png)')
More = Exercise(8, 'More', 'Balabala')

exercises: List[Exercise] = [
    Bicep_Curl,
    Jacknife_Situps,
    Swimming,
    Jogging,
    Hiking,
    Table_Tennis,
    Basketball,
    More
]
