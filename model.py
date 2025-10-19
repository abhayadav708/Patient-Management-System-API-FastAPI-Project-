from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("inserted")


def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("updated")

Patient_info = {'name': 'John Doe', 'age': 30}
Patient1 = Patient(**Patient_info)

update_patient_data(Patient1)
