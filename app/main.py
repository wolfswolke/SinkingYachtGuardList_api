import os

from fastapi import FastAPI
from fastapi.datastructures import State
from contextlib import asynccontextmanager
from app.routes import general, backend
from services.api_handler import yacht_handler

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Manages the FastAPI application's startup and shutdown lifecycle events.

    Establishes an asynchronous connection to Redis on startup and ensures the connection is closed on shutdown.
    """
    print("Starting up...")
    yacht_handler.setup(base_url)

    yield
base_url = os.getenv("BASE_URL")
app = FastAPI(lifespan=lifespan)

app.include_router(general.router)
app.include_router(backend.router)