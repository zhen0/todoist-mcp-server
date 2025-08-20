# Todoist MCP Server

An MCP (Model Context Protocol) server for interacting with Todoist using FastMCP 2.

## Features

### Tools
- **Task Management**: Create, update, complete, reopen, and delete tasks
- **Quick Add**: Add tasks using natural language
- **Project Management**: Create, update, and delete projects
- **Label Management**: Create, update, and delete labels
- **Section Management**: Create, update, and delete sections within projects

### Resources
- `todoist://tasks/today` - Get all tasks due today
- `todoist://tasks/overdue` - Get all overdue tasks
- `todoist://tasks/upcoming` - Get tasks for the next 7 days
- `todoist://stats` - Get statistics summary
- `todoist://projects/{project_id}/summary` - Get project-specific summary

## Setup

1. Install dependencies:
```bash
uv add fastmcp todoist-api-python python-dotenv pydantic