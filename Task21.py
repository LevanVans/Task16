import json

class Address:
    def __init__(self, city, street):
        self.city = city
        self.street = street

    def to_dict(self):
        return {"city": self.city, "street": self.street}

class Student:
    row_id_counter = 1 

    def __init__(self, name, mark, address):
        self.row_id = Student.row_id_counter 
        Student.row_id_counter += 1
        self.name = name
        self.mark = mark
        self.address = address.to_dict()

    def to_dict(self):
        return {"row_id": self.row_id, "name": self.name, "mark": self.mark, "address": self.address}


address1= Address("Tbilisi", "Didube")
student1 = Student("Levani", 95, address1)



def save_students(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file )


def load_students(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

json.dumps(address1.to_dict())
json.dumps(student1.to_dict(),)

students = []


for data in load_students('students.json'):
    mark = int(data["mark"])
    
    if mark >= 91:
        grade = "A"
    elif mark >= 81:
        grade = "B"
    elif mark >= 71:
        grade = "C"
    else:
        grade = "D"

    data["mark"] = str(mark) 
    data["grade"] = grade


    students.append(data)
    
    
save_students(students, "students.json")


loaded_students_updated = load_students("students_updated.json")


print(json.dumps(loaded_students_updated, indent=2))
