# main.py
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"data": "bloglist"}


@app.get("/blog/bestselling")
# FastAPI read the file line by line
# to check this , drag this route below the blog/{id} route
## this will not work as expected
# this is because FastAPI matches the routes in the order they are defined
def bestselling():

    return {"data": "bestselling blogs"}


@app.get("/blog/{id}")
# to get the dynamic data we need to put it into the paranthesis
def showblog(id: int):

    # fetch blog with id = id

    return {"id": id}


@app.get("/blog/{id}/comments")
def showblogcomments(id: int):

    # fetch blog comments with blog id = id

    return {"data": f"comments for blog {id}"}
