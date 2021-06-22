from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import home

app = FastAPI()


app.include_router(home.router)
