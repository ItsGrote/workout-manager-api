from modelWorkout import Workout
from modelExercise import Exercise
from repository import WorkoutRepository
from utils import validate_date, validate_name, validate_number

class WorkoutService:
    def __init__(self, workout_data, repo):
        self.workouts = workout_data
        self.repo = repo
        self.exercise_service = ExerciseService()

        self._next_id = self._get_next_id()

    def _get_next_id(self):
        if not self.workouts:
            return 1
        
        return max(workout.id for workout in self.workouts) + 1

    def _get_next_exercise_id(self):
        all_ids = [
            exercise.id
            for workout in self.workouts
            for exercise in workout.exercises
        ]

        return max(all_ids, default=0) + 1

    def create_workout(self, name, date):
        validate_name(name)
        validate_date(date)

        workout = Workout(self._next_id, name, date)
        self._next_id += 1

        self.workouts.append(workout)

        self.repo.save(self.workouts)

        return workout
    
    def get_workout_by_id(self, workout_id):
        for workout in self.workouts:
            if workout.id == workout_id:
                return workout
        
        raise ValueError("workout nao encontrado")

    def add_exercise(self, workout, name, sets_data):
        exercise_id = self._get_next_exercise_id()

        exercise = self.exercise_service.create_exercise(
            exercise_id, name, sets_data
        )

        workout.exercises.append(exercise)

        self.repo.save(self.workouts)

    def delete_workout(self, workout_id):
        for index, workout in enumerate(self.workouts):
            if workout.id == workout_id:
                del self.workouts[index]

                self.repo.save(self.workouts)
                return
        
        raise ValueError("Treino nao encontrado")

    def  get_all_workout(self):
        return self.workouts
    
    def edit_workout(self, workout_id, name=None, date=None):
        if name is not None:
            validate_name(name)

        if date is not None:
            validate_date(date)

        for workout in self.workouts:
            if workout.id == workout_id:
                if name is not None:
                    workout.name = name

                if date is not None:
                    workout.date = date

                self.repo.save(self.workouts)
                return workout

        raise ValueError("Treino nao encontrado")        

    def _validate_workout(self, workout, exercise):
        if not isinstance(workout, Workout):
            raise ValueError("workout invalido!")
    
        if not isinstance(exercise, Exercise):
            raise ValueError("exercise invalido!")

class ExerciseService:
    

    def create_exercise(self, id, name, sets_data):
         self._validate_sets(sets_data)
         validate_name(name)

         exercise = Exercise(id, name, sets_data)

         return exercise
    
    def remove_exercise(self, workout, exercise_id):
        for index, exercise in enumerate(workout.exercises):
            if exercise.id == exercise_id:
                del workout.exercises[index]
                return 
        
        raise ValueError("Exercicio nao encontrado")
    
    def edit_exercise(self, workout, exercise_id, name=None, sets_data=None):
        if name is not None:
            validate_name(name)
        
        if sets_data is not None:
            if not isinstance(sets_data, list):
                raise ValueError("Dados invalido")
            
            for sets in sets_data:
                if "reps" not in sets or "weight" not in sets:
                    raise ValueError("Formato invalido")
                
                validate_number(sets["reps"])
                validate_number(sets["weight"])
        
        for exercise in workout.exercises:
            if exercise.id == exercise_id:
                if name is not None:
                    exercise.name = name

                if sets_data is not None:
                    exercise.sets_data = sets_data

                return exercise

        raise ValueError("Exercicio nao encontrado")

            


    def _validate_sets(self, sets_data):
        if not isinstance(sets_data, list):
            raise ValueError("Erro! Nao e uma lista")

        if len(sets_data) == 0:
            raise ValueError("Lista vazia! Preencha para continuar.")
        
        for data in sets_data:
            if not isinstance(data, dict):
                raise ValueError("Cada set deve ser um objeto/")
            
            reps = data["reps"]
            weight = data["weight"]

            if not isinstance(reps, int) or not isinstance(weight, (int, float)):
                raise ValueError("Valores invalidos!")
            
            if reps <= 0 or weight < 0:
                raise ValueError("Valores invalidos!")
    