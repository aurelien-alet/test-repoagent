from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/another-endpoint")
async def root():
    return {"message": "Another endpoint"}
