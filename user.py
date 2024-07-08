from workout import Workout
from typing import List


class User():
    max_attempts: int = 10000
    def __init__(self, id, email: str, password: str):
        self.id = id
        self.email = email
        self.password = password
        self.active = False
        self.workouts : List[Workout] = []
        self.attempts = 0
        self.num_workouts = 0


    '''def update(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        return self'''
    
    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def get_id(self) -> int:
        return self.id

    '''def __repr__(self):
        return f' {self.exercise}'
    '''

    def able_to_login(self, email, password) -> bool:
        if self.attempts >= User.max_attempts:
            self.deactivate()
            return False
        if email != self.email:
            return False
        if password == self.password:
            return True
        else:
            self.attempts += 1
        return False

    def get_username(self):
        return self.email

    def get_workout(self) -> List[Workout]:
        return self.workouts

    def create_workout(self, name = None, discription = ""):
        self.workouts.append(Workout(len(self.workouts) + 1, [], name, discription))
        self.num_workouts += 1

    def delete_workout(self, workout):
        self.workout.remove(workout)
        self.num_workouts -= 1

    def remove_workout_by_id(self, id):
        for workout in self.workouts:
            if workout.id == id:
                self.workouts.remove(workout)
                self.num_workouts -= 1

    def find_workout_by_id(self, id):
        for workout in self.workouts:
            if workout.id == id:
                return workout

    def add_exercise(self, exercise):
        self.workouts[self.num_workouts - 1].add(exercise)

    def add_workout(self, workout):
        self.num_workouts += 1
        self.workouts.append(workout)

    def get_num_workouts(self) -> int:
        return self.num_workouts

    def remove_all_workouts(self):
        self.workouts = []
        self.num_workouts = 0
