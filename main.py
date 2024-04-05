import uvicorn
from fastapi import FastAPI
import random

# Create an instance of FastAPI
app = FastAPI()

# Define your routes
@app.get("/")
async def read_root():
    data=[]
    for i in range(10):
        data.append(f"random {random.randint(100, 999)}")
    return {"message": data}


if __name__ == "__main__":
    uvicorn.run(app, port=8000)
 