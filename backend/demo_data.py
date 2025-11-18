"""
Demo script to add sample reviews to the database for testing
Run this after setting up the database to see the UI in action
"""

import os
import sys
from datetime import datetime, timedelta
from sqlalchemy.orm import Session

# Add the app directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))

from app.database import SessionLocal, create_tables
from app.models import Review

def add_demo_reviews():
    """Add sample reviews to the database"""
    create_tables()
    db = SessionLocal()
    
    try:
        # Check if reviews already exist
        existing_count = db.query(Review).count()
        if existing_count > 0:
            print(f"Database already has {existing_count} reviews. Skipping demo data.")
            return
        
        demo_reviews = [
            {
                "contact_number": "+1415555001",
                "user_name": "Aditi Sharma",
                "product_name": "iPhone 15",
                "product_review": "Amazing battery life, very satisfied. The camera quality is outstanding and the build feels premium.",
                "created_at": datetime.now() - timedelta(hours=2)
            },
            {
                "contact_number": "+1415555002",
                "user_name": "John Smith",
                "product_name": "MacBook Pro M3",
                "product_review": "Incredible performance for development work. The M3 chip handles everything I throw at it effortlessly.",
                "created_at": datetime.now() - timedelta(hours=5)
            },
            {
                "contact_number": "+1415555003",
                "user_name": "Maria Garcia",
                "product_name": "AirPods Pro",
                "product_review": "Best noise cancellation I've ever experienced. Perfect for commuting and work calls.",
                "created_at": datetime.now() - timedelta(hours=8)
            },
            {
                "contact_number": "+1415555004",
                "user_name": "David Chen",
                "product_name": "iPad Air",
                "product_review": "Great for digital art and note-taking. The Apple Pencil integration is seamless.",
                "created_at": datetime.now() - timedelta(days=1, hours=3)
            },
            {
                "contact_number": "+1415555005",
                "user_name": "Sarah Johnson",
                "product_name": "Apple Watch Series 9",
                "product_review": "Love the health tracking features. The battery lasts all day even with heavy usage.",
                "created_at": datetime.now() - timedelta(days=1, hours=7)
            },
            {
                "contact_number": "+1415555006",
                "user_name": "Ahmed Hassan",
                "product_name": "iPhone 15",
                "product_review": "Switched from Android and couldn't be happier. The ecosystem integration is fantastic.",
                "created_at": datetime.now() - timedelta(days=2, hours=1)
            },
            {
                "contact_number": "+1415555007",
                "user_name": "Emily Davis",
                "product_name": "Tesla Model 3",
                "product_review": "Revolutionary driving experience. The autopilot features are impressive and the charging network is extensive.",
                "created_at": datetime.now() - timedelta(days=2, hours=5)
            },
            {
                "contact_number": "+1415555008",
                "user_name": "Michael Brown",
                "product_name": "Sony WH-1000XM5",
                "product_review": "Superior sound quality and comfort. Perfect for long flights and work sessions.",
                "created_at": datetime.now() - timedelta(days=3, hours=2)
            }
        ]
        
        for review_data in demo_reviews:
            review = Review(**review_data)
            db.add(review)
        
        db.commit()
        print(f"Successfully added {len(demo_reviews)} demo reviews to the database!")
        
        # Print summary
        total_reviews = db.query(Review).count()
        unique_products = db.query(Review.product_name).distinct().count()
        unique_users = db.query(Review.contact_number).distinct().count()
        
        print(f"\nDatabase Summary:")
        print(f"Total Reviews: {total_reviews}")
        print(f"Unique Products: {unique_products}")
        print(f"Unique Users: {unique_users}")
        
    except Exception as e:
        print(f"Error adding demo data: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    add_demo_reviews()