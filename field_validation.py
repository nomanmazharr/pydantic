from pydantic import BaseModel, field_validator, Field, EmailStr

class Patient(BaseModel):
    name: str
    age: int
    email: EmailStr

    # use this if we want some custom validation logic for a field
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        domains = ['sps.com', 'voltic.ai']
        domain_name = value.split('@')[-1]

        if domain_name not in domains:
            raise ValueError('Not a valid domain')

        return value

patient_info = {'name':'Bilal', 'age':40, 'email': 'ali@sps.com'}
# patient_info2 = {'name':'Bilal', 'age':40, 'email': 'ali@sp.com'}
patient1 = Patient(**patient_info)

print(patient1)