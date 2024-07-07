from workout import Workout
from typing import List
class User():
    numbers = 0
    def __init__(self, email: str, password: str):
        self.id = User.numbers + 1
        self.email = email
        self.password = password
        self.active = False
        self.workout : List[Workout] = []
        self.num_workouts = 0
        User.numbers += 1


    '''def update(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        return self'''
    
    def activate(self):
        self.active = True

    def get_id(self) -> int:
        return self.id

        return self

    '''def __repr__(self):
        return f' {self.exercise}'
    '''
    def able_to_login(self, email, password) -> bool:
        return email == self.email and password == self.password
    def get_username(self):
        return self.email

    def get_workout(self) -> List[Workout]:
        return self.workout
    def create_workout(self, name = None, discription = ""):
        self.workout.append(Workout(len(self.workout) + 1, [], name, discription))
        self.num_workouts += 1

    def delete_workout(self, workout):
        self.workout.remove(workout)
        self.num_workouts -= 1
    def add_exercise(self, exercise):
        self.workout[self.num_workouts - 1].add(exercise)

    def get_num_workouts(self) -> int:
        return self.num_workouts
