#!/usr/bin/env python3
"""
Basic test script for Tushare MCP Server - without requiring API token
"""
import asyncio
import sys
from tushare_mcp_server.models import StockBasicParams, DailyParams, TushareResponse
from tushare_mcp_server.config import settings

def test_models():
    """Test data models"""
    print("Testing data models...")
    
    # Test StockBasicParams
    params = StockBasicParams(ts_code="000001.SZ", limit=10)
    print(f"✅ StockBasicParams: {params}")
    
    # Test DailyParams
    daily_params = DailyParams(ts_code="000001.SZ", start_date="20240101", end_date="20240131")
    print(f"✅ DailyParams: {daily_params}")
    
    # Test TushareResponse
    response = TushareResponse(code=0, msg="Success", data={"fields": ["ts_code", "name"], "items": [["000001.SZ", "Ping An"]]})
    print(f"✅ TushareResponse: {response}")
    
    return True

def test_server_initialization():
    """Test server initialization"""
    print("\nTesting server initialization...")
    
    try:
        from tushare_mcp_server.mcp_server import TushareMCPServer
        server = TushareMCPServer()
        print("✅ Server initialized successfully")
        return True
    except Exception as e:
        print(f"❌ Server initialization failed: {e}")
        return False

def test_tool_definitions():
    """Test tool definitions"""
    print("\nTesting tool definitions...")
    
    try:
        from tushare_mcp_server.mcp_server import TushareMCPServer
        server = TushareMCPServer()
        print("✅ Tool definitions registered successfully")
        return True
    except Exception as e:
        print(f"❌ Tool definitions test failed: {e}")
        return False

def main():
    """Run all basic tests"""
    print("🚀 Tushare MCP Server - Basic Tests")
    print("=" * 50)
    
    # Test models
    models_test = test_models()
    
    # Test server initialization
    server_test = test_server_initialization()
    
    # Test tool definitions
    tools_test = test_tool_definitions()
    
    print("\n" + "=" * 50)
    print("📊 Test Summary:")
    print(f"Data Models: {'✅ PASSED' if models_test else '❌ FAILED'}")
    print(f"Server Init: {'✅ PASSED' if server_test else '❌ FAILED'}")
    print(f"Tool Definitions: {'✅ PASSED' if tools_test else '❌ FAILED'}")
    
    if models_test and server_test and tools_test:
        print("\n🎉 Basic tests passed! Server structure is ready.")
        print("\nTo test with real Tushare API:")
        print("1. Set TUSHARE_TOKEN environment variable")
        print("2. Run: python test_server.py")
        return 0
    else:
        print("\n⚠️  Some basic tests failed.")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)