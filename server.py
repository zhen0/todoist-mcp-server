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
    
# @mcp.tool()
# def update_todoist_task_by_id(task_id: str, content: str = None, priority: int = None, due_string: str = None, labels: list[str]= None):
#     """Update a task from Todoist by ID"""
#     try:
#         task = todoist.update_task(task_id, content=content, priority=priority, due_string=due_string, labels=labels)
#         return task
        
#     except Exception as e:
#         return {"success": False, "error": str(e)}

@mcp.tool()
def get_todoist_projects():
    """Get projects from Todoist"""
    try:
        projects = todoist.get_projects()
        return projects
        
    except Exception as e:
        return {"success": False, "error": str(e)}


@mcp.tool()
def create_todoist_task_by_id(content: str = None, priority: int = None, due_string: str = None, labels: list[str]= None, project_id: str = None):
    """Create a task in Todoist"""
    try:
        task = todoist.add_task(content=content, priority=priority, due_string=due_string, labels=labels, project_id=project_id)
        return task
        
    except Exception as e:
        return {"success": False, "error": str(e)}
    
# Entry point
if __name__ == "__main__":
    mcp.run()