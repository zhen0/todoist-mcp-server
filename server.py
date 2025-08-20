# server.py
from fastmcp import FastMCP
from todoist_api_python.api import TodoistAPI
from config import config

# Create the MCP server instance
mcp = FastMCP("Todoist MCP Server")

# Initialize Todoist API client
todoist = TodoistAPI(config.TODOIST_API_KEY)



@mcp.tool()
def get_todoist_tasks():
    """Get tasks from Todoist with optional filters"""
    try:
        tasks = todoist.get_tasks()
        return tasks
        
    except Exception as e:
        return {"success": False, "error": str(e)}
    
@mcp.tool()
def update_todoist_task_by_id(task_id: str, content: str = None, priority: int = None, due_string: str = None, labels: list[str]= None):
    """Update a task from Todoist by ID"""
    try:
        task = todoist.update_task(task_id, content=content, priority=priority, due_string=due_string, labels=labels)
        return task
        
    except Exception as e:
        return {"success": False, "error": str(e)}

# Entry point
if __name__ == "__main__":
    mcp.run()