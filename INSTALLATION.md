# Chat Mode Creator MCP Server - Installation & Usage Guide

## 🚀 Installation Instructions

### 1. **Verify Server Setup**
Your MCP server is ready! The following files have been created:
- `mcp-config.json` - Configuration for MCP clients
- `run-mcp-server.bat` - Windows batch script to run the server
- `run-mcp-server.ps1` - PowerShell script to run the server

### 2. **Test the Server**
Test that the server runs correctly:
```powershell
cd c:\git\mcp\gh_customs
.\run-mcp-server.ps1
```

### 3. **Configure VS Code MCP Settings**

#### VS Code Insiders Settings Configuration
Add this to your VS Code User Settings (`settings.json`):
```json
{
  "mcp": {
    "inputs": [],
    "servers": {
      "create_chat_mode": {
        "command": "C:\\git\\mcp\\gh_customs\\.venv\\Scripts\\python.exe",
        "args": [
          "C:\\git\\mcp\\gh_customs\\mcp_chatmode_server.py"
        ],
        "cwd": "C:\\git\\mcp\\gh_customs",
        "env": {
          "PYTHONPATH": "C:\\git\\mcp\\gh_customs",
          "VIRTUAL_ENV": "C:\\git\\mcp\\gh_customs\\.venv"
        }
      }
    }
  },
  "chat.mcp.discovery.enabled": true
}
```

#### Alternative: Claude Desktop Configuration (if using Claude Desktop)
Add this to your Claude Desktop configuration file:
```json
{
  "mcpServers": {
    "chat-mode-creator": {
      "command": "C:\\git\\mcp\\gh_customs\\.venv\\Scripts\\python.exe",
      "args": ["C:\\git\\mcp\\gh_customs\\mcp_chatmode_server.py"],
      "cwd": "C:\\git\\mcp\\gh_customs",
      "env": {
        "PYTHONPATH": "C:\\git\\mcp\\gh_customs",
        "VIRTUAL_ENV": "C:\\git\\mcp\\gh_customs\\.venv"
      }
    }
  }
}
```

#### PowerShell Launcher Script Option
```json
{
  "mcp": {
    "servers": {
      "create_chat_mode": {
        "command": "powershell",
        "args": [
          "-ExecutionPolicy", "Bypass",
          "-File", "C:\\git\\mcp\\gh_customs\\run-mcp-server.ps1"
        ]
      }
    }
  }
}
```

### 4. **Using the MCP Server**

Once configured, you can use the server's tools:

#### Available Tools:
- **`suggest_chat_mode`** - Analyzes your query and suggests the most appropriate chat mode
- **`create_chat_mode`** - Creates VS Code chat mode files

#### Available Chat Modes:
- `spec_driven_development` - Spec-Driven Development workflow
- `lambda_to_functions_migration` - AWS Lambda to Azure Functions migration
- `azure_bicep_development` - Azure Bicep infrastructure development

## 🎯 Usage Examples

### Example 1: Get Chat Mode Suggestion
Ask Copilot: *"I want to migrate my AWS Lambda to Azure Functions"*

The MCP server will use the `suggest_chat_mode` tool to:
1. Analyze your query
2. Find the best matching chat mode (`lambda_to_functions_migration`)
3. Offer to create the specialized chat mode file

### Example 2: Direct Chat Mode Creation
```json
{
  "tool": "create_chat_mode",
  "arguments": {
    "mode_type": "lambda_to_functions_migration",
    "workspace_path": "."
  }
}
```

### Example 3: Query Analysis and Suggestion
```json
{
  "tool": "suggest_chat_mode",
  "arguments": {
    "user_query": "I need help with Azure Bicep infrastructure templates",
    "workspace_path": "."
  }
}
```

## 🤖 How Copilot Integration Works

1. **Ask natural questions** like:
   - "I want to migrate my AWS Lambda to Azure Functions"
   - "Help me with Azure Bicep infrastructure"
   - "I need assistance with specification-driven development"

2. **Copilot will use the MCP tools** to:
   - Analyze your query with `suggest_chat_mode`
   - Recommend the appropriate chat mode
   - Offer to create the chat mode file with `create_chat_mode`

3. **The server intelligently matches** your requests to available chat modes using keyword analysis

## 📁 File Structure
```
c:\git\mcp\gh_customs\
├── mcp_chatmode_server.py      # Main MCP server
├── chat_modes/                 # Source chat mode templates
│   ├── spec-driven-development.chatmode.md
│   ├── lambda-to-functions-migration.chatmode.md
│   └── azure-bicep-development.chatmode.md
├── mcp-config.json            # MCP configuration
├── run-mcp-server.bat         # Windows batch launcher
├── run-mcp-server.ps1         # PowerShell launcher
├── requirements.txt           # Python dependencies
└── .venv/                     # Python virtual environment
```

## 🔧 Troubleshooting

### MCP Server Won't Connect in VS Code
1. **Check VS Code MCP settings**:
   - Ensure `"chat.mcp.discovery.enabled": true` is set
   - Verify the server paths are correct with capital drive letters
   - Check that the virtual environment path exists

2. **Restart VS Code** after making settings changes

3. **Check the MCP server logs** in VS Code:
   - Open Command Palette (Ctrl+Shift+P)
   - Run "Developer: Show Logs"
   - Look for MCP server connection errors

### Server Won't Start
1. Ensure virtual environment is activated:
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

2. Check dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

3. Test manually:
   ```powershell
   python mcp_chatmode_server.py
   ```

### Copilot Not Using MCP Tools
1. **Make sure MCP discovery is enabled**: `"chat.mcp.discovery.enabled": true`
2. **Try explicit requests**: "Use the suggest_chat_mode tool to help me..."
3. **Check server status**: Look for "create_chat_mode" in the MCP server list
4. **Restart VS Code** if the server was recently added

### Environment Variables Issues
If you see import errors, ensure these environment variables are set in your MCP configuration:
```json
"env": {
  "PYTHONPATH": "C:\\git\\mcp\\gh_customs",
  "VIRTUAL_ENV": "C:\\git\\mcp\\gh_customs\\.venv"
}
```

## 🎉 Success!
Your **chat-mode-creator** MCP server is ready to use! 

The server dynamically loads chat modes from the `chat_modes/` folder, so you can easily add new modes by creating new `.chatmode.md` files in that directory.
