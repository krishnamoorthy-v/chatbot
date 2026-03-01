from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo")

@mcp.tool()
def intro() -> str:
    """Get the intro."""
    return f"Hi iam bot2.0"