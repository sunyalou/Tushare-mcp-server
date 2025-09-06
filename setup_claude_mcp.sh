#!/bin/bash

# Tushare MCP Server - Claude Desktop Setup Script
# This script helps you configure Claude Desktop with the Tushare MCP Server

echo "🚀 Setting up Tushare MCP Server for Claude Desktop..."
echo

# Check if TUSHARE_TOKEN is set
if [ -z "$TUSHARE_TOKEN" ]; then
    echo "⚠️  TUSHARE_TOKEN environment variable is not set."
    echo "Please set your Tushare API token first:"
    echo "export TUSHARE_TOKEN='your_tushare_api_token_here'"
    echo
    read -p "Enter your Tushare API token now (or press Enter to skip): " token_input
    if [ -n "$token_input" ]; then
        export TUSHARE_TOKEN="$token_input"
        echo "✅ TUSHARE_TOKEN set temporarily for this session"
    else
        echo "⚠️  No token provided. You'll need to manually update the config file."
    fi
else
    echo "✅ TUSHARE_TOKEN is already set: ${TUSHARE_TOKEN:0:10}..."
fi

# Claude Desktop config path
CLAUDE_CONFIG_DIR="$HOME/Library/Application Support/Claude"
CLAUDE_CONFIG_FILE="$CLAUDE_CONFIG_DIR/config.json"

# Check if Claude Desktop is installed
if [ ! -d "$CLAUDE_CONFIG_DIR" ]; then
    echo "❌ Claude Desktop config directory not found at: $CLAUDE_CONFIG_DIR"
    echo "Please make sure Claude Desktop is installed and has been run at least once."
    exit 1
fi

# Backup existing config if it exists
if [ -f "$CLAUDE_CONFIG_FILE" ]; then
    backup_file="$CLAUDE_CONFIG_FILE.backup.$(date +%Y%m%d_%H%M%S)"
    echo "💾 Backing up existing config to: $backup_file"
    cp "$CLAUDE_CONFIG_FILE" "$backup_file"
fi

# Create or update the config file
echo "🔧 Configuring Claude Desktop..."

# If config file exists, merge with existing config
if [ -f "$CLAUDE_CONFIG_FILE" ]; then
    # Use Python to merge JSON files properly
    python3 -c "
import json
import os

config_file = '$CLAUDE_CONFIG_FILE'
tushare_token = os.environ.get('TUSHARE_TOKEN', 'your_tushare_api_token_here')

# Read existing config
with open(config_file, 'r') as f:
    config = json.load(f)

# Add MCP servers section if it doesn't exist
if 'mcpServers' not in config:
    config['mcpServers'] = {}

# Add Tushare server
config['mcpServers']['tushare'] = {
    'command': 'python',
    'args': ['-m', 'tushare_mcp_server.main'],
    'env': {
        'TUSHARE_TOKEN': tushare_token
    }
}

# Write updated config
with open(config_file, 'w') as f:
    json.dump(config, f, indent=2)

print('✅ Claude Desktop configuration updated successfully!')
print('📁 Config file location:', config_file)
"
else
    # Create new config file
    cat > "$CLAUDE_CONFIG_FILE" << EOF
{
  "scale": 0,
  "locale": "en-US", 
  "userThemeMode": "system",
  "mcpServers": {
    "tushare": {
      "command": "python",
      "args": ["-m", "tushare_mcp_server.main"],
      "env": {
        "TUSHARE_TOKEN": "${TUSHARE_TOKEN:-your_tushare_api_token_here}"
      }
    }
  }
}
EOF
    echo "✅ New Claude Desktop configuration created!"
fi

echo
echo "🎉 Setup complete!"
echo
echo "📋 Next steps:"
echo "1. Restart Claude Desktop to load the new configuration"
echo "2. Test the connection by asking: 'Tell me about Ping An Bank (000001.SZ)'"
echo "3. If you see errors, check that:"
echo "   - Your Tushare API token is correct"
echo "   - Python and required packages are installed"
echo "   - The project is in your Python path"
echo
echo "🔧 Configuration file location: $CLAUDE_CONFIG_FILE"
echo "📖 For more information, see the README.md file"