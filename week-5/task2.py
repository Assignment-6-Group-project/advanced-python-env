import json

def create_json():
    data = [
        {"name": "Alice", "age": 19, "grades": [90, 85, 92]},
        {"name": "Bob", "age": 20, "grades": [75, 80, 70]},
        {"name": "Charlie", "age": 18, "grades": [100, 95, 98]}
    ]

    with open("students.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def process_json():
    with open("students.json", "r", encoding="utf-8") as f:
        students = json.load(f)

    for s in students:
        s["average"] = round(sum(s["grades"]) / len(s["grades"]))

    with open("students_updated.json", "w", encoding="utf-8") as f:
        json.dump(students, f, indent=4)

if __name__ == "__main__":
    create_json()
    process_json()