# Claude Desktop MCP Setup Guide for Tushare MCP Server

## 🚀 Quick Setup

### Option 1: Automated Setup (Recommended)
```bash
# Run the setup script
./setup_claude_mcp.sh
```

### Option 2: Manual Setup
1. **Get your Tushare API token** from [Tushare Pro](https://tushare.pro/)
2. **Update your Claude Desktop config** at `~/Library/Application Support/Claude/config.json`

## 📋 Configuration

### Claude Desktop Configuration
Your Claude Desktop config file should include:

```json
{
  "scale": 0,
  "locale": "en-US",
  "userThemeMode": "system",
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

### Environment Variables
You can also set the token as an environment variable:
```bash
export TUSHARE_TOKEN="your_tushare_api_token_here"
```

## 🔧 Troubleshooting

### Common Issues

1. **"Command not found" error**
   - Make sure Python is in your PATH
   - Try using full path to Python: `/usr/bin/python` or `/usr/local/bin/python3`

2. **"Tushare token required" error**
   - Verify your TUSHARE_TOKEN is correct
   - Check that the token is properly set in the config

3. **"Module not found" error**
   - Install the package: `pip install -e .`
   - Make sure you're in the project directory

4. **Connection issues**
   - Check your internet connection
   - Verify Tushare API is accessible
   - Try running the demo script first: `python demo_simple.py`

### Testing Your Setup

1. **Test basic functionality:**
   ```bash
   python test_basic.py
   ```

2. **Test with your token:**
   ```bash
   TUSHARE_TOKEN=your_token python demo_simple.py
   ```

3. **Test server startup:**
   ```bash
   TUSHARE_TOKEN=your_token python -m tushare_mcp_server.main
   ```

## 🎯 Usage Examples

Once configured, you can ask Claude questions like:

- "Tell me about Ping An Bank (000001.SZ)"
- "Show me daily prices for 000001.SZ last month"
- "Get income statement for 000001.SZ 2023"
- "What are the trading days this month?"
- "Show me top 10 Hong Kong Stock Connect stocks"

## 📁 File Locations

- **Claude Config**: `~/Library/Application Support/Claude/config.json`
- **Backup Config**: `claude_mcp_config.json` (in project directory)
- **Setup Script**: `setup_claude_mcp.sh`
- **Project Config**: `.env` file (optional)

## 🔍 Verification Steps

1. **Check Claude Desktop recognizes the server:**
   - Restart Claude Desktop
   - Look for MCP server status in settings

2. **Test with a simple query:**
   - Ask "What stocks do you have information about?"
   - Should return basic stock information

3. **Check server logs:**
   - Look for any error messages
   - Verify API calls are being made

## 🆘 Getting Help

If you encounter issues:
1. Check the troubleshooting section above
2. Verify your Tushare API token is valid
3. Test the server independently with `demo_simple.py`
4. Check Claude Desktop logs for specific error messages

## 📚 Available Tools

The Tushare MCP Server provides these tools:
- `stock_basic` - Company information
- `daily` - Daily stock prices
- `weekly` - Weekly stock prices
- `monthly` - Monthly stock prices
- `income` - Income statements
- `balance_sheet` - Balance sheet data
- `cashflow` - Cash flow statements
- `trade_cal` - Trading calendar
- `ggt_top10` - Top Hong Kong Stock Connect stocks
- And many more... see `api/` directory for full documentation