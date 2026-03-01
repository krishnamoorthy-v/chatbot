import sys
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
server_path = os.path.join(BASE_DIR, "mcp_server", "server.py")


async def local_mcp_client():
    print(f"DEBUG: Attempting to start server at: {server_path}")
    if not os.path.exists(server_path):
        print("ERROR: Could not find server.py at that path! Please check your folder names.")
        return

    client = MultiServerMCPClient(
        {
            "local": {
                "transport": "sse",
                "url": "http://localhost:8000/sse",
            }
        }
    )

    return client
