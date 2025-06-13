from pydantic import BaseModel, Field, AnyUrl, EmailStr, computed_field
from typing import Literal, Annotated, Optional, List


class Patient(BaseModel):
    name: str = Field(..., description='name of the patient')
    age: int = Field(..., description='age of the patient')
    linkedin: AnyUrl = Field(..., description='linkedin url')
    email: EmailStr = Field(..., description='email of the patient')
    weight: Annotated[float, Field(..., description='weight of the patient')]
    height: Annotated[float, Field(..., description='heigh in meters')]
    married: Annotated[Literal['yes', 'No'], Field(description='married or not', default='No')]
    allergies: Annotated[Optional[List[str]], Field(description='patient allergies', max_length=3, default=None)]


    @computed_field
    @property
    def bmi_calculation(self) -> float:
        bmi = (self.weight / (self.height**2))
        return bmi



patient_info = {'name':'Ali', 'age':'30', 'linkedin':'https://linkedin.com', 'email':'ali@gmail.com', 'weight': 70.5, 'height': 5.10, 'allergies': ['pollen', 'dust']}

patient1 = Patient(**patient_info)
# print(patient1)
print(patient1)