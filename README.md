# Chat Mode Creator MCP Server

An MCP (Model Context Protocol) server that helps create custom VS Code chat modes for specialized development workflows.

## Features

This MCP server provides a tool to create three specialized chat modes:

### 🎯 Spec-Driven Development
- Transforms specifications into code through AI
- Treats specifications as the primary development artifact
- Follows systematic SDD workflow phases
- Includes consistency validation and checklist integration

### 🔄 Lambda to Azure Functions Migration  
- Systematic migration guidance from AWS Lambda to Azure Functions
- Runtime and service mapping assistance
- Code conversion patterns and best practices
- Infrastructure migration support

### 🏗️ Azure Bicep Development
- Expert assistance for Azure Bicep infrastructure as code
- Azure Well-Architected Framework integration
- Advanced Bicep patterns and techniques
- Security, monitoring, and deployment best practices

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the MCP server:
```bash
python mcp_chatmode_server.py
```

## Usage

### Available Tool

**`create_chat_mode`**
- Creates a custom VS Code chat mode file
- **Parameters:**
  - `mode_type` (required): One of `"spec_driven_development"`, `"lambda_to_functions"`, or `"azure_bicep_development"`
  - `output_path` (optional): Custom path for the .chatmode.md file
  - `workspace_path` (optional): Workspace path (defaults to current directory)

### Example Usage

```python
# Create a Spec-Driven Development chat mode
create_chat_mode(
    mode_type="spec_driven_development",
    workspace_path="/path/to/your/project"
)

# Create Azure Bicep Development mode with custom path
create_chat_mode(
    mode_type="azure_bicep_development", 
    output_path="custom/chatmodes/",
    workspace_path="/path/to/your/project"
)
```

## Chat Mode Files Structure

Each chat mode file follows the VS Code chat mode format:

```markdown
---
description: Brief description of the chat mode
tools: ['list', 'of', 'available', 'tools']
---

# Chat Mode Instructions

Detailed instructions for the AI when operating in this mode...
```

## Integration with VS Code

1. After creating a chat mode file, open VS Code in your workspace
2. Use `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac) to open Command Palette  
3. Run "Chat: Configure Chat Modes" to verify the mode is detected
4. Select the new mode from the chat mode dropdown in the Chat view

## File Locations

- **Default Location**: `.github/chatmodes/` (VS Code standard)
- **Reference Copies**: `chat_modes/` directory in this project
- **Custom Locations**: Specify with `output_path` parameter

## Chat Mode Descriptions

### Spec-Driven Development Mode
Focuses on transforming specifications into code through a systematic 5-phase process: Idea Analysis → PRD Creation → Implementation Planning → Consistency Validation → Code Generation.

### Lambda to Functions Migration Mode  
Provides comprehensive migration assistance from AWS Lambda to Azure Functions, including runtime mapping, code conversion patterns, infrastructure migration, and testing strategies.

### Azure Bicep Development Mode
Expert assistance for Azure Bicep infrastructure as code development, incorporating Azure Well-Architected Framework principles, advanced patterns, and production-ready templates.

## Contributing

Feel free to extend this MCP server with additional chat modes by:
1. Adding new templates to `CHAT_MODE_TEMPLATES`
2. Updating the enum in the tool schema
3. Creating comprehensive mode instructions

## License

MIT License - See LICENSE file for details
