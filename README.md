# Todoist MCP Server

An MCP (Model Context Protocol) server for interacting with Todoist using FastMCP 2.

## Features

### Tools
- **Task Management**: Read tasks

## Setup

1. Install dependencies:
```bash
uv add fastmcp todoist-api-python python-dotenv pydantic
```

## Run
run --with fastmcp --with todoist-api-python fastmcp todoist-mcp-server/server.py
