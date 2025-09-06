# Tushare Pro API Quick Start Guide

## Base Configuration

**Base URL**: `https://api.tushare.pro`

**Authentication**: All requests must include your API token in the POST body

## Request Format

All API calls use POST method with JSON body:

```json
{
  "api_name": "<interface_name>",
  "token": "<your_token>",
  "params": {<key_value_parameters>},
  "fields": ["<column1>", "<column2>"]
}
```

## Response Format

```json
{
  "code": 0,
  "msg": null,
  "data": {
    "fields": ["<column_names>"],
    "items": [[<row1_data>], [<row2_data>], ...]
  }
}
```

## Exchange Code Suffix Rules

- **SSE (Shanghai Stock Exchange)**: `.SH`
- **SZSE (Shenzhen Stock Exchange)**: `.SZ`
- **BSE (Beijing Stock Exchange)**: `.BJ`
- **HKEX (Hong Kong Stock Exchange)**: `.HK`

## Core API Endpoints

### Equity Information
- `stock_basic` - List of A-shares
- `trade_cal` - Exchange calendar
- `hk_hold` - Stock-Connect constituents
- `namechange` - Historical names
- `new_share` - IPO pipeline

### Market Data
- `daily` - End-of-day bars
- `moneyflow` - Daily capital flow
- `stk_factor` - Adjustment factors & metrics
- `suspend` - Halt/resume log

### Financial Data
- `income` - Income statement
- `balancesheet` - Balance sheet
- `cashflow` - Cash flow statement
- `forecast` - Earnings guidance
- `express` - Flash results
- `dividend` - Splits & dividends
- `fina_indicator` - Calculated ratios
- `fina_audit` - Auditor opinion
- `mainbz` - Revenue breakdown