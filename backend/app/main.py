from fastapi import FastAPI, Depends, HTTPException, Form
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
import uvicorn

from .database import get_db, create_tables
from .models import Review, ReviewResponse
from .conversation import ConversationManager
from .whatsapp import WhatsAppService

app = FastAPI(title="WhatsApp Review Collector", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services
whatsapp_service = WhatsAppService()

@app.on_event("startup")
async def startup_event():
    create_tables()

@app.get("/")
async def root():
    return {"message": "WhatsApp Review Collector API"}

@app.get("/api/reviews", response_model=List[ReviewResponse])
async def get_reviews(db: Session = Depends(get_db)):
    """Get all reviews from the database"""
    reviews = db.query(Review).order_by(Review.created_at.desc()).all()
    return reviews

@app.post("/webhook/whatsapp")
async def whatsapp_webhook(
    From: str = Form(...),
    Body: str = Form(...),
    db: Session = Depends(get_db)
):
    """Handle incoming WhatsApp messages from Twilio"""
    """Handle incoming WhatsApp messages from Twilio"""
    try:
        contact_number = From.replace('whatsapp:', '')
        message_body = Body.strip()
        
        # Process the conversation
        response = ConversationManager.process_message(contact_number, message_body)
        
        # Check if this is a review completion
        if isinstance(response, dict) and "review_data" in response:
            # Save the review to database
            review_data = response["review_data"]
            new_review = Review(
                contact_number=review_data["contact_number"],
                user_name=review_data["user_name"],
                product_name=review_data["product_name"],
                product_review=review_data["product_review"]
            )
            db.add(new_review)
            db.commit()
            
            # Clear conversation state
            ConversationManager.clear_state(contact_number)
            
            # Send confirmation message
            whatsapp_service.send_message(contact_number, response["message"])
        else:
            # Send the conversation response
            whatsapp_service.send_message(contact_number, response)
        
        return {"status": "success"}
    
    except Exception as e:
        print(f"Error processing WhatsApp message: {e}")
        return {"status": "error", "message": str(e)}

@app.post("/webhook/whatsapp/status")
async def whatsapp_status_callback(
    MessageSid: str = Form(...),
    MessageStatus: str = Form(...),
    To: str = Form(None),
    From: str = Form(None)
):
    """Handle WhatsApp message status callbacks from Twilio"""
    try:
        print(f"Message Status Update: {MessageSid} - {MessageStatus}")
        if To:
            print(f"To: {To}")
        if From:
            print(f"From: {From}")
        
        # You can store status updates in database if needed
        # For now, just log them
        
        return {"status": "success"}
    except Exception as e:
        print(f"Error processing status callback: {e}")
        return {"status": "error", "message": str(e)}

@app.get("/api/stats")
async def get_stats(db: Session = Depends(get_db)):
    """Get basic statistics about reviews"""
    total_reviews = db.query(Review).count()
    unique_products = db.query(Review.product_name).distinct().count()
    unique_users = db.query(Review.contact_number).distinct().count()
    
    return {
        "total_reviews": total_reviews,
        "unique_products": unique_products,
        "unique_users": unique_users
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)