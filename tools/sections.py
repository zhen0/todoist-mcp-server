# # tools/sections.py
# from typing import Optional, Dict, Any
# from server import mcp, todoist
# from pydantic import BaseModel, Field

# class SectionInput(BaseModel):
#     """Input model for creating/updating sections"""
#     name: str = Field(description="Section name")
#     project_id: str = Field(description="Project ID where the section belongs")
#     order: Optional[int] = Field(None, description="Section order within the project")

# @mcp.tool()
# def create_section(input_data: SectionInput) -> Dict[str, Any]:
#     """Create a new section in a project"""
#     try:
#         section = todoist.add_section(
#             name=input_data.name,
#             project_id=input_data.project_id,
#             order=input_data.order
#         )
#         return {
#             "success": True,
#             "section": {
#                 "id": section.id,
#                 "name": section.name,
#                 "project_id": section.project_id,
#                 "order": section.order
#             }
#         }
#     except Exception as e:
#         return {"success": False, "error": str(e)}

# @mcp.tool()
# def get_sections(project_id: Optional[str] = None) -> Dict[str, Any]:
#     """Get all sections, optionally filtered by project"""
#     try:
#         sections = todoist.get_sections(project_id=project_id)
#         return {
#             "success": True,
#             "count": len(sections),
#             "sections": [
#                 {
#                     "id": section.id,
#                     "name": section.name,
#                     "project_id": section.project_id,
#                     "order": section.order
#                 }
#                 for section in sections
#             ]
#         }
#     except Exception as e:
#         return {"success": False, "error": str(e)}

# @mcp.tool()
# def get_section(section_id: str) -> Dict[str, Any]:
#     """Get a specific section by ID"""
#     try:
#         section = todoist.get_section(section_id)
#         return {
#             "success": True,
#             "section": {
#                 "id": section.id,
#                 "name": section.name,
#                 "project_id": section.project_id,
#                 "order": section.order
#             }
#         }
#     except Exception as e:
#         return {"success": False, "error": str(e)}

# @mcp.tool()
# def update_section(section_id: str, name: str) -> Dict[str, Any]:
#     """Update a section name"""
#     try:
#         section = todoist.update_section(section_id, name=name)
#         return {
#             "success": True,
#             "section": {
#                 "id": section.id,
#                 "name": section.name,
#                 "project_id": section.project_id,
#                 "order": section.order
#             }
#         }
#     except Exception as e:
#         return {"success": False, "error": str(e)}

