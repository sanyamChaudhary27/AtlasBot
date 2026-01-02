from  sqlmodel import SQLModel, create_engine, Session, select
from models import ChatHistory

file_name = "database.db"
engine = create_engine(f"sqlite:///{file_name}")
SQLModel.metadata.create_all(engine)
session = Session(engine)

def init_db():
   SQLModel.metadata.create_all(engine)
  

def get_history(
  user_id: int, 
  limit: int = 15
):
  with Session(engine) as session:
    statement = select(
      ChatHistory
    ).where(
      ChatHistory.user_id == user_id
    ).orderby(
      ChatHistory.timestamp.desc()
    ).limit(limit)
   
     
    results = session.exec(
      statement
    ).all()
    return sorted(
      results, 
      key=lambda x: x.id
    )
  
def save_message(
  user_id: int, 
  content: str, 
  role: str
):
   with Session(engine) as session:
      msg = ChatHistory(
        user_id=user_id,
        content=content,
        role=role
      )
      session.add(msg)
      session.commit()
      session.refresh(msg)

