# config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configuration for Todoist MCP Server"""
    TODOIST_API_KEY = os.getenv("TODOIST_API_KEY")
    
    if not TODOIST_API_KEY:
        raise ValueError("TODOIST_API_KEY environment variable is required")

config = Config()