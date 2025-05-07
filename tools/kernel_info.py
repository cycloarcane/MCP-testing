"""
kernel_info.py — FastMCP tool that returns kernel info via `uname -a`
"""
from fastmcp import FastMCP          # core server class :contentReference[oaicite:4]{index=4}
import subprocess

mcp = FastMCP("kernel")              # tool route will be /kernel

@mcp.tool()
def get_kernel() -> str:
    """Return full kernel string as in `uname -a`."""
    return subprocess.check_output(["uname", "-a"], text=True).strip()  # uname(1) :contentReference[oaicite:5]{index=5}

if __name__ == "__main__":
    # stdio transport = perfect for mcpo
    mcp.run(transport="stdio")
