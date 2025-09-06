#!/usr/bin/env python3
"""
Tushare MCP Server - Simple Demo

This script shows basic usage without requiring user input.
"""

import os
from tushare_mcp_server.models import StockBasicParams, DailyParams, TushareResponse
from tushare_mcp_server.config import settings

def simple_demo():
    """Simple demonstration of basic functionality"""
    print("🚀 Tushare MCP Server - Simple Demo")
    print("=" * 50)
    
    # Check if token is configured
    token = os.environ.get("TUSHARE_TOKEN", "")
    if not token:
        print("⚠️  TUSHARE_TOKEN not set. Showing demo without API calls.")
        print("To run full demo, set: export TUSHARE_TOKEN='your_token'")
        print("\n📋 What you can do with this server:")
        show_examples()
        return
    
    print(f"✅ Using Tushare token: {token[:10]}...")
    
    try:
        # Initialize client
        from tushare_mcp_server.tushare_client import TushareClient
        client = TushareClient(token)
        
        print("\n1️⃣ Testing stock basic info...")
        response = client.get_stock_basic({"limit": 2})
        if response.code == 0 and response.data:
            items = response.data.get('items', [])
            print(f"✅ Successfully retrieved {len(items)} stocks")
            print("✅ API connection working!")
        else:
            print(f"❌ API error: {response.msg}")
        
        print("\n✅ Server is ready to use!")
        print("\n🎯 Next steps:")
        print("1. Configure Claude Desktop with MCP settings")
        print("2. Start asking questions about Chinese stocks")
        print("3. Check README.md for full documentation")
        
    except Exception as e:
        print(f"❌ Demo failed: {e}")

def show_examples():
    """Show example usage without API calls"""
    examples = [
        "Tell me about Ping An Bank (000001.SZ)",
        "Show me daily prices for 000001.SZ last month",
        "Get income statement for 000001.SZ 2023",
        "What are the trading days this month?",
        "Show me top 10 Hong Kong Stock Connect stocks"
    ]
    
    print("\nExample questions you can ask Claude:")
    for i, example in enumerate(examples, 1):
        print(f"{i}. {example}")
    
    print("\n🔧 Available tools:")
    tools = [
        "stock_basic - Company information",
        "daily - Daily stock prices", 
        "income - Income statements",
        "trade_cal - Trading calendar",
        "ggt_top10 - Top HK Stock Connect stocks"
    ]
    for tool in tools:
        print(f"  - {tool}")

if __name__ == "__main__":
    simple_demo()