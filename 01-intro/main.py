from typing import Optional
from fastapi import FastAPI
from enum import Enum

myApp = FastAPI()


@myApp.get("/hello")
def index():
    return {"message": "Hello World"}


# @myApp.get("/blog/all")
# def get_all_blogs():
#     return {"data": "All blogs"}


# @myApp.get("/blog/all")
# def get_all_blogs(page=1, page_size=10):
#     return {"data": f"Page: {page} and Page Size: {page_size}"}


@myApp.get("/blog/all")
def get_all_blogs(page=1, page_size: Optional[int] = None):
    return {"data": f"Page: {page} and Page Size: {page_size}"}


@myApp.get("/blog/{id}/comments/{comment_id}")
def get_comment(
    id: int, comment_id: int, valid: bool = True, username: Optional[str] = None
):
    return {
        "data": f"Blog ID: {id} and Comment ID: {comment_id}, Valid: {valid}, Username: {username}"
    }


class BlogType(str, Enum):
    short = "short"
    story = "story"
    howto = "howto"


@myApp.get("/blog/type/{type}")
def get_blog_by_type(type: BlogType):
    return {"data": f"Blog type is {type.value}"}


@myApp.get("/blog/{id}")
def show(id: int):
    return {"data": f"Blog with id {id}"}
