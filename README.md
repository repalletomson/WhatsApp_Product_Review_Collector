# WhatsApp Product Review Collector

A full-stack application that collects product reviews via WhatsApp and displays them in a modern React dashboard.

## 🎯 **Assignment Overview**

This project implements a complete WhatsApp-based product review collection system as specified in the requirements:

1. ✅ **WhatsApp Integration**: Users submit reviews via WhatsApp conversation flow
2. ✅ **Backend API**: FastAPI with PostgreSQL/SQLite database storage
3. ✅ **Frontend Dashboard**: React application with professional UI design
4. ✅ **Real-time Updates**: Reviews appear instantly on the dashboard
5. ✅ **Modern Design**: Professional color palette and responsive layout

## 🛠 **Tech Stack**
- **Backend**: FastAPI (Python)
- **Frontend**: React with modern UI components
- **Database**: SQLite (easily configurable to PostgreSQL)
- **WhatsApp Integration**: Twilio WhatsApp Sandbox
- **Styling**: Custom CSS with professional color palette

## Features
- WhatsApp conversation flow for collecting reviews
- Automated review storage in PostgreSQL
- Modern React dashboard with real-time review display
- Professional UI with carefully selected color palette
- Responsive design

## Project Structure
```
whatsapp-review-collector/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── database.py
│   │   ├── whatsapp.py
│   │   └── conversation.py
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── services/
│   │   ├── styles/
│   │   ├── App.js
│   │   └── index.js
│   ├── public/
│   └── package.json
└── README.md
```

## Setup Instructions

### Prerequisites
- Python 3.8+
- Node.js 16+
- PostgreSQL
- Twilio Account (free tier)

### Backend Setup

1. **Clone and navigate to backend**
```bash
cd backend
```

2. **Create virtual environment**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Setup PostgreSQL Database**
```sql
CREATE DATABASE whatsapp_reviews;
```

5. **Environment Configuration**
```bash
cp .env.example .env
```
Edit `.env` with your database and Twilio credentials:
```
DATABASE_URL=postgresql://username:password@localhost/whatsapp_reviews
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
```

6. **Run the backend**
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend Setup

1. **Navigate to frontend**
```bash
cd frontend
```

2. **Install dependencies**
```bash
npm install
```

3. **Start development server**
```bash
npm start
```

### Twilio WhatsApp Setup

1. **Access Twilio Console**
   - Go to Twilio Console → Messaging → Try it out → Send a WhatsApp message

2. **Configure Webhook**
   - Set webhook URL to: `https://your-domain.com/webhook/whatsapp`
   - For local development, use ngrok: `ngrok http 8000`

3. **Test the Integration**
   - Send "Hi" to your Twilio WhatsApp number
   - Follow the conversation flow

## API Endpoints

### GET /api/reviews
Returns all stored reviews
```json
[
  {
    "id": 1,
    "contact_number": "+1415XXXXXXX",
    "user_name": "Aditi",
    "product_name": "iPhone 15",
    "product_review": "Amazing battery life, very satisfied.",
    "created_at": "2025-11-17T12:34:56Z"
  }
]
```

### POST /webhook/whatsapp
Receives WhatsApp messages from Twilio

## Conversation Flow

1. User sends any message to start
2. Bot asks: "Which product is this review for?"
3. Bot asks: "What's your name?"
4. Bot asks: "Please send your review for [product]."
5. Bot confirms: "Thanks [name] -- your review for [product] has been recorded."

## Color Palette

The UI uses a professional, modern color scheme:
- **Primary**: Deep Blue (#1e40af) - Trust and reliability
- **Secondary**: Emerald Green (#10b981) - Success and growth
- **Accent**: Amber (#f59e0b) - Energy and attention
- **Background**: Clean whites and light grays
- **Text**: Dark grays for excellent readability

## Development Notes

- Backend runs on port 8000
- Frontend runs on port 3000
- Database migrations handled automatically
- CORS enabled for development
- Error handling and validation included

## Deployment

For production deployment:
1. Set up PostgreSQL database
2. Configure environment variables
3. Deploy backend (Railway, Heroku, etc.)
4. Deploy frontend (Vercel, Netlify, etc.)
5. Update Twilio webhook URL

## License

MIT License