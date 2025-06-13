from pydantic import BaseModel, Field, AnyUrl, EmailStr
from typing import Literal, Annotated, Optional, List


class Patient(BaseModel):
    name: str = Field(..., description='name of the patient')
    age: int = Field(..., description='age of the patient')
    linkedin: AnyUrl = Field(..., description='linkedin url')
    email: EmailStr = Field(..., description='email of the patient')
    weight: Annotated[float, Field(..., description='weight of the patient')]
    married: Annotated[Literal['yes', 'No'], Field(description='married or not', default='No')]
    allergies: Annotated[Optional[List[str]], Field(description='patient allergies', max_length=3, default=None)]

def update_patient_data(patient: Patient):
    patient.name = 'Ahmad'
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')

patient_info = {'name':'Ali', 'age':'30', 'linkedin':'https://linkedin.com', 'email':'ali@gmail.com', 'weight': 70.5, 'allergies': ['pollen', 'dust']}

patient1 = Patient(**patient_info)
# print(patient1)

print(update_patient_data(patient1))