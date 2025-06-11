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
    """Load all available chat modes from the chat_modes directory and subdirectories."""
    chat_modes = {}
    
    if not os.path.exists(MODES_DIR):
        return chat_modes
    
    # Check both root directory and subdirectories
    for root, dirs, files in os.walk(MODES_DIR):
        for filename in files:
            if filename.endswith('.chatmode.md'):
                file_path = os.path.join(root, filename)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Extract description from frontmatter
                    description = extract_description_from_frontmatter(content)
                    
                    # Create mode key from filename (remove .chatmode.md and convert to snake_case)
                    mode_key = filename.replace('.chatmode.md', '').replace('-', '_')
                    
                    # Get relative path for subfolder info
                    rel_path = os.path.relpath(file_path, MODES_DIR)
                    subfolder = os.path.dirname(rel_path) if os.path.dirname(rel_path) != '.' else None
                    
                    chat_modes[mode_key] = {
                        'filename': filename,
                        'content': content,
                        'description': description,
                        'subfolder': subfolder,
                        'full_path': file_path
                    }
                except Exception as e:
                    print(f"Warning: Could not load chat mode file {filename}: {e}")
    
    return chat_modes

def load_custom_prompts(mode_name: str) -> Dict[str, Dict[str, str]]:
    """Load custom prompts for a specific mode from its subfolder."""
    prompts = {}
    mode_folder = os.path.join(MODES_DIR, mode_name.replace('_', '-'))
    
    if not os.path.exists(mode_folder):
        return prompts
    
    for filename in os.listdir(mode_folder):
        if filename.endswith('.prompt.md'):
            file_path = os.path.join(mode_folder, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Extract description from frontmatter
                description = extract_description_from_frontmatter(content)
                
                # Create prompt key from filename (remove .prompt.md and convert to snake_case)
                prompt_key = filename.replace('.prompt.md', '').replace('-', '_')
                
                prompts[prompt_key] = {
                    'filename': filename,
                    'content': content,
                    'description': description,
                    'full_path': file_path
                }
            except Exception as e:
                print(f"Warning: Could not load custom prompt file {filename}: {e}")
    
    return prompts

def extract_description_from_frontmatter(content: str) -> str:
    """Extract description from YAML frontmatter in files."""
    # Look for YAML frontmatter between --- markers
    frontmatter_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if frontmatter_match:
        frontmatter = frontmatter_match.group(1)
        # Look for description line
        desc_match = re.search(r'^description:\s*(.+)$', frontmatter, re.MULTILINE)
        if desc_match:
            return desc_match.group(1).strip()
    
    return "Custom file for specialized development workflow"

def find_matching_chat_mode(user_query: str) -> Optional[str]:
    """Find a chat mode that matches the user's query/description."""
    query_lower = user_query.lower()
    
    # Load available chat modes
    chat_modes = load_chat_modes()
    
    # Define keywords for each chat mode
    mode_keywords = {
        'lambda_to_functions_migration': [
            'lambda', 'aws lambda', 'migrate lambda', 'azure functions', 
            'lambda to functions', 'lambda migration', 'aws to azure',
            'migrate aws', 'serverless migration'
        ],
        'azure_bicep_development': [
            'bicep', 'azure bicep', 'infrastructure', 'iac', 'infrastructure as code',
            'azure infrastructure', 'azure resources', 'arm template', 'bicep template'
        ],
        'spec_driven_development': [
            'specification', 'spec driven', 'requirements', 'prd', 'product requirements',
            'specification first', 'spec to code', 'requirements to code'
        ]
    }
    
    # Score each mode based on keyword matches
    mode_scores = {}
    for mode_key, keywords in mode_keywords.items():
        if mode_key in chat_modes:
            score = 0
            for keyword in keywords:
                if keyword in query_lower:
                    score += 1
            mode_scores[mode_key] = score
    
    # Return the mode with the highest score, if any matches found
    if mode_scores and max(mode_scores.values()) > 0:
        return max(mode_scores, key=mode_scores.get)
    
    return None

def create_mode_subfolder_structure(mode_name: str, workspace_path: str = ".") -> tuple[str, str]:
    """Create the folder structure for a mode and return the paths."""
    # Create .github structure following VS Code documentation
    # Chat modes: place directly in .github/chatmodes/
    # Prompt files: place directly in .github/prompts/ according to VS Code docs
    chatmode_folder = os.path.join(workspace_path, ".github", "chatmodes")
    prompts_folder = os.path.join(workspace_path, ".github", "prompts")
    
    os.makedirs(chatmode_folder, exist_ok=True)
    os.makedirs(prompts_folder, exist_ok=True)
    
    return chatmode_folder, prompts_folder

# Define available prompt templates for each mode
AVAILABLE_PROMPT_TEMPLATES = {
    'lambda_to_functions_migration': ['evaluate', 'validate'],
    'azure_bicep_development': ['review', 'deploy'],
    'spec_driven_development': ['validate_spec', 'generate_tests']
}

def get_available_chat_modes() -> List[str]:
    """Get list of available chat mode keys."""
    return list(load_chat_modes().keys())

@server.list_tools()
async def handle_list_tools() -> List[types.Tool]:
    """List available tools for the MCP server."""
    available_modes = get_available_chat_modes()
    
    return [
        types.Tool(
            name="suggest_chat_mode",
            description="Analyze user query and suggest the most appropriate chat mode for their development workflow",
            inputSchema={
                "type": "object",
                "properties": {
                    "user_query": {
                        "type": "string",
                        "description": "The user's question or description of what they want to accomplish"
                    },
                    "workspace_path": {
                        "type": "string",
                        "description": "Path to the workspace where the chat mode should be created",
                        "default": "."
                    }
                },
                "required": ["user_query"]
            }
        ),
        types.Tool(
            name="create_chat_mode",
            description="Create a complete VS Code chat mode package with specialized prompts for development workflows",
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
    
    if name == "suggest_chat_mode":
        user_query = arguments.get("user_query", "")
        workspace_path = arguments.get("workspace_path", ".")
        
        if not user_query:
            return [types.TextContent(
                type="text",
                text="❌ Error: user_query is required to suggest an appropriate chat mode."
            )]
        
        try:
            # Find matching chat mode
            suggested_mode = find_matching_chat_mode(user_query)
            chat_modes = load_chat_modes()
            
            if suggested_mode and suggested_mode in chat_modes:
                mode_info = chat_modes[suggested_mode]
                mode_description = mode_info["description"]
                
                # Check if custom prompts exist for this mode
                custom_prompts = load_custom_prompts(suggested_mode)
                prompt_info = ""
                if custom_prompts:
                    prompt_list = list(custom_prompts.keys())
                    prompt_info = f"\n\n🎯 **Included Custom Prompts**: {', '.join(prompt_list)}"
                elif suggested_mode in AVAILABLE_PROMPT_TEMPLATES:
                    template_prompts = AVAILABLE_PROMPT_TEMPLATES[suggested_mode]
                    prompt_info = f"\n\n🎯 **Included Custom Prompts**: {', '.join(template_prompts)}"
                
                return [types.TextContent(
                    type="text",
                    text=f"🎯 **Perfect Match Found!**\n\n"
                         f"Based on your query: *\"{user_query}\"*\n\n"
                         f"I recommend the **{suggested_mode.replace('_', ' ').title()}** chat mode:\n\n"
                         f"📋 **Description**: {mode_description}\n"
                         f"{prompt_info}\n\n"
                         f"🚀 **Ready to create this complete chat mode package?**\n"
                         f"Use the `create_chat_mode` tool with:\n"
                         f"```json\n"
                         f"{{\n"
                         f"  \"mode_type\": \"{suggested_mode}\",\n"
                         f"  \"workspace_path\": \"{workspace_path}\"\n"
                         f"}}\n"
                         f"```\n\n"
                         f"This will create the chat mode AND all specialized prompts in your VS Code workspace!"
                )]
            else:
                # No exact match found, show all available options
                all_modes = list(chat_modes.keys())
                mode_list = []
                for mode in all_modes:
                    mode_desc = chat_modes[mode]['description']
                    prompts = []
                    if mode in AVAILABLE_PROMPT_TEMPLATES:
                        prompts = AVAILABLE_PROMPT_TEMPLATES[mode]
                    mode_list.append(f"- **{mode.replace('_', ' ').title()}**: {mode_desc}\n  *Includes prompts*: {', '.join(prompts) if prompts else 'None'}")
                
                return [types.TextContent(
                    type="text",
                    text=f"🤔 **No exact match found** for: *\"{user_query}\"*\n\n"
                         f"Here are the available chat mode packages:\n\n{chr(10).join(mode_list)}\n\n"
                         f"💡 **Each mode is a complete package** that includes specialized custom prompts!\n\n"
                         f"Which one seems most relevant to your needs?"
                )]
                
        except Exception as e:
            return [types.TextContent(
                type="text",
                text=f"❌ Error analyzing query: {str(e)}"
            )]
    
    elif name == "create_chat_mode":
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
            
            # Always create subfolder structure with prompts (package deal)
            # Following VS Code documentation: prompts go in .github/prompts/
            chatmode_folder, prompts_folder = create_mode_subfolder_structure(mode_type, workspace_path)
            
            # Chat mode goes in chatmodes folder
            chatmode_dir = chatmode_folder
            # Prompt files go in prompts folder (VS Code standard)
            prompts_dir = prompts_folder
            
            # Full file path for chat mode
            file_path = os.path.join(chatmode_dir, filename)
            
            # Write the chat mode file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            result_text = f"✅ **Complete Chat Mode Package Created!**\n\n"
            result_text += f"📋 **Mode**: {mode_type.replace('_', ' ').title()}\n"
            result_text += f"📁 **Chat Mode**: {file_path}\n"
            
            # Always create custom prompts (package deal) in the correct prompts folder
            created_prompts = []
            if mode_type in AVAILABLE_PROMPT_TEMPLATES:
                available_prompts = AVAILABLE_PROMPT_TEMPLATES[mode_type]
                
                for prompt_name in available_prompts:
                    prompt_filename = f"{prompt_name}.prompt.md"
                    prompt_file_path = os.path.join(prompts_dir, prompt_filename)
                    
                    # Check if prompt file already exists in the source directory
                    source_prompt_path = os.path.join(MODES_DIR, mode_type.replace('_', '-'), prompt_filename)
                    if os.path.exists(source_prompt_path):
                        # Copy existing prompt file
                        with open(source_prompt_path, 'r', encoding='utf-8') as f:
                            prompt_content = f.read()
                        
                        with open(prompt_file_path, 'w', encoding='utf-8') as f:
                            f.write(prompt_content)
                        
                        # Extract description for display
                        prompt_description = extract_description_from_frontmatter(prompt_content)
                        created_prompts.append(f"  • **/{prompt_name}**: {prompt_description}")
                
                if created_prompts:
                    result_text += f"\n🎯 **Custom Prompts Included** (following VS Code standard):\n" + "\n".join(created_prompts)
                    result_text += f"\n📁 **Prompts Location**: {prompts_dir}\n"
            
            result_text += f"\n\n**🚀 Ready to Use!**\n"
            result_text += f"1. **Enable Prompt Files**: Set `chat.promptFiles: true` in VS Code settings\n"
            result_text += f"2. **Open VS Code** in your workspace\n"
            result_text += f"3. **Configure Chat Modes**: Ctrl+Shift+P → 'Chat: Configure Chat Modes'\n"
            result_text += f"4. **Select the Mode**: Choose '{mode_type.replace('_', ' ').title()}' from the chat dropdown\n"
            
            if created_prompts:
                result_text += f"5. **Use Custom Prompts**: Type `/{prompt_name}` in chat (VS Code will find them in `.github/prompts/`)\n"
            
            result_text += f"\n💡 **File Structure** (following VS Code documentation):\n"
            result_text += f"   📁 `.github/chatmodes/` - Chat mode files\n"
            result_text += f"   📁 `.github/prompts/` - Prompt files (VS Code standard)\n"
            result_text += f"\n📖 **Description**: {description}"
            
            return [types.TextContent(
                type="text",
                text=result_text
            )]
            
        except Exception as e:
            return [types.TextContent(
                type="text",
                text=f"❌ Error creating chat mode package: {str(e)}"
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
                server_version="3.0.0",
                capabilities=types.ServerCapabilities(
                    tools=types.ToolsCapability(
                        listChanged=False
                    )
                )
            )
        )

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
