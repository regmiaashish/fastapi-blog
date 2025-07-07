# main.py
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


app = FastAPI()


@app.get("/blog")
#This is how the queery parameters work
# we can use the query parameters to filter the data
# we can use the query parameters to limit the data
def index(limit: int, published: bool, str: Optional[str] = None):
    if published:
        return {"data": f"all published blogs with limit {limit}"}
    else:
        return {"data": "all blogs in db", "limit": limit}


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


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool] 

@app.post("/blog")
# to create a new blog we need to use the post method   
def createblog(blog: Blog):
    # here we can use the blog object to create a new blog
    # we can use the blog object to save the blog to the database
    return {"data": f"blog created with title {blog.title}"}
