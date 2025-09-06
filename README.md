# Tushare MCP Server

A Model Context Protocol (MCP) server that provides AI assistants with access to Chinese stock market data through the Tushare API.

## 🌟 Features

- **Core Market Data APIs** - Basic stock information and price data
- **Daily, Weekly, Monthly Prices** - Historical stock price data
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

### Example 3: Get Weekly Stock Data

**User Query:** "Show me weekly data for 000001.SZ"

**Claude will use:** `weekly` tool

**Parameters:**
```json
{
  "ts_code": "000001.SZ",
  "start_date": "20240101",
  "end_date": "20240131"
}
```

**Returns:** Weekly OHLC prices and trading volume

### Example 4: Get Monthly Stock Data

**User Query:** "Show me monthly data for 000001.SZ"

**Claude will use:** `monthly` tool

**Parameters:**
```json
{
  "ts_code": "000001.SZ",
  "start_date": "20240101",
  "end_date": "20241231"
}
```

**Returns:** Monthly OHLC prices and trading volume

## 🔧 Available Tools

### Stock Basic Information
- **`stock_basic`** - Basic stock and company information

### Market Data
- **`daily`** - Daily stock prices (OHLC, volume, amount)
- **`weekly`** - Weekly stock data (requires 2000+ Tushare points)
- **`monthly`** - Monthly stock data (requires 2000+ Tushare points)

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

API documentation is available in the `api/` directory for implemented endpoints:

- **Authentication & Usage** (`api/authentication-usage.md`)
- **Stock Basic Information** (`api/stock_basic.md`)
- **Market Data** (`api/data_daily.md`, `api/data_weekly.md`, `api/data_monthly.md`)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Tushare Pro](https://tushare.pro/) for providing the financial data API
- [Model Context Protocol](https://modelcontextprotocol.io/) for the MCP specification
- The open-source community for the excellent tools and libraries

---

**Happy trading! 🚀**