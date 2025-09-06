#!/usr/bin/env python3
"""
Test MCP server integration for weekly and monthly tools
"""
import asyncio
import json
from tushare_mcp_server.mcp_server import TushareMCPServer
from tushare_mcp_server.config import settings

async def test_mcp_integration():
    """Test MCP server with new weekly and monthly tools"""
    
    # Set the token from environment variable
    import os
    token = os.getenv('TUSHARE_TOKEN')
    if not token:
        print("❌ Error: TUSHARE_TOKEN environment variable not set!")
        print("   Please set your Tushare API token:")
        print("   export TUSHARE_TOKEN='your_tushare_api_token_here'")
        return
    settings.tushare_token = token
    
    print("🔧 Testing MCP Server Integration")
    print("="*50)
    
    # Initialize server
    server = TushareMCPServer()
    
    # Test that we have 4 tools now (stock_basic, daily, weekly, monthly)
    print("\n📋 Testing MCP Tools Directly:")
    print("  • stock_basic: Basic stock information")
    print("  • daily: Daily stock prices")
    print("  • weekly: Weekly stock prices (NEW)")
    print("  • monthly: Monthly stock prices (NEW)")
    
    # Test weekly tool
    print("\n📅 Testing Weekly Tool via MCP...")
    weekly_args = {
        'ts_code': '601888.SH',
        'start_date': '20240101',
        'end_date': '20240331'
    }
    
    try:
        weekly_result = await server.handle_call_tool('weekly', weekly_args)
        if weekly_result:
            weekly_data = json.loads(weekly_result[0].text)
            items = weekly_data.get('items', [])
            print(f"✅ Weekly tool: Retrieved {len(items)} weekly records")
            if items:
                print(f"   Sample: Week ending {items[0][1]} - Close: ¥{items[0][2]}")
    except Exception as e:
        print(f"❌ Weekly tool error: {e}")
    
    # Test monthly tool
    print("\n📆 Testing Monthly Tool via MCP...")
    monthly_args = {
        'ts_code': '601888.SH',
        'start_date': '20240101',
        'end_date': '20240331'
    }
    
    try:
        monthly_result = await server.handle_call_tool('monthly', monthly_args)
        if monthly_result:
            monthly_data = json.loads(monthly_result[0].text)
            items = monthly_data.get('items', [])
            print(f"✅ Monthly tool: Retrieved {len(items)} monthly records")
            if items:
                print(f"   Sample: Month ending {items[0][1]} - Close: ¥{items[0][2]}")
    except Exception as e:
        print(f"❌ Monthly tool error: {e}")
    
    print("\n" + "="*50)
    print("✅ MCP integration test completed!")

if __name__ == "__main__":
    asyncio.run(test_mcp_integration())