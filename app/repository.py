import json
from mapperWorkout import MapperWorkout

class WorkoutRepository:
    def save(self, workouts):
        with open("data.json", "w") as file:
            json.dump(
                [MapperWorkout.workout_to_dict(workout) for workout in workouts],
                  file
            )

    def load(self):
        try:
            with open("data.json", "r") as file:
                data = json.load(file)

                return [
                    MapperWorkout.workout_to_dict(workout)
                    for workout in data
                ]
            
        except:
            return []