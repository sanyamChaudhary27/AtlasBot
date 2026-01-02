import threading
import uvicron
from fasapi import FastAPI
from bot import start_bot
from database import init_db
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
   init_db()
   bot_thread = threading.Thread(target=start_bot)
   bot_thread.start()
   yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
def home():
  return  {"message": "Atlas is Online"}

if __name__ == "__main__":
   uvicorn.run(app, host="0.0.0.0", port=8000)