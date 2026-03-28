🚀 Django Job Board Suite
A powerful, full-featured Job Board application built with Django. This project serves as a comprehensive platform for employers to post jobs and for candidates to discover their next career move. It focuses on clean architecture, secure authentication, and a modern UI.


✨ Key Features
Custom User System: Specialized authentication supporting different user roles (Employers/Candidates).

Job Management: Full CRUD for job postings with categories and status tracking.

Smart Search & Filters: Advanced filtering for jobs by title, location, or status.

Professional Profiles: Integrated Profile Pictures and bios for users (Powered by Pillow).

Rich Content Support: Job descriptions with full formatting using CKEditor.

Responsive Dashboard: A sleek, mobile-friendly interface built with Bootstrap 5.


🛠️ Tech Stack
Backend: Python 3.x, Django.

Frontend: Bootstrap 5, HTML5, Custom CSS.

Database: SQLite (Development) / Ready for PostgreSQL.

Security: Environment variables via .env for sensitive keys.

⚙️ Installation & Setup
Clone the Repository:

Bash
git clone git@github.com:mostafa3ttar/Job-Board.git
cd job-board
Environment Setup:

Bash
python -m venv venv
source venv/Scripts/activate  # For Git Bash
pip install -r requirements.txt
Database Configuration:

Bash
python manage.py makemigrations
python manage.py migrate
Launch:

Bash
python manage.py runserver

Developed by Mostafa Ali