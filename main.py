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
    User(LastName="Anasco", FirstName="Joshua", Email="joshua.anasco@example.com", Password="tes123"),
    User(LastName="Snowman", FirstName="build", Email="build.snowman@example.com", Password="test456"),
    User(LastName="Dancer", FirstName="Bria", Email="bria.dancer@example.com", Password="test789"),
]

@app.get("/users")
def get_users():
    """Return the list of users."""
    return users_db