@echo off
echo Setting up WhatsApp Review Collector Project...
echo.

echo Step 1: Setting up Backend...
cd backend

echo Creating virtual environment...
python -m venv venv
call venv\Scripts\activate.bat

echo Installing Python dependencies...
pip install -r requirements.txt

echo.
echo Step 2: Setting up Frontend...
cd ..\frontend

echo Installing Node.js dependencies...
npm install

echo.
echo Step 3: Environment Setup...
cd ..\backend
if not exist .env (
    copy .env.example .env
    echo Created .env file. Please update it with your database and Twilio credentials.
)

echo.
echo Setup complete!
echo.
echo Next steps:
echo 1. Update backend/.env with your database and Twilio credentials
echo 2. Create PostgreSQL database: whatsapp_reviews
echo 3. Run start_backend.bat to start the backend server
echo 4. Run start_frontend.bat to start the frontend server
echo.
pause