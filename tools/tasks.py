# tools/tasks.py
from typing import Optional, List, Dict, Any
from server import mcp, todoist
from pydantic import BaseModel, Field

# class TaskInput(BaseModel):
#     content: str = Field(description="The task content/title")
#     description: Optional[str] = Field(None, description="Task description")
#     project_id: Optional[str] = Field(None, description="Project ID")
#     labels: Optional[List[str]] = Field(None, description="List of label names")
#     due_string: Optional[str] = Field(None, description="Human-friendly due date (e.g., 'tomorrow', 'next Monday')")

@mcp.tool()
def get_tasks(
) -> Dict[str, Any]:
    """Get tasks from Todoist with optional filters"""
    try:
        tasks = todoist.get_tasks()
        return tasks
        
    except Exception as e:
        return {"success": False, "error": str(e)}

