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

# Step 5: Initialize Alembic for Database Migrations
alembic init alembic

# Step 6: Create and Apply Initial Database Migration
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head

# Step 7: Run the FastAPI Application
uvicorn app.main:app --reload
