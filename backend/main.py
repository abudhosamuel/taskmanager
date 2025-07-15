from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.database import Base, engine
from backend.routes import auth, user, task, admin

# Initialize database
Base.metadata.create_all(bind=engine)

# Create app
app = FastAPI(
    title="Task Manager API",
    version="1.0.0",
    description="A task management system with authentication and role-based access."
)

# CORS settings
origins = [
    "http://localhost:5173",  # Vite frontend
    "http://127.0.0.1:5173",
    # Add more origins if deploying
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(user.router, prefix="/users", tags=["User Management"])
app.include_router(task.router, prefix="/tasks", tags=["Tasks"])
app.include_router(admin.router, prefix="", tags=["Admin"])  

