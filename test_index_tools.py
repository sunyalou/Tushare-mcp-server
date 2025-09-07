#!/usr/bin/env python3
"""
Test script for Tushare MCP Server Index Tools - demonstrates usage
"""
import asyncio
import json
from tushare_mcp_server.mcp_server import TushareMCPServer
from tushare_mcp_server.config import settings

async def test_index_tools():
    """Test all index-related tools"""
    server = TushareMCPServer()
    
    print("🚀 Testing Index Tools")
    print("=" * 50)
    
    # Test 1: index_daily
    print("\n📈 Testing index_daily...")
    try:
        result = await server.handle_call_tool("index_daily", {
            "ts_code": "000001.SH",
            "start_date": "20240101",
            "end_date": "20240105"
        })
        print(f"✅ index_daily: {len(json.loads(result[0].text).get('items', []))} records")
    except Exception as e:
        print(f"❌ index_daily failed: {e}")
    
    # Test 2: index_weekly
    print("\n📊 Testing index_weekly...")
    try:
        result = await server.handle_call_tool("index_weekly", {
            "ts_code": "399300.SZ",
            "trade_date": "20240105"
        })
        print(f"✅ index_weekly: {len(json.loads(result[0].text).get('items', []))} records")
    except Exception as e:
        print(f"❌ index_weekly failed: {e}")
    
    # Test 3: index_monthly
    print("\n📅 Testing index_monthly...")
    try:
        result = await server.handle_call_tool("index_monthly", {
            "ts_code": "000001.SH",
            "start_date": "20240101",
            "end_date": "20241231"
        })
        print(f"✅ index_monthly: {len(json.loads(result[0].text).get('items', []))} records")
    except Exception as e:
        print(f"❌ index_monthly failed: {e}")
    
    # Test 4: index_dailybasic
    print("\n🔍 Testing index_dailybasic...")
    try:
        result = await server.handle_call_tool("index_dailybasic", {
            "ts_code": "399300.SZ",
            "trade_date": "20240105"
        })
        print(f"✅ index_dailybasic: {len(json.loads(result[0].text).get('items', []))} records")
    except Exception as e:
        print(f"❌ index_dailybasic failed: {e}")
    
    # Test 5: index_weight
    print("\n⚖️  Testing index_weight...")
    try:
        result = await server.handle_call_tool("index_weight", {
            "index_code": "399300.SZ",
            "trade_date": "20240105"
        })
        print(f"✅ index_weight: {len(json.loads(result[0].text).get('items', []))} records")
    except Exception as e:
        print(f"❌ index_weight failed: {e}")
    
    print("\n" + "=" * 50)
    print("✅ Index tools testing completed!")
    print("\n📋 Available Index Tools:")
    print("• index_daily - Daily index prices and trading data")
    print("• index_weekly - Weekly index prices and trading data") 
    print("• index_monthly - Monthly index prices and trading data")
    print("• index_dailybasic - Daily index indicators (PE, PB, turnover)")
    print("• index_weight - Index component weights and constituents")
    
    print("\n💡 Usage Examples:")
    print("# Get Shanghai Composite daily data")
    print('{"ts_code": "000001.SH", "start_date": "20240101", "end_date": "20240131"}')
    print("\n# Get CSI 300 weekly data")
    print('{"ts_code": "399300.SZ", "trade_date": "20240105"}')
    print("\n# Get index PE, PB, turnover rate")
    print('{"ts_code": "399300.SZ", "trade_date": "20240105"}')
    print("\n# Get CSI 300 constituent weights")
    print('{"index_code": "399300.SZ", "trade_date": "20240105"}')

if __name__ == "__main__":
    asyncio.run(test_index_tools())