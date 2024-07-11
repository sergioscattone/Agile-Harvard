import datetime


class Exercise_History():
    def __init__(self, workout, user_id):
        self.workout = workout
        self.user_id = user_id
        self.timestamp = str(datetime.datetime.now())


    def get_workout(self):
        return self.workout

    def get_user(self):
        return self.user_id

    def get_time(self):
        return self.timestamp.split()[0]

