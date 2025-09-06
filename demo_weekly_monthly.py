#!/usr/bin/env python3
"""
Demo script for weekly and monthly stock data APIs
Shows how to use the new weekly and monthly endpoints
"""
import os
import asyncio
from tushare_mcp_server.tushare_client import TushareClient

async def demo_weekly_monthly():
    """Demonstrate weekly and monthly stock data APIs"""
    
    # Get token from environment variable
    token = os.getenv('TUSHARE_TOKEN')
    if not token:
        print("❌ Error: TUSHARE_TOKEN environment variable not set!")
        print("   Please set your Tushare API token:")
        print("   export TUSHARE_TOKEN='your_tushare_api_token_here'")
        return
    
    client = TushareClient(token)
    
    print("📊 Weekly & Monthly Stock Data API Demo")
    print("="*60)
    print("Stock: 601888.SH (China Tourism Group Duty Free)")
    print("Period: Q1 2024 (Jan-Mar)")
    print()
    
    # Weekly Data Demo
    print("📅 WEEKLY DATA (Weekly Candlesticks)")
    print("-" * 40)
    
    weekly_params = {
        'ts_code': '601888.SH',
        'start_date': '20240101',
        'end_date': '20240331'
    }
    
    try:
        weekly_response = await client.get_weekly(weekly_params)
        
        if weekly_response.code == 0 and weekly_response.data:
            items = weekly_response.data.get('items', [])
            fields = weekly_response.data.get('fields', [])
            
            print(f"✅ Retrieved {len(items)} weekly records")
            print(f"📋 Fields: {fields}")
            print()
            
            # Display weekly data in table format
            header = "{:<12} {:<10} {:<10} {:<10} {:<10} {:<12} {:<10}".format(
                "Week End", "Open", "High", "Low", "Close", "Change", "Volume"
            )
            print(header)
            print("-" * len(header))
            
            for item in items[:8]:  # Show first 8 weeks
                data = dict(zip(fields, item))
                print("{:<12} ¥{:<9} ¥{:<9} ¥{:<9} ¥{:<9} ¥{:<11} {:<10}".format(
                    data.get('trade_date', ''),
                    data.get('open', ''),
                    data.get('high', ''),
                    data.get('low', ''),
                    data.get('close', ''),
                    data.get('change', ''),
                    f"{int(float(data.get('vol', 0))):,}"
                ))
            
            if len(items) > 8:
                print(f"... and {len(items) - 8} more weeks")
                
            # Weekly summary
            if items:
                closes = [float(item[fields.index('close')]) for item in items]
                volumes = [float(item[fields.index('vol')]) for item in items]
                pct_changes = [float(item[fields.index('pct_chg')]) for item in items]
                
                print(f"\n📈 Q1 2024 Weekly Summary:")
                print(f"   Highest Close: ¥{max(closes):.2f}")
                print(f"   Lowest Close: ¥{min(closes):.2f}")
                print(f"   Average Weekly Volume: {sum(volumes)/len(volumes)/1e6:.1f}M shares")
                print(f"   Best Week: +{max(pct_changes):.2f}%")
                print(f"   Worst Week: {min(pct_changes):.2f}%")
                
        else:
            print(f"❌ Weekly API Error: {weekly_response.msg}")
            
    except Exception as e:
        print(f"❌ Weekly API Exception: {e}")
    
    print("\n" + "="*60)
    
    # Monthly Data Demo
    print("\n📆 MONTHLY DATA (Monthly Candlesticks)")
    print("-" * 40)
    
    monthly_params = {
        'ts_code': '601888.SH',
        'start_date': '20240101',
        'end_date': '20240331'
    }
    
    try:
        monthly_response = await client.get_monthly(monthly_params)
        
        if monthly_response.code == 0 and monthly_response.data:
            items = monthly_response.data.get('items', [])
            fields = monthly_response.data.get('fields', [])
            
            print(f"✅ Retrieved {len(items)} monthly records")
            print(f"📋 Fields: {fields}")
            print()
            
            # Display monthly data
            header = "{:<12} {:<10} {:<10} {:<10} {:<10} {:<12} {:<10}".format(
                "Month End", "Open", "High", "Low", "Close", "Change", "Volume(M)"
            )
            print(header)
            print("-" * len(header))
            
            for item in items:
                data = dict(zip(fields, item))
                print("{:<12} ¥{:<9} ¥{:<9} ¥{:<9} ¥{:<9} ¥{:<11} {:<10.1f}".format(
                    data.get('trade_date', ''),
                    data.get('open', ''),
                    data.get('high', ''),
                    data.get('low', ''),
                    data.get('close', ''),
                    data.get('change', ''),
                    float(data.get('vol', 0)) / 1e6
                ))
            
            # Monthly analysis
            if items:
                closes = [float(item[fields.index('close')]) for item in items]
                pct_changes = [float(item[fields.index('pct_chg')]) for item in items]
                
                print(f"\n📊 Q1 2024 Monthly Analysis:")
                for i, item in enumerate(items):
                    data = dict(zip(fields, item))
                    month_name = ['Jan', 'Feb', 'Mar'][i] if i < 3 else 'Month'
                    print(f"   {month_name} 2024: Close ¥{data.get('close', '')} ({data.get('pct_chg', '')}%)")
                
                print(f"\n📈 Q1 Performance Summary:")
                print(f"   Starting Price (Jan): ¥{items[0][fields.index('open')]}")
                print(f"   Ending Price (Mar): ¥{items[-1][fields.index('close')]}")
                q1_return = (float(items[-1][fields.index('close')]) - float(items[0][fields.index('open')])) / float(items[0][fields.index('open')]) * 100
                print(f"   Q1 Total Return: {q1_return:.2f}%")
                
        else:
            print(f"❌ Monthly API Error: {monthly_response.msg}")
            
    except Exception as e:
        print(f"❌ Monthly API Exception: {e}")
    
    print("\n" + "="*60)
    print("\n💡 Usage Examples:")
    print("• Weekly data shows weekly OHLC patterns and trends")
    print("• Monthly data provides longer-term perspective")
    print("• Both require 2000+ Tushare points to access")
    print("• Use with Claude Desktop: 'Show me weekly data for 601888'")
    print("\n✅ Weekly & Monthly APIs are now available!")

if __name__ == "__main__":
    asyncio.run(demo_weekly_monthly())