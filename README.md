# Tushare MCP Server

A comprehensive Model Context Protocol (MCP) server that provides AI assistants with access to Chinese financial market data through the Tushare API.

## 🌟 Features

- **20+ Stock Data APIs** - Complete coverage of Chinese stock market data
- **Real-time Market Data** - Daily, weekly, monthly stock prices and indicators
- **Financial Statements** - Income, balance sheet, cash flow data
- **Stock Connect Data** - Hong Kong and mainland China stock connect information
- **Management Information** - Executive data and compensation
- **Full MCP Protocol Support** - Works with Claude Desktop and other MCP clients
- **Professional Error Handling** - Robust API error management
- **Type Safety** - Full Pydantic validation for all parameters

## 🚀 Quick Start

### Installation

#### Option 1: Install from Source
```bash
git clone <repository-url>
cd tushare-mcp-server
pip install -r requirements.txt
pip install -e .
```

#### Option 2: Direct Python Execution
```bash
# Clone and run without installation
git clone <repository-url>
cd tushare-mcp-server
pip install -r requirements.txt
```

### Configuration

1. **Get your Tushare token** from [Tushare Pro](https://tushare.pro/)

2. **Set environment variable:**
   ```bash
   export TUSHARE_TOKEN="your_tushare_api_token_here"
   ```

3. **Or create a .env file:**
   ```bash
   cp .env.example .env
   # Edit .env to add your TUSHARE_TOKEN
   ```

### Basic Usage

#### Command Line
```bash
# Start the MCP server
TUSHARE_TOKEN=your_token python -m tushare_mcp_server.main

# With debug mode
DEBUG=true TUSHARE_TOKEN=your_token python -m tushare_mcp_server.main
```

#### Claude Desktop Integration

Add this configuration to your Claude Desktop settings:

```json
{
  "mcpServers": {
    "tushare": {
      "command": "python",
      "args": ["-m", "tushare_mcp_server.main"],
      "env": {
        "TUSHARE_TOKEN": "your_tushare_api_token_here"
      }
    }
  }
}
```

## 📖 Usage Examples

### Example 1: Get Basic Stock Information

**User Query:** "Tell me about Ping An Bank (000001.SZ)"

**Claude will use:** `stock_basic` tool

**Parameters:**
```json
{
  "ts_code": "000001.SZ"
}
```

**Returns:** Company name, area, industry, listing date, etc.

### Example 2: Get Daily Stock Prices

**User Query:** "Show me the daily prices for 000001.SZ for January 2024"

**Claude will use:** `daily` tool

**Parameters:**
```json
{
  "ts_code": "000001.SZ",
  "start_date": "20240101",
  "end_date": "20240131"
}
```

**Returns:** Open, high, low, close prices, volume, amount for each trading day

### Example 3: Get Financial Statements

**User Query:** "Get the income statement for 000001.SZ for 2023"

**Claude will use:** `income` tool

**Parameters:**
```json
{
  "ts_code": "000001.SZ",
  "period": "20231231"
}
```

**Returns:** Revenue, profit, EPS, and other income statement data

## 🔧 Available Tools

### Stock Basic Information
- **`stock_basic`** - Basic stock and company information
- **`namechange`** - Historical name changes
- **`new_share`** - IPO pipeline and new listings

### Market Data
- **`daily`** - Daily stock prices (OHLC, volume, amount)
- **`weekly`** - Weekly stock data
- **`monthly`** - Monthly stock data
- **`daily_basic`** - Fundamental indicators (PE, PB, PS ratios)
- **`stk_limit`** - Daily price limits (up/down)

### Financial Statements
- **`income`** - Income statements
- **`balancesheet`** - Balance sheets
- **`cashflow`** - Cash flow statements
- **`express`** - Flash financial results
- **`forecast`** - Earnings forecasts

### Trading & Market Info
- **`trade_cal`** - Trading calendar and holidays

### Stock Connect (Hong Kong)
- **`ggt_daily`** - Daily Hong Kong Stock Connect statistics
- **`ggt_top10`** - Top 10 Hong Kong Stock Connect stocks
- **`hsgt_top10`** - Top 10 Shanghai/Shenzhen Stock Connect stocks

### Corporate Governance
- **`stk_managers`** - Management information
- **`stk_rewards`** - Management compensation and holdings

## 📊 Stock Code Format

Stock codes should include exchange suffix:
- **`.SZ`** - Shenzhen Stock Exchange (e.g., `000001.SZ`)
- **`.SH`** - Shanghai Stock Exchange (e.g., `600000.SH`)
- **`.BJ`** - Beijing Stock Exchange (e.g., `830799.BJ`)

## 📅 Date Format

All dates use YYYYMMDD format:
- `20240101` - January 1, 2024
- `20231231` - December 31, 2023

## ⚙️ Configuration Options

### Environment Variables
- **`TUSHARE_TOKEN`** - Your Tushare API token (required)
- **`DEBUG`** - Enable debug logging (optional, default: false)
- **`HOST`** - Server host (optional, default: 0.0.0.0)
- **`PORT`** - Server port (optional, default: 8000)

### .env File Example
```
TUSHARE_TOKEN=your_token_here
DEBUG=false
HOST=0.0.0.0
PORT=8000
```

## 🧪 Testing

### Basic Functionality Test
```bash
# Test package import
python -c "from tushare_mcp_server.main import main; print('✅ Package loads correctly')"

# Run demo
python demo_simple.py

# Start server
TUSHARE_TOKEN=your_token python -m tushare_mcp_server.main
```

## 📚 API Documentation

Complete API documentation is available in the `api/` directory, including:

- **Authentication & Usage** (`api/authentication-usage.md`)
- **Stock Basic Information** (`api/stock_basic.md`)
- **Market Data** (`api/data_daily.md`, `api/data_weekly.md`, etc.)
- **Financial Statements** (`api/finance_income.md`, `api/finance_balancesheet.md`, etc.)
- **Trading Calendar** (`api/trade_cal.md`)
- **Stock Connect** (`api/data_ggt_daily.md`, `api/data_ggt_top10.md`)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Tushare Pro](https://tushare.pro/) for providing the financial data API
- [Model Context Protocol](https://modelcontextprotocol.io/) for the MCP specification
- The open-source community for the excellent tools and libraries

---

**Happy trading! 🚀**