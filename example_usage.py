"""
Example usage of the Chat Mode Creator MCP server
"""
import asyncio
import json
from mcp_chatmode_server import server, handle_call_tool

async def example_create_modes():
    """Example of creating all three chat modes"""
    
    # Create Spec-Driven Development mode
    sdd_result = await handle_call_tool(
        "create_chat_mode",
        {
            "mode_type": "spec_driven_development",
            "workspace_path": "."
        }
    )
    print("SDD Mode Result:", sdd_result[0].text)
    
    # Create Lambda to Functions Migration mode
    migration_result = await handle_call_tool(
        "create_chat_mode", 
        {
            "mode_type": "lambda_to_functions",
            "workspace_path": "."
        }
    )
    print("\nMigration Mode Result:", migration_result[0].text)
    
    # Create Azure Bicep Development mode
    bicep_result = await handle_call_tool(
        "create_chat_mode",
        {
            "mode_type": "azure_bicep_development", 
            "workspace_path": "."
        }
    )
    print("\nBicep Mode Result:", bicep_result[0].text)

if __name__ == "__main__":
    asyncio.run(example_create_modes())
