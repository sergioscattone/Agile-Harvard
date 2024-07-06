from typing import List
from exercise import Exercise


class Workout:
    def __init__(self, id: int, exercises: List[Exercise], description: str):
        self.id = id
        self.exercises = exercises
        self.description = description

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

    def __repr__(self):
        return f' {self.exercises}'
