from typing import Dict, List, Optional, Any, Union
from pydantic import BaseModel, Field
from datetime import date

class TushareRequest(BaseModel):
    api_name: str
    token: str
    params: Dict[str, Any] = {}
    fields: Optional[str] = None

class TushareResponse(BaseModel):
    code: int
    msg: Optional[str] = None
    data: Optional[Dict[str, Any]] = None

class StockBasicParams(BaseModel):
    ts_code: Optional[str] = None
    name: Optional[str] = None
    exchange: Optional[str] = None
    market: Optional[str] = None
    is_hs: Optional[str] = None
    list_status: Optional[str] = None
    limit: Optional[int] = 2000
    offset: Optional[int] = 0

class DailyParams(BaseModel):
    ts_code: Optional[str] = None
    trade_date: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None

class WeeklyParams(BaseModel):
    ts_code: Optional[str] = None
    trade_date: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None

class MonthlyParams(BaseModel):
    ts_code: Optional[str] = None
    trade_date: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None