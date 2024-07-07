from workout import Workout
from typing import List
class User():
    numbers = 0
    max_attempts: int = 5
    def __init__(self, email: str, password: str):
        self.id = User.numbers + 1
        self.email = email
        self.password = password
        self.active = False
        self.workout : List[Workout] = []
        self.attempts = 0
        self.num_workouts = 0
        User.numbers += 1


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

        return self

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
        return self.workout
    def create_workout(self, name = None, discription = ""):
        self.workout.append(Workout(len(self.workout) + 1, [], name, discription))
        self.num_workouts += 1

    def delete_workout(self, workout):
        self.workout.remove(workout)
        self.num_workouts -= 1

    def remove_workout_by_id(self, id):
        for workout in self.workout:
            if workout.id == id:
                self.workout.remove(workout)
                self.num_workouts -= 1

    def find_workout_by_id(self, id):
        for workout in self.workout:
            if workout.id == id:
                return workout

    def add_exercise(self, exercise):
        self.workout[self.num_workouts - 1].add(exercise)

    def get_num_workouts(self) -> int:
        return self.num_workouts

    def remove_all_workouts(self):
        for workout in self.workout:
            workout.remove()
        self.num_workouts = 0