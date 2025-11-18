# Deployment Guide

## 🚀 **Quick Deployment**

### **Local Development**
```bash
# 1. Setup Backend
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your Twilio credentials
python demo_data.py  # Add sample data
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# 2. Setup Frontend (new terminal)
cd frontend
npm install
npm start
```

### **Production Deployment**

#### **Backend (Railway/Heroku)**
1. Create new project on Railway/Heroku
2. Connect GitHub repository
3. Set environment variables:
   - `DATABASE_URL`: Your PostgreSQL connection string
   - `TWILIO_ACCOUNT_SID`: Your Twilio Account SID
   - `TWILIO_AUTH_TOKEN`: Your Twilio Auth Token
4. Deploy automatically from main branch

#### **Frontend (Vercel/Netlify)**
1. Connect GitHub repository to Vercel/Netlify
2. Set build command: `npm run build`
3. Set publish directory: `build`
4. Set environment variable:
   - `REACT_APP_API_URL`: Your backend URL
5. Deploy automatically from main branch

### **WhatsApp Configuration**
1. Go to Twilio Console → WhatsApp Sandbox
2. Set webhook URL: `https://your-backend-url.com/webhook/whatsapp`
3. Method: POST
4. Save configuration
5. Test by sending message to Twilio WhatsApp number

## 🎯 **Live Demo URLs**
- **Frontend**: https://your-frontend-url.vercel.app
- **Backend API**: https://your-backend-url.railway.app
- **API Docs**: https://your-backend-url.railway.app/docs