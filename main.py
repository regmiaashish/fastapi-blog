# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def main():
    return {'data': {'name': 'Aashish Regmi'}}

@app.get("/about")
def main():
    return {'data': {'name': 'About us section'}}