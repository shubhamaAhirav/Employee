# Step 1: Clone the Repository and Move into the Directory
git clone https://github.com/yourusername/EmployeeManagementAPI.git
cd EmployeeManagementAPI

# Step 2: Set Up a Virtual Environment and Activate It
python -m venv venv
# Activate the virtual environment
venv\Scripts\activate

# Step 3: Install Required Packages
pip install -r requirements.txt

# Step 4: Set Up the Environment Variables
# Create a .env file with the database URL
echo DATABASE_URL=sqlite:///./employees.db > .env

# Step 5: Configure Database in db.py
# Create db.py file with database connection details:
(
echo from sqlalchemy import create_engine
echo from sqlalchemy.ext.declarative import declarative_base
echo from sqlalchemy.orm import sessionmaker
echo import os
echo from dotenv import load_dotenv
echo.
echo load_dotenv()
echo DATABASE_URL = os.getenv("DATABASE_URL")
echo engine = create_engine(DATABASE_URL)
echo SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
echo Base = declarative_base()
) > db.py

# Step 6: Initialize Alembic for Database Migrations
alembic init alembic

# Step 7: Configure Alembic with Database URL
# Open alembic.ini and replace `sqlalchemy.url` with your database URL
(Get-Content alembic.ini).replace('; sqlalchemy.url = driver://user:pass@localhost/dbname', 'sqlalchemy.url = sqlite:///./employees.db') | Set-Content alembic.ini

# Step 8: Update Alembic env.py for Metadata Targeting
# In alembic/env.py, replace `target_metadata` configuration:
(Get-Content alembic/env.py).replace('target_metadata = None', 'from app.models import Base`nfrom db import DATABASE_URL`ntarget_metadata = Base.metadata') | Set-Content alembic/env.py

# Step 9: Create and Apply Initial Database Migration
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head

# Step 10: Run the FastAPI Application
uvicorn app.main:app --reload
