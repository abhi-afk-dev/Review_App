School Review Manager
A mini web app for submitting and viewing school reviews.

Technologies
Backend: Flask, Flask-SQLAlchemy
Database: MySQL
Frontend: HTML, Tailwind CSS

Setup
Clone/Create Project.

Install Python dependencies:
pip install -r requirements.txt

MySQL Database:
Ensure MySQL server is running.
Create a database (e.g., school_reviews_db).
The app will create the reviews table on first run.

Configure config.py:
Update MYSQL_USER, MYSQL_PASSWORD with your MySQL credentials.
Set a unique SECRET_KEY.

Run
Activate virtual environment.
Start app: python app.py
Access: http://127.0.0.1:5000/