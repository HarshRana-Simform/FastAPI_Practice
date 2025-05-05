from fastapi import FastAPI, Query
from typing import Optional, Annotated
from pydantic import BaseModel
from . import schemas

app = FastAPI()


@app.get('/')
def home():
    return {"data": "This is the blog home page."}


# Query parameters
@app.get('/blog/list')
def blog_list(limit: Annotated[
    int | None,
    Query(alias="Limit-blogs",
          title="Limit",
          description="Provide a limit to be set:",
          deprecated=True)
] = None):
    return {"Query parasm Passed": f"Limit is set to: {limit}"}

# Post , Request body


@app.post('/blog/create')
def blog_create(request: schemas.Blog, user: schemas.User):
    result = {**request.model_dump(), "code": "Added filled."}
    print(result)
    print(request.model_dump())
    return request, user

# Path parameters


@app.get('/blog/{id}')
def blog(id: int):
    return id
