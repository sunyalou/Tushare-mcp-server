#!/usr/bin/env python3
"""Test script for index APIs"""
import asyncio
import json
from tushare_mcp_server.tushare_client import TushareClient

async def test_index_apis():
    """Test the new index API methods"""
    client = TushareClient()
    
    # Test parameters for different index APIs
    test_params = {
        "ts_code": "000001.SH",  # Shanghai Composite Index
        "trade_date": "20230101"
    }
    
    print("Testing index_daily...")
    try:
        result = await client.get_index_daily(test_params)
        print(f"Success: {len(result.data.get('items', []))} records returned")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\nTesting index_weekly...")
    try:
        result = await client.get_index_weekly(test_params)
        print(f"Success: {len(result.data.get('items', []))} records returned")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\nTesting index_monthly...")
    try:
        result = await client.get_index_monthly(test_params)
        print(f"Success: {len(result.data.get('items', []))} records returned")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\nTesting index_dailybasic...")
    try:
        result = await client.get_index_dailybasic(test_params)
        print(f"Success: {len(result.data.get('items', []))} records returned")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\nTesting index_weight...")
    try:
        weight_params = {
            "index_code": "399300.SZ",  # CSI 300 Index
            "trade_date": "20230101"
        }
        result = await client.get_index_weight(weight_params)
        print(f"Success: {len(result.data.get('items', []))} records returned")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(test_index_apis())