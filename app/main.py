from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def first():
    response = {"hello":"world"}
    return response