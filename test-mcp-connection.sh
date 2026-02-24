#!/bin/bash
# Test MCP Server Connection
# This script verifies that MCP servers can be started and are responsive

echo "🔍 Testing MCP Server Connections..."
echo ""

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Test entscheidsuche-mcp
echo "1️⃣  Testing entscheidsuche-mcp..."
ENTSCHEIDSUCHE_PATH="/Users/thibault/Documents/legal-assistant/mcp-servers/entscheidsuche-mcp/build/index.js"

if [ -f "$ENTSCHEIDSUCHE_PATH" ]; then
    echo -e "${GREEN}✓${NC} File exists: $ENTSCHEIDSUCHE_PATH"
    
    # Try to start the server (will timeout after 2 seconds, which is expected)
    timeout 2s node "$ENTSCHEIDSUCHE_PATH" 2>&1 | head -n 1 &
    SERVER_PID=$!
    sleep 1
    
    if ps -p $SERVER_PID > /dev/null 2>&1; then
        echo -e "${GREEN}✓${NC} Server process started successfully"
        kill $SERVER_PID 2>/dev/null
    else
        echo -e "${YELLOW}⚠${NC}  Server exited (this may be normal for stdio servers)"
    fi
else
    echo -e "${RED}✗${NC} File not found: $ENTSCHEIDSUCHE_PATH"
fi

echo ""

# Test onlinekommentar-mcp
echo "2️⃣  Testing onlinekommentar-mcp..."
ONLINEKOMMENTAR_PATH="/Users/thibault/Documents/legal-assistant/mcp-servers/onlinekommentar-mcp/build/index.js"

if [ -f "$ONLINEKOMMENTAR_PATH" ]; then
    echo -e "${GREEN}✓${NC} File exists: $ONLINEKOMMENTAR_PATH"
    
    # Try to start the server (will timeout after 2 seconds, which is expected)
    timeout 2s node "$ONLINEKOMMENTAR_PATH" 2>&1 | head -n 1 &
    SERVER_PID=$!
    sleep 1
    
    if ps -p $SERVER_PID > /dev/null 2>&1; then
        echo -e "${GREEN}✓${NC} Server process started successfully"
        kill $SERVER_PID 2>/dev/null
    else
        echo -e "${YELLOW}⚠${NC}  Server exited (this may be normal for stdio servers)"
    fi
else
    echo -e "${RED}✗${NC} File not found: $ONLINEKOMMENTAR_PATH"
fi

echo ""

# Check MCP configuration
echo "3️⃣  Checking MCP configuration..."
MCP_CONFIG="/Users/thibault/Documents/legal-assistant/.opencode/mcp.json"

if [ -f "$MCP_CONFIG" ]; then
    echo -e "${GREEN}✓${NC} MCP config exists: $MCP_CONFIG"
    
    # Validate JSON
    if python3 -m json.tool "$MCP_CONFIG" > /dev/null 2>&1; then
        echo -e "${GREEN}✓${NC} MCP config is valid JSON"
        
        # Show config
        echo ""
        echo "📋 Current MCP Configuration:"
        cat "$MCP_CONFIG" | python3 -m json.tool
    else
        echo -e "${RED}✗${NC} MCP config has invalid JSON"
    fi
else
    echo -e "${RED}✗${NC} MCP config not found: $MCP_CONFIG"
fi

echo ""

# Check opencode.jsonc
echo "4️⃣  Checking opencode.jsonc..."
OPENCODE_CONFIG="/Users/thibault/Documents/legal-assistant/opencode.jsonc"

if [ -f "$OPENCODE_CONFIG" ]; then
    echo -e "${GREEN}✓${NC} opencode.jsonc exists: $OPENCODE_CONFIG"
    
    # Show config
    echo ""
    echo "📋 Current opencode.jsonc:"
    cat "$OPENCODE_CONFIG"
    
    echo ""
    echo -e "${YELLOW}ℹ${NC}  To verify configuration, run: opencode"
else
    echo -e "${RED}✗${NC} opencode.jsonc not found: $OPENCODE_CONFIG"
fi

echo ""
echo "✅ MCP Connection Test Complete"
echo ""
echo "Next steps:"
echo "  1. Restart OpenWork to load MCP servers"
echo "  2. Check available tools/functions in OpenWork"
echo "  3. Test with: \"Load the swiss-case-law-research skill\""
