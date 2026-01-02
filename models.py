from sqlmodel import  SQLModel, Field
import time

class ChatHistory(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key=True)
  user_id: int
  content: str
  role: str
  timestamp: float = Field( default_factory = time.time )  