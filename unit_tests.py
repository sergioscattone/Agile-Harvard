import unittest
from exercise import Exercise
from exercise_history import Exercise_History
from workout import Workout
from user import User

class Testing(unittest.TestCase):
    def test_framework_works(self):
        self.assertEqual(True, True)

    # test the creation of an exercise
    def test_create_exercise(self):
        id = 1
        name = "Exercise name 1"
        description = "Exercise description 1"
        exercise = Exercise(id, name, description)

        self.assertEqual(id, exercise.id, "Exercise ID does not match")
        self.assertEqual(name, exercise.name, "Exercise name does not match")
        self.assertEqual(description, exercise.description, "Exercise description does not match")

    # test the update of an exercise
    def test_update_exercise(self):
        id = 1
        name = "Exercise name 1"
        description = "Exercise description 1"
        exercise = Exercise(id, name, description)

        name_modified = "Exercise name 1 modified"
        description_modified = "Exercise description 1 modified"
        exercise.update(name_modified, description_modified)

        self.assertEqual(id, exercise.id, "Exercise ID does not match")
        self.assertEqual(name_modified, exercise.name, "Exercise name does not match")
        self.assertEqual(description_modified, exercise.description, "Exercise description does not match")
    
    # test the creation of a workout
    def test_create_workout(self):
        id = 1
        exercises = []
        workout_description = "Workout description 1"
        workout = Workout(id, exercises, workout_description)
        self.assertEqual(id, workout.id, "Workout id field does not match")
        self.assertEqual(exercises, workout.exercises, "Workout exercises list does not match")

    # test we can add exercises to a workout
    def test_add_exercise_to_workout(self):
        id = 1
        name = "Exercise name 1"
        description = "Exercise description 1"
        first_exercise = Exercise(id, name, description)
        workout_description = "Workout description 1"
        workout = Workout(id, [ first_exercise ], workout_description)

        # here exercises should be one
        self.assertEqual(1, len(workout.exercises), "Workload exercises list does not match")

        id = 2
        name = "Exercise name 2"
        description = "Exercise description 2"
        second_exercise = Exercise(id, name, description)
        workout.add(second_exercise)

        # here exercises should be two
        self.assertEqual(2, len(workout.exercises), "Add exercises to a workout does not work")

    # test we can remove exercises from a workout
    def test_remove_exercise_from_workout(self):
        exercises = []
        id = 1
        name = "Exercise name 1"
        description = "Exercise description 1"
        first_exercise = Exercise(id, name, description)
        exercises.append(first_exercise)
        
        id = 2
        name = "Exercise name 2"
        description = "Exercise description 2"
        second_exercise = Exercise(id, name, description)
        exercises.append(second_exercise)
        
        # We initialize a workout with two exercises
        workout_description = "Workout description 1"
        workout = Workout(id, exercises, workout_description)
        # here exercises should be two
        self.assertEqual(2, len(workout.exercises), "Workout exercises list does not match")
        
        workout.remove(first_exercise)
        # here exercises should be one
        self.assertEqual(1, len(workout.exercises), "Remove exercise from workout does not work")

        workout.remove(second_exercise)
        # here exercises should be zero
        self.assertEqual(0, len(workout.exercises), "Remove exercise from workout does not work")

    # test we can find exercises in a workout
    def test_find_exercise_in_workout(self):
        exercises = []
        id = 1
        name = "Exercise name 1"
        description = "Exercise description 1"
        first_exercise = Exercise(id, name, description)
        exercises.append(first_exercise)
        
        id = 2
        name = "Exercise name 2"
        description = "Exercise description 2"
        second_exercise = Exercise(id, name, description)
        exercises.append(second_exercise)
        
        # We initialize a workout with two exercises
        workout_description = "Workout description 1"
        workout = Workout(id, exercises, workout_description)

        # Now we are going to find the exercise with ID 1, the first one
        first_exercise_find = workout.find(1)
        self.assertEqual(first_exercise.id, first_exercise_find.id, "Workout find is not getting the exercises")
        self.assertEqual(first_exercise.name, first_exercise_find.name, "Workout find is not getting the exercises")
        self.assertEqual(first_exercise.description, first_exercise_find.description, "Workout find is not getting the exercises")

    # test the creation of an user
    def test_create_user(self):
        email = "user@email.com"
        password = "password"
        user = User(email, password)

        self.assertEqual(email, user.email, "User email does not match")
        self.assertEqual(password, user.password, "User password does not match")
        User.numbers = 0
        
    # test if the user is able to login
    def test_user_is_able_to_login(self):
        email = "user@email.com"
        password = "password"
        user = User(email, password)

        # here the use is able to loggin
        self.assertEqual(True, user.able_to_login(email, password))
        User.numbers = 0

    # test the activation of an user
    def test_activate_user(self):
        email = "user@email.com"
        password = "password"
        user = User(email, password)
        self.assertEqual(False, user.active, "User activate does not match")

        # we activate the user 
        # Eventually this will happen when the user confirm the email
        user.activate()
        self.assertEqual(True, user.active, "User activate does not match")
        User.numbers = 0

    # test get id from user
    def test_get_id_from_user(self):
        # Create user
        email = "user@email.com"
        password = "password"
        user = User(email, password)
        self.assertEqual(1, user.id)

        # Create another user, ID should be next number
        email = "user2@email.com"
        password = "password2"
        user2 = User(email, password)
        self.assertEqual(2, user2.id)
        User.numbers = 0
    
    # test get username from suer
    def test_get_username_from_user(self):
        # Create user
        email = "user@email.com"
        password = "password"
        user = User(email, password)
        self.assertEqual(email, user.get_username())
        User.numbers = 0

    # test the deactivation of an user
    def test_deactivate_user(self):
        email = "user@email.com"
        password = "password"
        user = User(email, password)
        user.activate()
        self.assertEqual(True, user.active, "User activate does not match")
        user.deactivate()
        self.assertEqual(False, user.active, "User activate does not match")
        User.numbers = 0

    # test user gets deactivated after max attempts to login
    def test_user_gets_deactivated_after_max_attempts_to_login(self):
        # Create user
        email = "user@email.com"
        password = "password"
        user = User(email, password)
        # we verify the user is active
        user.activate()
        self.assertEqual(True, user.active)

        # we verify the correct password do not block the user
        for i in range(User.max_attempts+1):
            user.able_to_login(user.email, user.password)
        self.assertEqual(True, user.active)

        # now we will try to login with a wrong password
        # until we deactivate the user
        for i in range(User.max_attempts+1):
            user.able_to_login(user.email, "wrong_password")
        self.assertEqual(False, user.active)
        User.numbers = 0

    # test remove workouts as user
    def test_remove_workouts_as_user(self):
        # Create user
        email = "user@email.com"
        password = "password"
        user = User(email, password)

        # Create exercise
        first_exercise_id = 1
        first_exercise_name = "Exercise name 1"
        first_exercise_description = "Exercise description 1"
        first_exercise = Exercise(
            first_exercise_id,
            first_exercise_name,
            first_exercise_description)
        
        # Create workout
        id = 1
        workout_description = "Workout description 1"
        first_workout = Workout(id, [ first_exercise ], workout_description)

        user.add_workout(first_workout)
        self.assertEqual(1, len(user.workouts))

        # Create another exercise
        second_exercise_id = 2
        second_name = "Exercise name 2"
        second_description = "Exercise description 2"
        second_exercise = Exercise(
            second_exercise_id,
            second_name,
            second_description)
        user.add_workout(second_exercise)
        self.assertEqual(2, len(user.workouts))

        # remove a particular workload
        user.remove_workout_by_id(1)
        self.assertEqual(1, len(user.workouts))

        User.numbers = 0

    # test remove all workouts as user
    def test_remove_all_workouts_as_user(self):
        # Create user
        email = "user@email.com"
        password = "password"
        user = User(email, password)

        # Create exercise
        first_exercise_id = 1
        first_exercise_name = "Exercise name 1"
        first_exercise_description = "Exercise description 1"
        first_exercise = Exercise(
            first_exercise_id,
            first_exercise_name,
            first_exercise_description)
        
        # Create first workout
        first_workout_id = 1
        first_workout_description = "Workout description 1"
        first_workout = Workout(first_workout_id, [ first_exercise ], first_workout_description)
        user.add_workout(first_workout)

        # Create another exercise
        second_exercise_id = 2
        second_name = "Exercise name 2"
        second_description = "Exercise description 2"
        second_exercise = Exercise(
            second_exercise_id,
            second_name,
            second_description)
        
        # Create second workout
        second_workout_id = 2
        second_workout_description = "Workout description 2"
        second_workout = Workout(second_workout_id, [ second_exercise ], second_workout_description)
        user.add_workout(second_workout)

        # remove all workouts in a single action
        user.remove_all_workouts()
        self.assertEqual(0, len(user.workouts))

        User.numbers = 0

    # Create history of exercises for an user
    def test_exercise_history_for_an_user(self):
        # Create exercise
        first_exercise_id = 1
        first_exercise_name = "Exercise name 1"
        first_exercise_description = "Exercise description 1"
        first_exercise = Exercise(
            first_exercise_id,
            first_exercise_name,
            first_exercise_description)
        
        # Create user
        email = "user@email.com"
        password = "password"
        user = User(email, password)

        # Create exercise history for user\
        id = 1
        user_exercise_history = Exercise_History(id, [ first_exercise ], user)
        self.assertTrue(id, user_exercise_history.id)
        self.assertTrue(first_exercise, user_exercise_history.exercise)
        self.assertTrue(user, user_exercise_history.user)

        Exercise_History.history = []
        User.numbers = 0

    # Fetch history of exercises for an user
    def test_get_history_from_user(self):
        # Create first user
        email = "user@email.com"
        password = "password"
        first_user = User(email, password)

        # Create second user
        email = "user2@email.com"
        password = "password2"
        second_user = User(email, password)

        amount_exercises_to_test = 3
        exercises_created = []
        for i in range(amount_exercises_to_test):
            # Create exercise
            exercise_id = i
            exercise_name = "Exercise name " + str(i)
            exercise_description = "Exercise description " + str(i)
            exercise = Exercise(exercise_id, exercise_name, exercise_description)
            # Create exercise history for user
            exercises_created.append(exercise)
            if i < 2:
                Exercise_History(i, [ exercise ], first_user)
            else:
                Exercise_History(i, [ exercise ], second_user)

        self.assertEqual(3, len(Exercise_History.history))
        exercises_history = Exercise_History.get_history_from_user(first_user)
        # history for first user should be only 2, not 3
        self.assertEqual(amount_exercises_to_test-1, len(exercises_history))
        
        for i in range(len(exercises_history)):
            self.assertEqual(exercises_created[i].id, exercises_history[i].id)
            self.assertEqual(first_user, exercises_history[i].user)
            self.assertIsNotNone(exercises_history[i].timestamp)

        Exercise_History.history = []
        User.numbers = 0

    # Test get self from workout
    def test_get_self_from_workout(self):
        id = 1
        name = "Exercise name 1"
        description = "Exercise description 1"
        first_exercise = Exercise(id, name, description)
        workout_description = "Workout description 1"
        workout = Workout(id, [ first_exercise ], workout_description)

        self.assertEqual('Workout description 1\n', workout.get_self())

    # test get_num_workouts from user
    def test_get_num_workouts(self):
        # Create first user
        email = "user@email.com"
        password = "password"
        user = User(email, password)
        self.assertEqual(0, user.get_num_workouts())

        # Assert that num_workouts increases when we create a workout
        user.create_workout()
        self.assertEqual(1, user.get_num_workouts())

if __name__ == '__main__':
    unittest.main()