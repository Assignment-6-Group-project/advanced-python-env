import json

def create_json():
    data = [
        {"name": "Alice", "age": 19, "grades": [90, 85, 92]},
        {"name": "Bob", "age": 20, "grades": [75, 80, 70]},
        {"name": "Charlie", "age": 18, "grades": [100, 95, 98]}
    ]

    with open("students.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
