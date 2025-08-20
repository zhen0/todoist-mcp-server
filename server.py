# server.py
from fastmcp import FastMCP
from todoist_api_python.api import TodoistAPI
from config import config

# Create the MCP server instance
mcp = FastMCP("Todoist MCP Server")

# Initialize Todoist API client
todoist = TodoistAPI(config.TODOIST_API_KEY)

# Import all tools and resources after creating mcp and todoist instances
from tools import tasks, projects, labels, sections
# from resources import register_resources

# Register resources
# register_resources(mcp, todoist)

@mcp.tool()
def get_todoist_tasks():
    """Get tasks from Todoist with optional filters"""
    try:
        tasks = todoist.get_tasks()
        return tasks
        
    except Exception as e:
        return {"success": False, "error": str(e)}

# Entry point
if __name__ == "__main__":
    mcp.run()