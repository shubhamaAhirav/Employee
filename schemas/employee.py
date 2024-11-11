from pydantic import BaseModel

class EmployeeBase(BaseModel):
    name: str
    age: int
    position: str
    department: str

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: int

    class Config:
        orm_mode = True
