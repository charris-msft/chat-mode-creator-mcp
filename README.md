# 🎯 Chat Mode Creator MCP Server

An advanced MCP (Model Context Protocol) server that creates custom VS Code chat modes AND custom prompts for specialized development workflows.

## ✨ Key Features

🎯 **Integrated Workflow**: Chat modes come with related custom prompts  
📁 **VS Code Compatible**: Follows official VS Code chat mode and prompt specifications  
🚀 **Ready-to-Use**: Pre-built templates for common development scenarios  
⚡ **Intelligent Matching**: Analyzes queries to suggest appropriate modes  

## 🛠️ Available Chat Modes & Custom Prompts

### 🔄 **Lambda to Azure Functions Migration**
**Chat Mode**: Comprehensive migration guidance from AWS Lambda to Azure Functions
- Runtime and service mapping assistance
- Code conversion patterns and best practices  
- Infrastructure migration support

**Custom Prompts**:
- `/evaluate` - Assess migration readiness and complexity
- `/validate` - Verify migrated functions work correctly

### 🏗️ **Azure Bicep Development**
**Chat Mode**: Expert assistance for Azure Bicep infrastructure as code
- Azure Well-Architected Framework integration
- Advanced Bicep patterns and techniques
- Security, monitoring, and deployment best practices

**Custom Prompts**:
- `/review` - Code review and best practices validation
- `/deploy` - Safe deployment procedures and checks

### 📋 **Spec-Driven Development**
**Chat Mode**: Transform specifications into code through systematic process
- Treats specifications as the primary development artifact
- Follows systematic 5-phase SDD workflow
- Includes consistency validation and checklist integration

**Custom Prompts**:
- `/validate_spec` - Validate specifications for completeness
- `/generate_tests` - Generate comprehensive test suites

## 🚀 Quick Installation

### 1. **Install Dependencies**
```bash
# Create and activate virtual environment (.venv)
python -m venv .venv
.\.venv\Scripts\Activate.ps1  # Windows PowerShell
# .venv/bin/activate          # Linux/Mac

# Install required packages
pip install -r requirements.txt
```

### 2. **Test Server**
```bash
# Test that the server runs correctly
python mcp_chatmode_server.py
```

### 3. **Configure VS Code**
Add to your VS Code User Settings (`settings.json`):
```json
{
  "mcp": {
    "servers": {
      "chat-mode-creator": {
        "command": "C:\\path\\to\\your\\.venv\\Scripts\\python.exe",
        "args": ["C:\\path\\to\\your\\mcp_chatmode_server.py"],
        "cwd": "C:\\path\\to\\your\\workspace",
        "env": {
          "PYTHONPATH": "C:\\path\\to\\your\\workspace",
          "VIRTUAL_ENV": "C:\\path\\to\\your\\.venv"
        }
      }
    }
  },
  "chat.mcp.discovery.enabled": true,
  "chat.promptFiles": true
}
```

## 🛠️ Available Tools

### **`create_chat_mode`** ⭐ Main Tool
Creates chat modes with integrated custom prompts
- **Parameters:**
  - `mode_type` (required): `"spec_driven_development"`, `"lambda_to_functions_migration"`, or `"azure_bicep_development"`
  - `workspace_path` (optional): Workspace path (defaults to current directory)

### **`suggest_chat_mode`** 🎯 Smart Assistant  
Analyzes your query and suggests the most appropriate chat mode
- **Parameters:**
  - `user_query` (required): Description of what you want to accomplish
  - `workspace_path` (optional): Workspace path (defaults to current directory)

### **`create_custom_prompt`** 🎨 Advanced
Create individual custom prompts for specific tasks
- **Parameters:**
  - `mode_type` (required): The chat mode this prompt belongs to
  - `prompt_name` (required): Name for the custom prompt
  - `custom_description` (optional): Custom description for the prompt

### **`list_mode_prompts`** 📋 Reference
List all available custom prompts for a specific chat mode
- **Parameters:**
  - `mode_type` (required): The chat mode to list prompts for

## 📁 File Structure

Files are created following VS Code standards:

```
.github/
├── chatmodes/
│   ├── azure-bicep-development.chatmode.md
│   ├── lambda-to-functions-migration.chatmode.md
│   └── spec-driven-development.chatmode.md
└── prompts/
    ├── review.prompt.md      # Azure Bicep prompts
    ├── deploy.prompt.md
    ├── evaluate.prompt.md    # Lambda migration prompts  
    ├── validate.prompt.md
    ├── validate_spec.prompt.md   # Spec-driven prompts
    └── generate_tests.prompt.md
```

## 💡 Usage Examples

### Natural Language Interaction
Just ask Copilot naturally:
- *"I want to migrate my AWS Lambda to Azure Functions"*
- *"Help me with Azure Bicep infrastructure templates"*  
- *"I need assistance with specification-driven development"*

Copilot will automatically use the MCP tools to suggest and create appropriate chat modes.

### Direct Tool Usage
```python
# Create Azure Bicep mode with prompts
create_chat_mode(
    mode_type="azure_bicep_development",
    workspace_path="/path/to/your/project"
)

# Get intelligent suggestions
suggest_chat_mode(
    user_query="I need help migrating serverless functions",
    workspace_path="/path/to/your/project"
)

# Create a custom prompt
create_custom_prompt(
    mode_type="azure_bicep_development",
    prompt_name="security_scan",
    custom_description="Scan templates for security issues"
)
```

## 🎯 Using in VS Code

### 1. **Chat Modes**
- Open VS Code Chat view
- Select your custom mode from the dropdown
- Get specialized assistance for that workflow

### 2. **Custom Prompts**  
- In chat, type `/prompt_name` (e.g., `/review`, `/evaluate`)
- Prompts automatically include mode-specific context
- Combine with file references for targeted help

### 3. **Integration Example**
```
Chat Mode: Azure Bicep Development
Prompt: /review
Context: main.bicep file
Result: Comprehensive security and best practices review
```

## 🔧 Troubleshooting

### MCP Server Won't Connect in VS Code
1. **Check VS Code MCP settings**:
   - Ensure `"chat.mcp.discovery.enabled": true` is set
   - Verify the server paths are correct with capital drive letters
   - Check that the virtual environment path exists

2. **Restart VS Code** after making settings changes

3. **Check the MCP server logs** in VS Code:
   - Open Command Palette (`Ctrl+Shift+P`)
   - Run "Developer: Show Logs"
   - Look for MCP server connection errors

### Server Won't Start
1. **Ensure virtual environment is activated**:
   ```powershell
   .\.venv\Scripts\Activate.ps1  # Windows
   source .venv/bin/activate     # Linux/Mac
   ```

2. **Check dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Test manually**:
   ```bash
   python mcp_chatmode_server.py
   ```

### Copilot Not Using MCP Tools
1. **Make sure MCP discovery is enabled**: `"chat.mcp.discovery.enabled": true`
2. **Try explicit requests**: "Use the suggest_chat_mode tool to help me..."
3. **Check server status**: Look for "chat-mode-creator" in the MCP server list
4. **Restart VS Code** if the server was recently added

### Environment Variables Issues
If you see import errors, ensure these environment variables are set in your MCP configuration:
```json
"env": {
  "PYTHONPATH": "/path/to/your/workspace",
  "VIRTUAL_ENV": "/path/to/your/.venv"
}
```

## 🎨 Advanced Configuration

### Alternative Launcher Scripts
You can also use PowerShell scripts for easier management:

**run-mcp-server.ps1**:
```powershell
cd "C:\path\to\your\workspace"
.\.venv\Scripts\Activate.ps1
python mcp_chatmode_server.py
```

**VS Code Configuration with PowerShell**:
```json
{
  "mcp": {
    "servers": {
      "chat-mode-creator": {
        "command": "powershell",
        "args": [
          "-ExecutionPolicy", "Bypass",
          "-File", "C:\\path\\to\\run-mcp-server.ps1"
        ]
      }
    }
  }
}
```

### Claude Desktop Integration
For Claude Desktop users, add to your configuration:
```json
{
  "mcpServers": {
    "chat-mode-creator": {
      "command": "/path/to/your/.venv/bin/python",
      "args": ["/path/to/your/mcp_chatmode_server.py"],
      "cwd": "/path/to/your/workspace"
    }
  }
}
```

## 🎯 Custom Prompt Examples

### Lambda Migration Evaluation (`/evaluate`)
Analyzes AWS Lambda functions for migration readiness:
- Runtime compatibility assessment
- Infrastructure dependency mapping  
- Performance characteristic evaluation
- Migration complexity scoring

### Bicep Template Review (`/review`)
Comprehensive Bicep template analysis:
- Security best practices validation
- Azure Well-Architected Framework compliance
- Cost optimization recommendations
- Code quality assessment

### Specification Validation (`/validate_spec`)
Ensures specifications are ready for code generation:
- Completeness checking
- Consistency analysis
- Implementation readiness validation
- Gap identification and resolution

## 🤝 Contributing

Extend this MCP server with additional chat modes:

1. **Add new templates** to `chat_modes/` directory
2. **Create new prompt files** for the mode
3. **Update** `AVAILABLE_PROMPT_TEMPLATES` in server code
4. **Test** with the provided test scripts
5. **Submit PR** with examples and documentation

### Template Structure
```markdown
---
description: Brief description of the chat mode
tools: ['relevant', 'tools', 'list']
---

# Chat Mode Name

## Purpose
What this mode helps with...

## Usage Guidelines  
How to use this mode effectively...

## Related Prompts
- `/prompt1` - Description
- `/prompt2` - Description
```

## 📊 Project Structure
```
chat-mode-creator/
├── mcp_chatmode_server.py          # Main MCP server
├── chat_modes/                     # Source templates
│   ├── azure-bicep-development.chatmode.md
│   ├── lambda-to-functions-migration.chatmode.md
│   ├── spec-driven-development.chatmode.md
│   └── */                          # Mode-specific prompts
├── requirements.txt                # Python dependencies
├── example_usage.py                # Usage examples
├── test_server.py                  # Test scripts
└── .venv/                          # Virtual environment
```

## 📄 License

MIT License - See LICENSE file for details

---

🎉 **Ready to supercharge your VS Code chat experience with specialized modes and custom prompts!**

*This MCP server intelligently creates organized chat modes and prompts that follow VS Code's official specifications, making your development workflow more efficient and context-aware.*
