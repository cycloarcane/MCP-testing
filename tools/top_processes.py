#!/usr/bin/env python3
"""
top_processes.py — FastMCP tool that returns the N most CPU‑hungry processes
(plus memory usage) using the standard `ps` command so it works even when
`top` is missing or differently configured.

Example route:
    /top/top_processes            # defaults to 10 entries
    /top/top_processes?limit=5    # custom number of rows

The output is a plain‑text table that mcp can stream straight back to the
client.
"""
from fastmcp import FastMCP
import subprocess

mcp = FastMCP("top")  # tool route will be /top


def _collect(limit: int) -> str:
    """Run `ps` and return the *limit* most CPU‑greedy processes as text."""
    try:
        # -eo: select fields; --sort -%cpu: descending CPU%; --no‑headers: skip header row
        raw = subprocess.check_output(
            [
                "ps",
                "-eo",
                "pid,comm,%cpu,%mem",
                "--sort=-%cpu",
                "--no-headers",
            ],
            text=True,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "ps command failed or is unavailable."

    # Trim to requested number of lines and prettify
    rows = raw.strip().splitlines()[: limit if limit > 0 else None]
    header = f"{'PID':>6} {'COMMAND':<25} {'CPU%':>6} {'MEM%':>6}"
    return "\n".join([header] + rows)


@mcp.tool()
def top_processes(limit: int = 10) -> str:
    """Return a table of the *limit* most CPU‑intensive processes (default 10).

    Parameters
    ----------
    limit : int, optional
        How many processes to include. Must be positive.
    """
    return _collect(limit)


if __name__ == "__main__":
    # stdio transport makes the tool usable by FastMCP without extra plumbing
    mcp.run(transport="stdio")
