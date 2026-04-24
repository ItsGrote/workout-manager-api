from flask import Blueprint, request, jsonify
from controller import WorkoutController
from mapperWorkout import MapperWorkout
from repository import WorkoutRepository

workout_bp = Blueprint("workout", __name__)

repo = WorkoutRepository()
workouts_data = repo.load()

controller = WorkoutController(workouts_data, repo)

@workout_bp.route("/workouts", methods=["POST"])
def create_workout():
    data = request.get_json(force=True)

    if not data or "name" not in data or "date" not in data:
        return jsonify({"error" : "dados invalidos"}), 400

    try:
        workout = controller.make_workout(
            data["name"],
            data["date"]
        )

        return jsonify(MapperWorkout.workout_to_dict(workout)), 201
    
    except ValueError as e:
        return jsonify({"error" : str(e)})

@workout_bp.route("/workouts/<int:workout_id>/exercises", methods=["POST"])
def add_exercises(workout_id):
    data = request.get_json(force=True)

    if not data or "name" not in data or "sets" not in data:
        return jsonify({"error" : "dados invalidos"}), 400

    try:
        workout = controller.add_exercise(
            workout_id,
            data["name"],
            data["sets"]
        )

        return jsonify(MapperWorkout.workout_to_dict(workout)), 200
    
    except ValueError as e:
        return jsonify({"error" : str(e)}), 400

@workout_bp.route("/workouts", methods=["GET"])
def list_workout():
    workouts = controller.list_workouts()

    return jsonify([
        MapperWorkout.workout_to_dict(workout)
        for workout in workouts
    ])

@workout_bp.route("/workouts/<int:workout_id>", methods=["GET"])
def list_workout_by_id(workout_id):
    try:
        workout = controller.find_workout_by_id(workout_id)

        return jsonify(MapperWorkout.workout_to_dict(workout))
    
    except ValueError as e:
        return jsonify({"error" : str(e)}), 404
    
@workout_bp.route("/workouts/<int:workout_id>", methods=["DELETE"])
def delete_workout(workout_id):
    try:
        controller.del_workout(workout_id)

        return jsonify({"message" : "Treino deletado com sucesso"}), 200
    
    except ValueError as e:
        return jsonify({"error", str(e)}), 404
    
@workout_bp.route("/workouts/<int:workout_id>/exercises/<int:exercise_id>", methods=["DELETE"])
def del_exercise(workout_id, exercise_id):
    try:
        controller.delete_exercise(workout_id, exercise_id)
        return jsonify({"message" : "exercicio deletado com sucesso"})
    
    except ValueError as e:
        return jsonify({"error" : str(e)}), 404
    
@workout_bp.route("/workouts/<int:workout_id>", methods=["PUT"])
def update_workout(workout_id):
    data = request.get_json(force=True)

    if not data:
        return jsonify({"error" : "dados invalidos"}), 400
    
    try:
        workout = controller.update_workout(
            workout_id, 
            data.get("name"),
            data.get("date")
        )

        return jsonify(MapperWorkout.workout_to_dict(workout)), 200
    
    except ValueError as e:
        return jsonify({"error" : str(e)}), 404

@workout_bp.route("/workouts/<int:workout_id>/exercises/<int:exercise_id>", methods=["PUT"])  
def update_exercise(workout_id, exercise_id):
    data = request.get_json(force=True)

    if not data:
        return jsonify({"error" : "dados invalidos"}), 400

    try:

        workout = controller.update_exercise(
            workout_id,
            exercise_id,
            data.get("name"),
            data.get("sets")
        )

        return jsonify(MapperWorkout.workout_to_dict(workout)), 200
    
    except ValueError as e:
        return jsonify({"error" : str(e)}), 404
