from pydantic import BaseModel, Field
from typing import Optional


class Blog(BaseModel):
    title: str = Field(
        title="Title", description="Enter the title of your blog: ", max_length=200)
    description: str
    id: int
    published: Optional[bool] = None


class User(BaseModel):
    user_id: int
    user_name: str
