#!/usr/bin/env python3
"""
Test script for weekly and monthly stock data APIs
"""
import os
import asyncio
from tushare_mcp_server.tushare_client import TushareClient

async def test_weekly_monthly_apis():
    """Test the new weekly and monthly APIs"""
    # Get token from environment variable
    token = os.getenv('TUSHARE_TOKEN')
    if not token:
        print("❌ Error: TUSHARE_TOKEN environment variable not set!")
        print("   Please set your Tushare API token:")
        print("   export TUSHARE_TOKEN='your_tushare_api_token_here'")
        return
    
    client = TushareClient(token)
    
    print("🧪 Testing Weekly and Monthly Stock Data APIs")
    print("="*60)
    
    # Test parameters
    test_params = {
        'ts_code': '601888.SH',
        'start_date': '20240101',
        'end_date': '20240430'
    }
    
    # Test Weekly API
    print("\n📅 Testing Weekly API...")
    try:
        weekly_response = await client.get_weekly(test_params)
        
        if weekly_response.code == 0:
            if weekly_response.data and weekly_response.data.get('items'):
                items = weekly_response.data.get('items', [])
                fields = weekly_response.data.get('fields', [])
                print(f"✅ Weekly API: Retrieved {len(items)} weekly records")
                print(f"📋 Fields: {fields}")
                
                # Show first week of data
                if items:
                    first_week = dict(zip(fields, items[0]))
                    print(f"📊 Sample week: {first_week.get('trade_date', 'N/A')} - Close: ¥{first_week.get('close', 'N/A')}")
            else:
                print("⚠️  Weekly API: No data returned")
        else:
            print(f"❌ Weekly API Error: {weekly_response.msg}")
            
    except Exception as e:
        print(f"❌ Weekly API Exception: {e}")
    
    # Test Monthly API
    print("\n📆 Testing Monthly API...")
    try:
        monthly_response = await client.get_monthly(test_params)
        
        if monthly_response.code == 0:
            if monthly_response.data and monthly_response.data.get('items'):
                items = monthly_response.data.get('items', [])
                fields = monthly_response.data.get('fields', [])
                print(f"✅ Monthly API: Retrieved {len(items)} monthly records")
                print(f"📋 Fields: {fields}")
                
                # Show first month of data
                if items:
                    first_month = dict(zip(fields, items[0]))
                    print(f"📊 Sample month: {first_month.get('trade_date', 'N/A')} - Close: ¥{first_month.get('close', 'N/A')}")
            else:
                print("⚠️  Monthly API: No data returned")
        else:
            print(f"❌ Monthly API Error: {monthly_response.msg}")
            
    except Exception as e:
        print(f"❌ Monthly API Exception: {e}")
    
    print("\n" + "="*60)
    print("✅ API testing completed!")

if __name__ == "__main__":
    asyncio.run(test_weekly_monthly_apis())