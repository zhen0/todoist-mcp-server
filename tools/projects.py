# # tools/projects.py
# from typing import Optional, Dict, Any
# from server import mcp, todoist
# from pydantic import BaseModel, Field

# class ProjectInput(BaseModel):
#     """Input model for creating/updating projects"""
#     name: str = Field(description="Project name")
#     color: Optional[str] = Field(None, description="Color name (e.g., 'red', 'blue')")
#     parent_id: Optional[str] = Field(None, description="Parent project ID")
#     is_favorite: Optional[bool] = Field(False, description="Mark as favorite")
#     view_style: Optional[str] = Field("list", description="View style: 'list' or 'board'")

# @mcp.tool()
# def create_project(input_data: ProjectInput) -> Dict[str, Any]:
#     """Create a new project"""
#     try:
#         project = todoist.add_project(
#             name=input_data.name,
#             color=input_data.color,
#             parent_id=input_data.parent_id,
#             is_favorite=input_data.is_favorite,
#             view_style=input_data.view_style
#         )
#         return {
#             "success": True,
#             "project": {
#                 "id": project.id,
#                 "name": project.name,
#                 "color": project.color,
#                 "parent_id": project.parent_id,
#                 "order": project.order,
#                 "comment_count": project.comment_count,
#                 "is_favorite": project.is_favorite,
#                 "url": project.url,
#                 "view_style": project.view_style
#             }
#         }
#     except Exception as e:
#         return {"success": False, "error": str(e)}

# @mcp.tool()
# def get_projects() -> Dict[str, Any]:
#     """Get all projects"""
#     try:
#         projects = todoist.get_projects()
#         return {
#             "success": True,
#             "count": len(projects),
#             "projects": [
#                 {
#                     "id": project.id,
#                     "name": project.name,
#                     "color": project.color,
#                     "parent_id": project.parent_id,
#                     "order": project.order,
#                     "comment_count": project.comment_count,
#                     "is_favorite": project.is_favorite,
#                     "is_inbox_project": project.is_inbox_project,
#                     "is_team_inbox": project.is_team_inbox,
#                     "view_style": project.view_style,
#                     "url": project.url
#                 }
#                 for project in projects
#             ]
#         }
#     except Exception as e:
#         return {"success": False, "error": str(e)}

# @mcp.tool()
# def get_project(project_id: str) -> Dict[str, Any]:
#     """Get a specific project by ID"""
#     try:
#         project = todoist.get_project(project_id)
#         return {
#             "success": True,
#             "project": {
#                 "id": project.id,
#                 "name": project.name,
#                 "color": project.color,
#                 "parent_id": project.parent_id,
#                 "order": project.order,
#                 "comment_count": project.comment_count,
#                 "is_favorite": project.is_favorite,
#                 "is_inbox_project": project.is_inbox_project,
#                 "is_team_inbox": project.is_team_inbox,
#                 "view_style": project.view_style,
#                 "url": project.url
#             }
#         }
#     except Exception as e:
#         return {"success": False, "error": str(e)}

# @mcp.tool()
# def update_project(project_id: str, input_data: ProjectInput) -> Dict[str, Any]:
#     """Update an existing project"""
#     try:
#         update_kwargs = {}
#         if input_data.name:
#             update_kwargs["name"] = input_data.name
#         if input_data.color is not None:
#             update_kwargs["color"] = input_data.color
#         if input_data.is_favorite is not None:
#             update_kwargs["is_favorite"] = input_data.is_favorite
#         if input_data.view_style is not None:
#             update_kwargs["view_style"] = input_data.view_style
            
#         project = todoist.update_project(project_id, **update_kwargs)
        
#         return {
#             "success": True,
#             "project": {
#                 "id": project.id,
#                 "name": project.name,
#                 "color": project.color,
#                 "is_favorite": project.is_favorite,
#                 "view_style": project.view_style
#             }
#         }
#     except Exception as e:
#         return {"success": False, "error": str(e)}
