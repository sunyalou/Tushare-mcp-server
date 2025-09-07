import httpx
import asyncio
from typing import Dict, List, Optional, Any
from .models import TushareRequest, TushareResponse
from .config import settings
import logging

logger = logging.getLogger(__name__)

class TushareClient:
    def __init__(self, token: Optional[str] = None):
        self.token = token or settings.tushare_token
        self.base_url = "https://api.tushare.pro"
        self.timeout = 30.0
        
    async def _make_request(self, api_name: str, params: Dict[str, Any], fields: Optional[str] = None) -> TushareResponse:
        """Make a request to Tushare API"""
        if not self.token:
            raise ValueError("Tushare token is required")
            
        request_data = TushareRequest(
            api_name=api_name,
            token=self.token,
            params=params,
            fields=fields
        )
        
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            try:
                response = await client.post(
                    self.base_url,
                    json=request_data.model_dump()
                )
                response.raise_for_status()
                
                result = response.json()
                tushare_response = TushareResponse(**result)
                
                if tushare_response.code != 0:
                    logger.error(f"Tushare API error: {tushare_response.msg} (code: {tushare_response.code})")
                    raise Exception(f"Tushare API error: {tushare_response.msg}")
                    
                return tushare_response
                
            except httpx.RequestError as e:
                logger.error(f"Request error: {e}")
                raise Exception(f"Request failed: {e}")
            except Exception as e:
                logger.error(f"Unexpected error: {e}")
                raise
    
    async def get_stock_basic(self, params: Dict[str, Any], fields: Optional[str] = None) -> TushareResponse:
        """Get basic stock information"""
        return await self._make_request("stock_basic", params, fields)
    
    async def get_daily(self, params: Dict[str, Any], fields: Optional[str] = None) -> TushareResponse:
        """Get daily stock prices"""
        return await self._make_request("daily", params, fields)
    
    async def get_weekly(self, params: Dict[str, Any], fields: Optional[str] = None) -> TushareResponse:
        """Get weekly stock prices"""
        return await self._make_request("weekly", params, fields)
    
    async def get_monthly(self, params: Dict[str, Any], fields: Optional[str] = None) -> TushareResponse:
        """Get monthly stock prices"""
        return await self._make_request("monthly", params, fields)
    
    async def get_index_daily(self, params: Dict[str, Any], fields: Optional[str] = None) -> TushareResponse:
        """Get index daily prices and trading data"""
        return await self._make_request("index_daily", params, fields)
    
    async def get_index_weekly(self, params: Dict[str, Any], fields: Optional[str] = None) -> TushareResponse:
        """Get index weekly prices and trading data"""
        return await self._make_request("index_weekly", params, fields)
    
    async def get_index_monthly(self, params: Dict[str, Any], fields: Optional[str] = None) -> TushareResponse:
        """Get index monthly prices and trading data"""
        return await self._make_request("index_monthly", params, fields)
    
    async def get_index_dailybasic(self, params: Dict[str, Any], fields: Optional[str] = None) -> TushareResponse:
        """Get index daily basic indicators"""
        return await self._make_request("index_dailybasic", params, fields)
    
    async def get_index_weight(self, params: Dict[str, Any], fields: Optional[str] = None) -> TushareResponse:
        """Get index component weights"""
        return await self._make_request("index_weight", params, fields)