"""
Linkfluence Database Seeder
Run: python seed_db.py

This script seeds the database with sample data for testing.
"""

from werkzeug.security import generate_password_hash
from datetime import datetime
from dotenv import load_dotenv

from database import get_db

load_dotenv()

def seed_data():
    print("🚀 Starting Database Seeding...")

    # Reuse the app's connection helper so the seeder and the API always agree
    # on which database they are pointed at (both resolve it from MONGO_URI).
    db = get_db()
    
    # Sample Users
    users = [
        {
            "name": "Demo Creator",
            "email": "creator@demo.com",
            "password": generate_password_hash("demo123"),
            "role": "creator",
            "bio": "I create amazing content for brands!",
            "category": "lifestyle",
            "followers_count": 50000,
            "created_at": datetime.utcnow()
        },
        {
            "name": "Demo Business",
            "email": "business@demo.com",
            "password": generate_password_hash("demo123"),
            "role": "business",
            "business_type": "retail",
            "description": "We connect brands with creators",
            "created_at": datetime.utcnow()
        }
    ]
    
    print("\n📂 Seeding users...", end=" ")
    for user in users:
        existing = db.users.find_one({"email": user["email"]})
        if not existing:
            db.users.insert_one(user)
    print(f"✅ Done ({len(users)} users)")
    
    # Get user IDs for campaigns
    creator = db.users.find_one({"email": "creator@demo.com"})
    business = db.users.find_one({"email": "business@demo.com"})
    
    if business:
        # Sample Campaign
        campaign = {
            "business_id": str(business["_id"]),
            "title": "Summer Campaign 2026",
            "description": "Looking for lifestyle creators to promote our summer collection",
            "budget": 5000,
            "status": "active",
            "created_at": datetime.utcnow()
        }
        
        print("📂 Seeding campaigns...", end=" ")
        existing = db.campaigns.find_one({"title": campaign["title"]})
        if not existing:
            db.campaigns.insert_one(campaign)
        print("✅ Done")
    
    print("\n✨ Seeding Complete!")
    print("\nTest Accounts:")
    print("  Creator: creator@demo.com / demo123")
    print("  Business: business@demo.com / demo123")

if __name__ == "__main__":
    seed_data()
