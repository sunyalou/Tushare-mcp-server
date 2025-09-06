#!/usr/bin/env python3
import asyncio
import logging
import sys
import os

try:
    from .mcp_server import TushareMCPServer
    from .config import settings
except ImportError:
    from mcp_server import TushareMCPServer
    from config import settings

def setup_logging():
    """Setup logging configuration"""
    logging.basicConfig(
        level=logging.DEBUG if settings.debug else logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )

async def main():
    """Main entry point"""
    setup_logging()
    
    if not settings.tushare_token:
        print("Error: TUSHARE_TOKEN environment variable is required")
        sys.exit(1)
    
    server = TushareMCPServer()
    await server.run()

if __name__ == "__main__":
    asyncio.run(main())