class User():
    numbers = 0
    max_attempts = 5

    def __init__(self, email: str, password: str):
        self.id = User.numbers + 1
        self.email = email
        self.password = password
        self.active = False
        self.workouts = []
        self.attempts = 0
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
            self.attempts = self.attempts + 1

        return False

    def get_username(self):
        return self.email

    def add_workout(self, workout):
        self.workouts.append(workout)
        return self
    
    def find_workout(self, workout_id):
        for workout in self.workouts:
            if workout.id == workout_id:
                return workout
    
    def remove_workout(self, workout_id):
        for workout in self.workouts:
            if workout.id == workout_id:
                self.workouts.remove(workout)

    def remove_all_workouts(self):
        self.workouts = []
