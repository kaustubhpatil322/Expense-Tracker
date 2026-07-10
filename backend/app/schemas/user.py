from pydantic import BaseModel,Field,EmailStr

class UserBase(BaseModel):
    name: str = Field(
        min_length = 2,
        max_length=100,
        description= "Full name of the user",
    )
    email: EmailStr

class UserCreate(UserBase):
    password: str=Field(
        min_length=8,
        max_length=128,
        description="User Password",
    )

class UserResponse(UserBase):
    id: int
    model_config={
        "from_attributes": True
    }
    
class UserLogin(BaseModel):
    email: EmailStr
    password: str
