from dotenv import dotenv_values
from fastapi import FastAPI

from api.movies import movies

from api.db import metadata, database, engine

metadata.create_all(engine)

config = dotenv_values("keys.env")

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(movies)
