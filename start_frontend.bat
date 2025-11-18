@echo off
echo Starting WhatsApp Review Collector Frontend...
echo.

cd frontend

echo Installing dependencies...
if not exist node_modules (
    npm install
)

echo.
echo Starting React development server...
echo Frontend will be available at: http://localhost:3000
echo.

npm start