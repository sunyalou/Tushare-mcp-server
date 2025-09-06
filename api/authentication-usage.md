# Tushare API Authentication and Usage Guide

## Authentication

### Getting Started
1. Register for a community account on Tushare platform
2. Obtain your API token from the user center
3. Use token globally or pass it with each request

### Python SDK Authentication
```python
import tushare as ts

# Set token once (or when it expires)
ts.set_token('your token here')

# Create API client
pro = ts.pro_api()  # or pro_api('your token')
```

## API Call Methods

| Method | Entry Point | Required Fields |
|--------|-------------|----------------|
| Python SDK | `pro.query(api_name, **params)` or `pro.api_name(**params)` | No additional fields |
| HTTP REST | POST `http://api.tushare.pro` | `api_name`, `token`, `params`, `fields` |

## Common Parameters

- **`api_name`**: Interface name, e.g., `"trade_cal"`
- **`token`**: User credential token
- **`params`**: Interface-specific filters, e.g., `{"start_date":"20180901","end_date":"20181001"}`
- **`fields`**: Comma-separated return columns, e.g., `"exchange,cal_date,is_open"`

## Response Structure

```json
{
  "code": 0,          // 0 = success; 2002 = insufficient permissions
  "msg": null,        // Error message if any
  "data": {
    "fields": ["column1", "column2"],
    "items": [[value1, value2], ...]
  }
}
```

## Points and Rate Limiting System

### Points System
- Platform uses a "points" system where different interfaces consume different amounts of points
- Daily free quota available
- Check "points frequency correspondence table" and "points expiration query" for current rules
- Exceeding quota requires recharge or wait for next day reset

### Rate Limiting
- No specific QPS given in official documentation
- Recommended: single-thread with 200ms+ intervals for safety
- High-frequency needs can apply for custom services

## Quick Example

### Python SDK Example
Get non-trading calendar for September 2018:
```python
df = pro.trade_cal(exchange='', start_date='20180901',
                   end_date='20181001', is_open='0',
                   fields='exchange,cal_date,is_open,pretrade_date')
```

### HTTP REST Example
```bash
curl -X POST -d '{
  "api_name":"trade_cal",
  "token":"xxxxxxxx",
  "params":{
    "exchange":"",
    "start_date":"20180901",
    "end_date":"20181001",
    "is_open":"0"
  },
  "fields":"exchange,cal_date,is_open,pretrade_date"
}' http://api.tushare.pro
```