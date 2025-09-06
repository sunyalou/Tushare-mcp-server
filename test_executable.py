#!/usr/bin/env python3
"""
Test script to verify the bin executables work correctly
"""
import subprocess
import sys
import os

def test_executable():
    """Test the bin executables"""
    print("🧪 Testing Tushare MCP Server executables...")
    
    # Set test token
    env = os.environ.copy()
    env['TUSHARE_TOKEN'] = 'test_token'
    
    # Test both executables
    executables = ['./bin/tushare-mcp', './bin/tushare-mcp-server']
    
    for exe in executables:
        print(f"\n📋 Testing {exe}...")
        
        try:
            # Start the process
            process = subprocess.Popen(
                [exe],
                env=env,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            # Wait a moment to see if it starts properly
            try:
                stdout, stderr = process.communicate(timeout=2)
                returncode = process.returncode
                
                if returncode == 0:
                    print(f"✅ {exe} completed successfully")
                else:
                    print(f"⚠️  {exe} exited with code {returncode}")
                    if stderr:
                        print(f"   Error: {stderr.strip()}")
                        
            except subprocess.TimeoutExpired:
                # Process is still running (expected for MCP server)
                process.kill()
                process.wait()
                print(f"✅ {exe} started successfully (MCP server mode)")
                
        except FileNotFoundError:
            print(f"❌ {exe} not found")
        except Exception as e:
            print(f"❌ {exe} failed: {e}")

if __name__ == "__main__":
    test_executable()