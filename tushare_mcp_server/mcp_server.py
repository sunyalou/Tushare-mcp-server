import json
import logging
from typing import Any, Dict, List, Optional
from mcp.server import Server, NotificationOptions
from mcp.server.models import InitializationOptions
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent, ImageContent, EmbeddedResource
from .tushare_client import TushareClient
from .models import *
from .config import settings

logger = logging.getLogger(__name__)

class TushareMCPServer:
    def __init__(self):
        self.server = Server("tushare-mcp-server")
        self.client = TushareClient()
        self._setup_tools()
        
    async def handle_call_tool(self, name: str, arguments: Dict[str, Any]) -> List[TextContent]:
        """Handle tool calls"""
        try:
            logger.info(f"Calling tool: {name} with arguments: {arguments}")
            
            # Remove None values from arguments
            params = {k: v for k, v in arguments.items() if v is not None}
            
            if name == "stock_basic":
                response = await self.client.get_stock_basic(params)
            elif name == "daily":
                response = await self.client.get_daily(params)
            elif name == "weekly":
                response = await self.client.get_weekly(params)
            elif name == "monthly":
                response = await self.client.get_monthly(params)
            elif name == "index_daily":
                response = await self.client.get_index_daily(params)
            elif name == "index_weekly":
                response = await self.client.get_index_weekly(params)
            elif name == "index_monthly":
                response = await self.client.get_index_monthly(params)
            elif name == "index_dailybasic":
                response = await self.client.get_index_dailybasic(params)
            elif name == "index_weight":
                response = await self.client.get_index_weight(params)
            else:
                raise ValueError(f"Unknown tool: {name}")
            
            if response.data:
                return [TextContent(
                    type="text",
                    text=json.dumps(response.data, ensure_ascii=False, indent=2)
                )]
            else:
                return [TextContent(
                    type="text",
                    text="No data returned from Tushare API"
                )]
                
        except Exception as e:
            logger.error(f"Error calling tool {name}: {e}")
            return [TextContent(
                type="text",
                text=f"Error: {str(e)}"
            )]
    
    def _setup_tools(self):
        """Setup all MCP tools"""
        
        @self.server.list_tools()
        async def handle_list_tools() -> List[Tool]:
            return [
                Tool(
                    name="stock_basic",
                    description="Get basic stock information and company details",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "ts_code": {"type": "string", "description": "Stock code (e.g., 000001.SZ)"},
                            "name": {"type": "string", "description": "Company name"},
                            "exchange": {"type": "string", "description": "Exchange code (SSE, SZSE, BSE)"},
                            "market": {"type": "string", "description": "Market type (主板, 科创板, 创业板, 北交所)"},
                            "is_hs": {"type": "string", "description": "Hong Kong Stock Connect eligibility (N, H, S)"},
                            "list_status": {"type": "string", "description": "Listing status (L, D, P)"},
                            "limit": {"type": "integer", "description": "Number of records to return (max 2000)"},
                            "offset": {"type": "integer", "description": "Offset for pagination"}
                        }
                    }
                ),
                Tool(
                    name="daily",
                    description="Get daily stock prices and trading data",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "ts_code": {"type": "string", "description": "Stock code (e.g., 000001.SZ)"},
                            "trade_date": {"type": "string", "description": "Trade date (YYYYMMDD format)"},
                            "start_date": {"type": "string", "description": "Start date (YYYYMMDD format)"},
                            "end_date": {"type": "string", "description": "End date (YYYYMMDD format)"}
                        }
                    }
                ),
                Tool(
                    name="weekly",
                    description="Get weekly stock prices and trading data (requires 2000+ Tushare points)",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "ts_code": {"type": "string", "description": "Stock code (e.g., 000001.SZ)"},
                            "trade_date": {"type": "string", "description": "Trade date (weekly last trading date, YYYYMMDD format)"},
                            "start_date": {"type": "string", "description": "Start date (YYYYMMDD format)"},
                            "end_date": {"type": "string", "description": "End date (YYYYMMDD format)"}
                        }
                    }
                ),
                Tool(
                    name="monthly",
                    description="Get monthly stock prices and trading data (requires 2000+ Tushare points)",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "ts_code": {"type": "string", "description": "Stock code (e.g., 000001.SZ)"},
                            "trade_date": {"type": "string", "description": "Trade date (monthly last trading date, YYYYMMDD format)"},
                            "start_date": {"type": "string", "description": "Start date (YYYYMMDD format)"},
                            "end_date": {"type": "string", "description": "End date (YYYYMMDD format)"}
                        }
                    }
                ),
                Tool(
                    name="index_daily",
                    description="Get index daily prices and trading data (requires 2000+ Tushare points)",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "ts_code": {"type": "string", "description": "Index code (e.g., 000001.SH, 399300.SZ)"},
                            "trade_date": {"type": "string", "description": "Trade date (YYYYMMDD format)"},
                            "start_date": {"type": "string", "description": "Start date (YYYYMMDD format)"},
                            "end_date": {"type": "string", "description": "End date (YYYYMMDD format)"}
                        }
                    }
                ),
                Tool(
                    name="index_weekly",
                    description="Get index weekly prices and trading data (requires 600+ Tushare points)",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "ts_code": {"type": "string", "description": "Index code (e.g., 000001.SH, 399300.SZ)"},
                            "trade_date": {"type": "string", "description": "Trade date (weekly last trading date, YYYYMMDD format)"},
                            "start_date": {"type": "string", "description": "Start date (YYYYMMDD format)"},
                            "end_date": {"type": "string", "description": "End date (YYYYMMDD format)"}
                        }
                    }
                ),
                Tool(
                    name="index_monthly",
                    description="Get index monthly prices and trading data (requires 600+ Tushare points)",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "ts_code": {"type": "string", "description": "Index code (e.g., 000001.SH, 399300.SZ)"},
                            "trade_date": {"type": "string", "description": "Trade date (monthly last trading date, YYYYMMDD format)"},
                            "start_date": {"type": "string", "description": "Start date (YYYYMMDD format)"},
                            "end_date": {"type": "string", "description": "End date (YYYYMMDD format)"}
                        }
                    }
                ),
                Tool(
                    name="index_dailybasic",
                    description="Get index daily basic indicators like PE, PB, turnover rate (requires 400+ Tushare points)",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "ts_code": {"type": "string", "description": "Index code (e.g., 000001.SH, 399300.SZ)"},
                            "trade_date": {"type": "string", "description": "Trade date (YYYYMMDD format)"},
                            "start_date": {"type": "string", "description": "Start date (YYYYMMDD format)"},
                            "end_date": {"type": "string", "description": "End date (YYYYMMDD format)"}
                        }
                    }
                ),
                Tool(
                    name="index_weight",
                    description="Get index component weights and constituents (requires 2000+ Tushare points)",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "index_code": {"type": "string", "description": "Index code, source from index basic info interface"},
                            "trade_date": {"type": "string", "description": "Trade date (YYYYMMDD format)"},
                            "start_date": {"type": "string", "description": "Start date (YYYYMMDD format)"},
                            "end_date": {"type": "string", "description": "End date (YYYYMMDD format)"}
                        }
                    }
                )
            ]
        
        @self.server.call_tool()
        async def handle_call_tool(name: str, arguments: Dict[str, Any]) -> List[TextContent]:
            """Handle tool calls"""
            return await self.handle_call_tool(name, arguments)
    
    async def run(self):
        """Run the MCP server"""
        async with stdio_server() as (read_stream, write_stream):
            await self.server.run(
                read_stream,
                write_stream,
                InitializationOptions(
                    server_name="tushare-mcp-server",
                    server_version="0.1.0",
                    capabilities=self.server.get_capabilities(
                        notification_options=NotificationOptions(),
                        experimental_capabilities={},
                    )
                )
            )