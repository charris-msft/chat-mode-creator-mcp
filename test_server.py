#!/usr/bin/env python3
"""
Simple test script to validate the MCP server functionality
"""
import os
import asyncio
from mcp_chatmode_server import handle_call_tool

async def test_single_mode(mode_type: str):
    """Test creating a single chat mode"""
    print(f"\n🧪 Testing {mode_type} chat mode creation...")
    
    result = await handle_call_tool(
        "create_chat_mode",
        {
            "mode_type": mode_type,
            "workspace_path": ".",
            "output_path": "test_output"  # Use custom path for testing
        }
    )
    
    print(f"✅ Result: {result[0].text[:100]}...")
    return result

async def main():
    """Main test function"""
    print("🚀 Starting MCP Chat Mode Creator Tests")
    print("=" * 50)
    
    # Test each mode type
    modes = ["spec_driven_development", "lambda_to_functions", "azure_bicep_development"]
    
    for mode in modes:
        await test_single_mode(mode)
        await asyncio.sleep(0.1)  # Small delay between tests
    
    # Verify files were created
    print("\n📁 Checking created files...")
    test_dir = "./test_output"
    if os.path.exists(test_dir):
        files = os.listdir(test_dir)
        print(f"✅ Created {len(files)} files in {test_dir}:")
        for file in files:
            print(f"   - {file}")
    else:
        print("❌ Test output directory not found")
    
    print("\n🎉 All tests completed!")

if __name__ == "__main__":
    asyncio.run(main())
