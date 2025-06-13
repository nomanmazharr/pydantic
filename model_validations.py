from pydantic import BaseModel, model_validator, EmailStr
from typing import ClassVar

class Patient(BaseModel):
    name: str
    age: int
    email: EmailStr
    allowed_domains: ClassVar[list[str]] = ['sps.com', 'voltic.ai']

    @model_validator(mode='after')
    def pateint_validator(cls, value):

        domain_name = value.email.split('@')[-1]

        if value.age> 60 and domain_name in cls.allowed_domains:
            raise ValueError('Patient has been retired from the company')

        return value

patient_info = {'name':'Bilal', 'age':65, 'email': 'ali@sps.com'}
# patient_info = {'name':'Bilal', 'age':65, 'email': 'ali@sp.com'}

patient1 = Patient(**patient_info)

print(patient1)