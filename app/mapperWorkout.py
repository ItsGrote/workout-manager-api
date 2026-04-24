
class MapperWorkout:
    @staticmethod
    def workout_to_dict(workout):
        return {
            "id" : workout.id,
            "name" : workout.name,
            "date" : workout.date,
            "exercises" : [
                {
                "id" : exercise.id,
                "name" : exercise.name,
                "sets" : exercise.sets_data
            }
                for  exercise in workout.exercises
            ]
        }
