# Workout Manager API

A Python + Flask API for managing workouts and exercises.

## 📌 About the project
This project allows you to create and manage workouts and exercises using a clean layered architecture:
- Routes → Controller → Service → Repository

Data is currently stored in a JSON file (temporary persistence layer).

---

## 🧱 Architecture
- `app/routes.py` → HTTP endpoints
- `app/controller.py` → request orchestration
- `app/service.py` → business logic
- `app/repository.py` → data access layer
- `app/models/` → domain entities
- `app/mapper/` → data transformation layer

---

## 🚀 How to run

```bash
pip install -r requirements.txt
```
```bash
python app/app.py
```

---

## 📦 Technologies
- Python 
- Flask

---

## ⚙️  Project Status 
- This project was developed as a learning exercise to explore backend development with Flask and layered architecture.
- It implements a basic REST API for managing workouts and exercises.


