# # tools/labels.py
# from typing import Optional, Dict, Any
# from server import mcp, todoist
# from pydantic import BaseModel, Field

# class LabelInput(BaseModel):
#     """Input model for creating/updating labels"""
#     name: str = Field(description="Label name")
#     color: Optional[str] = Field(None, description="Color name")
#     order: Optional[int] = Field(None, description="Label order")
#     is_favorite: Optional[bool] = Field(False, description="Mark as favorite")

# @mcp.tool()
# def create_label(input_data: LabelInput) -> Dict[str, Any]:
#     """Create a new label"""
#     try:
#         label = todoist.add_label(
#             name=input_data.name,
#             color=input_data.color,
#             order=input_data.order,
#             is_favorite=input_data.is_favorite
#         )
#         return {
#             "success": True,
#             "label": {
#                 "id": label.id,
#                 "name": label.name,
#                 "color": label.color,
#                 "order": label.order,
#                 "is_favorite": label.is_favorite
#             }
#         }
#     except Exception as e:
#         return {"success": False, "error": str(e)}

# @mcp.tool()
# def get_labels() -> Dict[str, Any]:
#     """Get all labels"""
#     try:
#         labels = todoist.get_labels()
#         return {
#             "success": True,
#             "count": len(labels),
#             "labels": [
#                 {
#                     "id": label.id,
#                     "name": label.name,
#                     "color": label.color,
#                     "order": label.order,
#                     "is_favorite": label.is_favorite
#                 }
#                 for label in labels
#             ]
#         }
#     except Exception as e:
#         return {"success": False, "error": str(e)}

# @mcp.tool()
# def get_label(label_id: str) -> Dict[str, Any]:
#     """Get a specific label by ID"""
#     try:
#         label = todoist.get_label(label_id)
#         return {
#             "success": True,
#             "label": {
#                 "id": label.id,
#                 "name": label.name,
#                 "color": label.color,
#                 "order": label.order,
#                 "is_favorite": label.is_favorite
#             }
#         }
#     except Exception as e:
#         return {"success": False, "error": str(e)}

# @mcp.tool()
# def update_label(label_id: str, input_data: LabelInput) -> Dict[str, Any]:
#     """Update an existing label"""
#     try:
#         update_kwargs = {}
#         if input_data.name:
#             update_kwargs["name"] = input_data.name
#         if input_data.color is not None:
#             update_kwargs["color"] = input_data.color
#         if input_data.order is not None:
#             update_kwargs["order"] = input_data.order
#         if input_data.is_favorite is not None:
#             update_kwargs["is_favorite"] = input_data.is_favorite
            
#         label = todoist.update_label(label_id, **update_kwargs)
        
#         return {
#             "success": True,
#             "label": {
#                 "id": label.id,
#                 "name": label.name,
#                 "color": label.color,
#                 "order": label.order,
#                 "is_favorite": label.is_favorite
#             }
#         }
#     except Exception as e:
#         return {"success": False, "error": str(e)}

# @mcp.tool()
# def delete_label(label_id: str) -> Dict[str, Any]:
#     """Delete a label"""
#     try:
#         result = todoist.delete_label(label_id)
#         return {"success": True, "message": f"Label {label_id} deleted"}
#     except Exception as e:
#         return {"success": False, "error": str(e)}