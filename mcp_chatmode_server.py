# mcp_chatmode_server.py
import json
import os
import re
from typing import Any, Dict, List, Optional
from mcp.server import Server
from mcp.server.models import InitializationOptions
import mcp.server.stdio
from mcp import types

# Initialize the MCP server
server = Server("chat-mode-creator")

# Chat mode definitions directory
MODES_DIR = "chat_modes"

# Ensure the chat modes directory exists
os.makedirs(MODES_DIR, exist_ok=True)

def load_chat_modes() -> Dict[str, Dict[str, str]]:
    """Load all available chat modes from the chat_modes directory."""
    chat_modes = {}
    
    if not os.path.exists(MODES_DIR):
        return chat_modes
    
    for filename in os.listdir(MODES_DIR):
        if filename.endswith('.chatmode.md'):
            file_path = os.path.join(MODES_DIR, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Extract description from frontmatter
                description = extract_description_from_frontmatter(content)
                
                # Create mode key from filename (remove .chatmode.md and convert to snake_case)
                mode_key = filename.replace('.chatmode.md', '').replace('-', '_')
                
                chat_modes[mode_key] = {
                    'filename': filename,
                    'content': content,
                    'description': description
                }
            except Exception as e:
                print(f"Warning: Could not load chat mode file {filename}: {e}")
    
    return chat_modes

def extract_description_from_frontmatter(content: str) -> str:
    """Extract description from YAML frontmatter in chat mode file."""
    # Look for YAML frontmatter between --- markers
    frontmatter_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if frontmatter_match:
        frontmatter = frontmatter_match.group(1)
        # Look for description line
        desc_match = re.search(r'^description:\s*(.+)$', frontmatter, re.MULTILINE)
        if desc_match:
            return desc_match.group(1).strip()
    
    return "Custom chat mode for specialized development workflow"

def get_available_chat_modes() -> List[str]:
    """Get list of available chat mode keys."""
    return list(load_chat_modes().keys())

@server.list_tools()
async def handle_list_tools() -> List[types.Tool]:
    """List available tools for the MCP server."""
    available_modes = get_available_chat_modes()
    
    return [
        types.Tool(
            name="create_chat_mode",
            description="Create a custom VS Code chat mode file for specialized development workflows",
            inputSchema={
                "type": "object",
                "properties": {
                    "mode_type": {
                        "type": "string",
                        "enum": available_modes,
                        "description": f"The type of chat mode to create. Available modes: {', '.join(available_modes)}"
                    },
                    "output_path": {
                        "type": "string",
                        "description": "Optional custom path for the .chatmode.md file (defaults to .github/chatmodes/)",
                        "default": ""
                    },
                    "workspace_path": {
                        "type": "string",
                        "description": "Path to the workspace where the chat mode should be created",
                        "default": "."
                    }
                },
                "required": ["mode_type"]
            }
        )
    ]

@server.call_tool()
async def handle_call_tool(name: str, arguments: Dict[str, Any]) -> List[types.TextContent]:
    """Handle tool calls from the MCP client."""
    
    if name == "create_chat_mode":
        mode_type = arguments.get("mode_type")
        output_path = arguments.get("output_path", "")
        workspace_path = arguments.get("workspace_path", ".")
        
        # Load available chat modes
        chat_modes = load_chat_modes()
        
        if mode_type not in chat_modes:
            available_modes = list(chat_modes.keys())
            return [types.TextContent(
                type="text",
                text=f"Error: Unknown mode type '{mode_type}'. Available types: {', '.join(available_modes)}"
            )]
        
        try:
            # Get the template from loaded chat modes
            template = chat_modes[mode_type]
            filename = template["filename"]
            content = template["content"]
            description = template["description"]
            
            # Determine output directory
            if output_path:
                # Use custom path
                output_dir = os.path.join(workspace_path, output_path)
            else:
                # Use default VS Code chat modes directory
                output_dir = os.path.join(workspace_path, ".github", "chatmodes")
            
            # Ensure directory exists
            os.makedirs(output_dir, exist_ok=True)
            
            # Full file path
            file_path = os.path.join(output_dir, filename)
            
            # Write the chat mode file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return [types.TextContent(
                type="text",
                text=f"✅ Successfully created chat mode file: {file_path}\n\n"
                     f"📋 **Mode Type**: {mode_type.replace('_', ' ').title()}\n"
                     f"📁 **Location**: {file_path}\n"
                     f"📖 **Source**: {os.path.join(MODES_DIR, filename)}\n\n"
                     f"**Next Steps:**\n"
                     f"1. Open VS Code in your workspace\n"
                     f"2. Use Ctrl+Shift+P (Cmd+Shift+P on Mac) to open Command Palette\n"
                     f"3. Run 'Chat: Configure Chat Modes' to verify the mode is detected\n"
                     f"4. Select the new mode from the chat mode dropdown in the Chat view\n\n"
                     f"🎯 **Mode Description**: {description}"
            )]
            
        except Exception as e:
            return [types.TextContent(
                type="text",
                text=f"❌ Error creating chat mode file: {str(e)}"
            )]
    
    return [types.TextContent(
        type="text",
        text=f"Unknown tool: {name}"
    )]

async def main():
    # Run the server using stdin/stdout streams
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="chat-mode-creator",
                server_version="1.0.0",
                capabilities=server.get_capabilities(
                    notification_options=None,
                    experimental_capabilities={}
                )
            )
        )

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
