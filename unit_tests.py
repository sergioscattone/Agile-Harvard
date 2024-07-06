import unittest
from excercise import Exercise
from workload import Workload
from user import User

class Testing(unittest.TestCase):
    def test_framework_works(self):
        self.assertEqual(True, True)

    # test the creation of an exercise
    def test_create_excersise(self):
        id = 1
        name = "Excercise name 1"
        description = "Exercise description 1"
        exercise = Exercise(id, name, description)

        self.assertEqual(id, exercise.id, "Excercise ID does not match")
        self.assertEqual(name, exercise.name, "Excercise name does not match")
        self.assertEqual(description, exercise.description, "Excercise description does not match")

    # test the update of an exercise
    def test_update_excersise(self):
        id = 1
        name = "Excercise name 1"
        description = "Exercise description 1"
        exercise = Exercise(id, name, description)

        name_modified = "Excercise name 1 modified"
        description_modified = "Exercise description 1 modified"
        exercise.update(name_modified, description_modified)

        self.assertEqual(id, exercise.id, "Excercise ID does not match")
        self.assertEqual(name_modified, exercise.name, "Excercise name does not match")
        self.assertEqual(description_modified, exercise.description, "Excercise description does not match")
    
    # test the creation of a workload
    def test_create_workload(self):
        id = 1
        exercises = []
        workload_description = "Workload description 1"
        workload = Workload(id, exercises, workload_description)
        self.assertEqual(id, workload.id, "Worload id field does not match")
        self.assertEqual(exercises, workload.exercises, "Worload exercises list does not match")

    # test we can add exercises to a workload
    def test_add_exercise_to_workload(self):
        id = 1
        name = "Excercise name 1"
        description = "Exercise description 1"
        first_exercise = Exercise(id, name, description)
        workload_description = "Workload description 1"
        workload = Workload(id, [ first_exercise ], workload_description)

        # here exercises should be one
        self.assertEqual(1, len(workload.exercises), "Worload exercises list does not match")

        id = 2
        name = "Excercise name 2"
        description = "Exercise description 2"
        second_exercise = Exercise(id, name, description)
        workload.add(second_exercise)

        # here exercises should be two
        self.assertEqual(2, len(workload.exercises), "Add exercises to a workload does not work")

    # test we can remove exercises from a workload
    def test_remove_exercise_from_workload(self):
        exercises = []
        id = 1
        name = "Excercise name 1"
        description = "Exercise description 1"
        first_exercise = Exercise(id, name, description)
        exercises.append(first_exercise)
        
        id = 2
        name = "Excercise name 2"
        description = "Exercise description 2"
        second_exercise = Exercise(id, name, description)
        exercises.append(second_exercise)
        
        # We initialize a workload with two exercises
        workload_description = "Workload description 1"
        workload = Workload(id, exercises, workload_description)
        # here exercises should be two
        self.assertEqual(2, len(workload.exercises), "Worload exercises list does not match")
        
        workload.remove(first_exercise)
        # here exercises should be one
        self.assertEqual(1, len(workload.exercises), "Remove exercise from workload does not work")

        workload.remove(second_exercise)
        # here exercises should be zero
        self.assertEqual(0, len(workload.exercises), "Remove exercise from workload does not work")

    # test we can find exercises in a workload
    def test_find_exercise_in_workload(self):
        exercises = []
        id = 1
        name = "Excercise name 1"
        description = "Exercise description 1"
        first_exercise = Exercise(id, name, description)
        exercises.append(first_exercise)
        
        id = 2
        name = "Excercise name 2"
        description = "Exercise description 2"
        second_exercise = Exercise(id, name, description)
        exercises.append(second_exercise)
        
        # We initialize a workload with two exercises
        workload_description = "Workload description 1"
        workload = Workload(id, exercises, workload_description)

        # Now we are going to find the exercise with ID 1, the first one
        first_exercise_find = workload.find(1)
        self.assertEqual(first_exercise.id, first_exercise_find.id, "Workload find is not getting the exercises")
        self.assertEqual(first_exercise.name, first_exercise_find.name, "Workload find is not getting the exercises")
        self.assertEqual(first_exercise.description, first_exercise_find.description, "Workload find is not getting the exercises")

    # test the creation of an user
    def test_create_user(self):
        id = 1
        email = "user@email.com"
        first_name = "FirstName"
        last_name = "LastName"
        user = User(id, email, first_name, last_name)

        self.assertEqual(id, user.id, "User ID does not match")
        self.assertEqual(email, user.email, "User email does not match")
        self.assertEqual(first_name, user.first_name, "Excercise first name does not match")
        self.assertEqual(last_name, user.last_name, "Excercise last name does not match")

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
        self.assertEqual(first_name, user.first_name, "Excercise first name does not match")
        self.assertEqual(last_name, user.last_name, "Excercise last name does not match")

        first_name_modified = "FirstNameModified"
        last_name_modified = "LastNameModified"
        user.update(first_name_modified, last_name_modified)

        # here we validate that only the first name and last name were update
        # and nothing else since the update method only accepts those fields to change
        self.assertEqual(id, user.id, "User ID does not match")
        self.assertEqual(email, user.email, "User email does not match")
        self.assertEqual(first_name_modified, user.first_name, "Excercise first name does not match")
        self.assertEqual(last_name_modified, user.last_name, "Excercise last name does not match")

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