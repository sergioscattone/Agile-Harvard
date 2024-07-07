import datetime


class Exercise_History():
    history = []
    def __init__(self, id: int, exercise, user):
        self.id = id
        self.exercise = exercise
        self.user = user
        self.timestamp = str(datetime.datetime.now())
        Exercise_History.history.append(self)

    def get_history_from_user(user):
        history_user = []
        for history in Exercise_History.history:
            if history.user == user:
                history_user.append(history)
        return history_user