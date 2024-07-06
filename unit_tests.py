import unittest
from exercise import Exercise
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
        id = 1
        email = "user@email.com"
        first_name = "FirstName"
        last_name = "LastName"
        user = User(id, email, first_name, last_name)

        self.assertEqual(id, user.id, "User ID does not match")
        self.assertEqual(email, user.email, "User email does not match")
        self.assertEqual(first_name, user.first_name, "Exercise first name does not match")
        self.assertEqual(last_name, user.last_name, "Exercise last name does not match")

    # test the update of an user
    def test_update_user(self):
        id = 1
        email = "user@email.com"
        first_name = "FirstName"
        last_name = "LastName"
        user = User(id, email, first_name, last_name)

        # here we assert the field values are the original ones
        self.assertEqual(id, user.id, "User ID does not match")
        self.assertEqual(email, user.email, "User email does not match")
        self.assertEqual(first_name, user.first_name, "Exercise first name does not match")
        self.assertEqual(last_name, user.last_name, "Exercise last name does not match")

        first_name_modified = "FirstNameModified"
        last_name_modified = "LastNameModified"
        user.update(first_name_modified, last_name_modified)

        # here we validate that only the first name and last name were update
        # and nothing else since the update method only accepts those fields to change
        self.assertEqual(id, user.id, "User ID does not match")
        self.assertEqual(email, user.email, "User email does not match")
        self.assertEqual(first_name_modified, user.first_name, "Exercise first name does not match")
        self.assertEqual(last_name_modified, user.last_name, "Exercise last name does not match")

    # test the activation of an user
    def test_activate_user(self):
        id = 1
        email = "user@email.com"
        first_name = "FirstName"
        last_name = "LastName"
        user = User(id, email, first_name, last_name)
        self.assertEqual(False, user.active, "User activate does not match")

        # we activate the user 
        # Eventually this will happen when the user confirm the email
        user.activate()
        self.assertEqual(True, user.active, "User activate does not match")


if __name__ == '__main__':
    unittest.main()