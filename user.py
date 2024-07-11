from workout import Workout
from typing import List
from exercise_history import Exercise_History


class User():
    max_attempts: int = 10000

    def __init__(self, id, email: str, password: str):
        self.id = id
        self.email = email
        self.password = password
        self.active = False
        self.workouts: List[Workout] = []
        self.attempts = 0
        self.num_workouts = 0
        self.exercise_history :List[Exercise_History] = []

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
        return self.workouts if self.workouts is not None else []

    def create_workout(self, name=None, description=""):
        self.workouts.append(Workout(len(self.workouts) + 1, [], name, description))
        self.num_workouts += 1

    def delete_workout(self, workout):
        self.workouts.remove(workout)
        self.num_workouts -= 1

    def remove_workout_by_id(self, id):
        for workout in self.workouts:
            if workout.id == id:
                self.workouts.remove(workout)
                self.num_workouts -= 1

    def find_workout_by_name(self, name):
        for workout in self.workouts:
            if name in workout.name:
                return workout
        return None

    def find_workout_by_id(self, id):
        for workout in self.workouts:
            if workout.id == id:
                return workout

    def add_exercise(self, exercise, index = None):
        if index == None:
            self.workouts[self.num_workouts - 1].add(exercise)
        else:
            self.workouts[index].add(exercise)

    def add_workout(self, workout):
        self.num_workouts += 1
        self.workouts.append(workout)

    def get_num_workouts(self) -> int:
        return self.num_workouts

    def remove_all_workouts(self):
        self.workouts = []
        self.num_workouts = 0

    def display(self):
        return self.email + str(self.id)
    
    def remove_workout_by_name(self, name):
        workout = self.find_workout_by_name(name)
        self.remove_workout_by_id(workout.id)

    def delete_workout_by_id(self, id):
        self.workouts.pop(id)
        self.num_workouts -= 1

    def add_to_history(self, workout_index):
        self.exercise_history.append(Exercise_History(self.workouts[workout_index], user_id = self.id))

    def get_num_history(self) -> int:
        return len(self.exercise_history)
    def get_history(self):
        return self.exercise_history