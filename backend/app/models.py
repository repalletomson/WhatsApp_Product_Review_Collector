from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from .database import Base
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Review(Base):
    __tablename__ = "reviews"
    
    id = Column(Integer, primary_key=True, index=True)
    contact_number = Column(String, nullable=False)
    user_name = Column(String, nullable=False)
    product_name = Column(String, nullable=False)
    product_review = Column(Text, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

class ReviewResponse(BaseModel):
    id: int
    contact_number: str
    user_name: str
    product_name: str
    product_review: str
    created_at: datetime
    
    class Config:
        orm_mode = True

class ConversationState(BaseModel):
    contact_number: str
    step: str
    product_name: Optional[str] = None
    user_name: Optional[str] = None