from pydantic import BaseModel


class CreatePostRequest(BaseModel):
    topic: str
