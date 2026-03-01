from mcp.server.fastmcp import FastMCP
from duckduckgo_search import DDGS

mcp = FastMCP("DuckDuckGo MCP Server")

@mcp.tool()
def web_search(query: str, max_results: int = 5):
    """
    Search the web using DuckDuckGo
    """
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=max_results)
        return [
            {
                "title": r.get("title"),
                "url": r.get("href"),
                "snippet": r.get("body"),
            }
            for r in results
        ]