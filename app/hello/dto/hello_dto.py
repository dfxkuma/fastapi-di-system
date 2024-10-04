from pydantic import BaseModel, Field


class EnterNameDto(BaseModel):
    name: str = Field(..., description="Your Name", examples=["Hobin Jwa"])


class WriteMessageDto(BaseModel):
    username: str = Field(..., description="Your Name", examples=["Hobin Jwa"])
    message: str = Field(..., description="Your Message", examples=["Hello, World!"])
