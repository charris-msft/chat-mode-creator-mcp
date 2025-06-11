# 🛠️ Development Best Practices

## 🐍 Python Virtual Environment

### **Always Activate venv Before Python Commands**
```powershell
# ✅ CORRECT: Activate venv first
.\.venv\Scripts\Activate.ps1 && python script.py

# ❌ WRONG: Running without venv
python script.py
```

### **Why This Matters**
- Ensures consistent package versions
- Isolates project dependencies
- Prevents conflicts with system Python
- Matches production environment setup

### **Commands Template**
```powershell
# Testing
.\.venv\Scripts\Activate.ps1 && python test_server.py

# Running server
.\.venv\Scripts\Activate.ps1 && python mcp_chatmode_server.py

# Installing packages
.\.venv\Scripts\Activate.ps1 && pip install package-name

# Syntax checking
.\.venv\Scripts\Activate.ps1 && python -m py_compile script.py
```

## 📁 File Organization

### **Project Structure**
```
c:\git\mcp\gh_customs\
├── .venv/                          # Virtual environment (never commit)
├── mcp_chatmode_server.py          # Main server code
├── test_*.py                       # Test scripts
├── requirements.txt                # Python dependencies
├── chat_modes/                     # Source templates
│   ├── azure-bicep-development/
│   ├── lambda-to-functions-migration/
│   └── spec-driven-development/
└── .github/chatmodes/              # Generated output (VS Code)
```

## 📁 VS Code File Structure (Updated)

### **Correct File Locations** ✅
Following [VS Code Copilot Customization Documentation](https://code.visualstudio.com/docs/copilot/copilot-customization):

```
.github/
├── chatmodes/           # Our convention for chat mode files
│   └── mode-name/
│       └── mode-name.chatmode.md
└── prompts/             # VS Code official prompt location
    └── mode-name/
        ├── prompt1.prompt.md
        └── prompt2.prompt.md
```

### **VS Code Settings Required**
```json
{
  "chat.promptFiles": true,
  "chat.promptFilesLocations": [".github/prompts"]  // Default, auto-detected
}
```

### **Why This Structure**
- **📚 Standards Compliance**: Follows official VS Code documentation
- **🔍 Auto-Detection**: VS Code automatically finds prompts in `.github/prompts/`
- **🎯 Clear Separation**: Chat modes vs prompt files in different locations
- **⚡ Better Integration**: Native VS Code support for prompt files

## 🧪 Testing Best Practices

### **Always Test After Changes**
1. **Syntax Check**: `python -m py_compile mcp_chatmode_server.py`
2. **Functionality Test**: `python test_simplified_server.py`
3. **Integration Test**: Test in VS Code with MCP client

### **Test Coverage**
- ✅ Tool discovery (`list_tools`)
- ✅ Chat mode suggestion (`suggest_chat_mode`)
- ✅ Package creation (`create_chat_mode`)
- ✅ Error handling (invalid inputs)
- ✅ File structure validation

## 💻 Terminal Commands

### **PowerShell Best Practices**
```powershell
# Always use full paths for clarity
.\.venv\Scripts\Activate.ps1 && python c:\git\mcp\gh_customs\script.py

# Chain commands with && for error handling
.\.venv\Scripts\Activate.ps1 && python test.py && echo "Success!"

# Use proper escaping for paths with spaces
cd "c:\path with spaces" && .\.venv\Scripts\Activate.ps1
```

## 🔧 Code Quality

### **MCP Server Guidelines**
- Keep tool descriptions clear and concise
- Use proper JSON schema validation
- Handle errors gracefully with user-friendly messages
- Use emoji sparingly but effectively in responses
- Version bump when making breaking changes

### **Error Handling Template**
```python
try:
    # Main logic here
    result = do_something()
    return [types.TextContent(type="text", text=f"✅ Success: {result}")]
except Exception as e:
    return [types.TextContent(type="text", text=f"❌ Error: {str(e)}")]
```

## 📝 Documentation

### **Always Update When Changing**
- [ ] README.md - User-facing documentation
- [ ] Function docstrings - Developer documentation  
- [ ] Tool descriptions - MCP client documentation
- [ ] Test scripts - Validation documentation

## 🚀 Deployment

### **Pre-deployment Checklist**
- [ ] Virtual environment activated
- [ ] All tests passing
- [ ] Syntax errors resolved
- [ ] Version number updated
- [ ] Documentation updated
- [ ] File structure validated

## 🎯 User Experience

### **Simplified Interface Principles**
- Package deal approach: Complete solutions, not component pieces
- Clear value proposition: What does the user get?
- Minimal decision fatigue: Sensible defaults
- Actionable next steps: What to do after creation

---

## 🔄 Quick Reference

**Before ANY Python command:**
```powershell
.\.venv\Scripts\Activate.ps1 && [your-command]
```

**Common Commands:**
```powershell
# Test the server
.\.venv\Scripts\Activate.ps1 && python test_simplified_server.py

# Check syntax
.\.venv\Scripts\Activate.ps1 && python -m py_compile mcp_chatmode_server.py

# Run server directly
.\.venv\Scripts\Activate.ps1 && python mcp_chatmode_server.py
```

**Remember:** The venv activation ensures we're using the right Python environment with the correct dependencies! 🐍✨
