import sys
import os
sys.path.append(os.path.dirname(__file__))

from database import engine
from models import Base

Base.metadata.create_all(bind=engine)
