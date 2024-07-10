from typing import List
from exercise import Exercise


class Workout:
    def __init__(self, id: int, exercises: List[Exercise], name = None, description: str = ""):
        self.id = id
        self.exercises = exercises
        self.description = description
        self.name = name
        if name == None:
            self.name = "My " + str(self.id) + "th Workout"
            if (id % 10 == 1) and (id % 100 != 11):
                self.name = self.name.replace("th", "st")
            if (id % 10 == 2) and (id % 100 != 12):
                self.name = self.name.replace("th", "nd")

    def add(self, exercise):
        self.exercises.append(exercise)
        return self

    def remove(self, exercise):
        self.exercises.remove(exercise)
        return self

    def find(self, exercise_id: int):
        for exercise in self.exercises:
            if exercise.id == exercise_id:
                return exercise

    def get_exercises(self):
        return self.exercises

    def get_self(self, name_needed = False):
        result = self.name + '\n'
        if name_needed:
            for exercise in self.exercises:
                result += str(exercise.get_name()) + "\n\t"
        return result
    def get_exercises(self):
        return self.exercises

"""    def __repr__(self):
        return f' {self.exercises}'"""
