from service import *


class WorkoutController:
    def __init__(self, workout_data, repo):
        self.workout_service = WorkoutService(workout_data, repo)
        self.exercise_service = ExerciseService()

    def make_workout(self, name, date):
        return self.workout_service.create_workout(name, date)

    def add_exercise(self, workout_id, name, sets_data):
        workout = self.workout_service.get_workout_by_id(workout_id)

        self.workout_service.add_exercise(workout, name, sets_data)

        return workout
    
    def del_workout(self, workout_id):
        return self.workout_service.delete_workout(workout_id)
    
    def update_workout(self, workout_id, name=None, date=None):
        return self.workout_service.edit_workout(workout_id, name, date)
    
    def delete_exercise(self, workout_id, exercise_id):
        workout = self.workout_service.get_workout_by_id(workout_id)
        return self.exercise_service.remove_exercise(workout, exercise_id)
    
    def update_exercise(self, workout_id, exercise_id, name=None, sets_data=None):
        workout = self.workout_service.get_workout_by_id(workout_id)

        self.exercise_service.edit_exercise(workout, exercise_id, name, sets_data)

        return workout
    
    def find_workout_by_id(self, workout_id):
        return self.workout_service.get_workout_by_id(workout_id)
    
    def list_workouts(self):
        return self.workout_service.get_all_workout()




