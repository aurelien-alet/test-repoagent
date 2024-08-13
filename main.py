from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/another-endpoint")
async def another_endpoint():
    return {"message": "Another endpoint"}
