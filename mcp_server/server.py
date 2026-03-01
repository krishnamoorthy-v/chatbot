from mcp.server.fastmcp import FastMCP
from tools.demo import intro
from tools.websearch import web_search
import logging

name = "Enterprise MCP Server"
logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(name)



def create_server() -> FastMCP:
    server = FastMCP(name=name)

    # register tools
    server.add_tool(intro)
    server.add_tool(web_search)
    return server


if __name__ == "__main__":

    try:
        logger.info("server initialized")
        server = create_server()
        server.run(transport="sse")
    except Exception as e:
        logger.error("server setup error")
