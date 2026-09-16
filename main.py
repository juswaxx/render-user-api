from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="User API")

class User(BaseModel):
    LastName: str
    FirstName: str
    Email: str
    Password: str

# Sample data - replace with your actual data source
users_db = [
    User(LastName="Doe", FirstName="John", Email="john.doe@example.com", Password="securepass123"),
    User(LastName="Smith", FirstName="Jane", Email="jane.smith@example.com", Password="mypassword456"),
    User(LastName="Johnson", FirstName="Bob", Email="bob.johnson@example.com", Password="bobsecure789"),
]

@app.get("/users")
def get_users():
    """Return the list of users."""
    return users_db