# # resources.py
# from typing import Dict, Any, List
# from datetime import datetime, timedelta

# def register_resources(mcp, todoist):
#     """Register all resources with the MCP server"""
    
#     @mcp.resource("todoist://tasks/all")
#     def get_all_tasks() -> Dict[str, Any]:
#         """Get all tasks with basic information"""
#         try:
#             tasks = todoist.get_tasks()
#             return tasks
    
            
#         except Exception as e:
#             return {"error": str(e), "error_type": type(e).__name__}