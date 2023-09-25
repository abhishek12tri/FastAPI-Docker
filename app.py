from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

"""Define server API Policy"""
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


"""Basic Test API"""
@app.get("/", tags=["Root"])
async def root():
    return {"message": "Hello World"}

"""Basic Test API"""
@app.get("/greet", tags=["Root"])
async def root(name: str):
    return {"message": f"Hi {name}"}