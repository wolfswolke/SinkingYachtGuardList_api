import os

from fastapi import FastAPI
from fastapi.datastructures import State
from contextlib import asynccontextmanager
from routes import general, backend
from services.api_handler import yacht_handler

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Manages the FastAPI application's startup and shutdown lifecycle events.

    Establishes an asynchronous connection to Redis on startup and ensures the connection is closed on shutdown.
    """
    print("Starting up...")
    if base_url is None:
        raise ValueError("BASE_URL environment variable is not set.")
    yacht_handler.setup(base_url=base_url, holding_time=holding_time)

    yield
base_url = os.getenv("BASE_URL")
holding_time = int(os.getenv("HOLDING_TIME", 86400))

app = FastAPI(lifespan=lifespan)

app.include_router(general.router)
app.include_router(backend.router)