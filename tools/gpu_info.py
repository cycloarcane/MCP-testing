#!/usr/bin/env python3
"""
gpu_info.py — FastMCP tool that returns GPU info via `nvidia-smi`
"""
from fastmcp import FastMCP
import subprocess, shutil

mcp = FastMCP("gpu")                 # tool route will be /gpu

@mcp.tool()
def gpu_summary() -> str:
    """
    Return one‑line GPU summary (`nvidia-smi -L`).
    Gracefully degrades if nvidia‑smi is absent.
    """
    if shutil.which("nvidia-smi") is None:
        return "nvidia-smi not found — no NVIDIA GPU detected."
    return subprocess.check_output(["nvidia-smi", "-L"], text=True).strip()  # NVSMI docs :contentReference[oaicite:6]{index=6}

if __name__ == "__main__":
    mcp.run(transport="stdio")
