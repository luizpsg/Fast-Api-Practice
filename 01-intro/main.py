from fastapi import FastAPI

myApp = FastAPI()


@myApp.get("/")
def index():
    return {"message": "Hello World"}
