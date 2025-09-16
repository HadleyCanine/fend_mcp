#/usr/bin/env python
# A simple MCP server wrapping the fend calculator.

from os.path import dirname, join, abspath
import subprocess

from mcp.server.fastmcp import FastMCP

# relative to the location of this script itself
MANUAL_LOCAL_PATH = "./fend-manual-llm.txt"

# Command used to call fend (assumed to be in PATH, change this if it's not)
FEND_COMMAND = "fend"

# resource URI
MANUAL_URI = "fend://manual"

mcp = FastMCP("fend calculator")


@mcp.tool()
def fend(q: str) -> str:
    """an arbitrary-precision unit-aware calculator.
    
    This tool supports a wide range of calculations including arithmetic (e.g., +, -, *, /, ^, !),
    unit conversions (e.g., kg, m, s, N, mph), temperature conversions (absolute and relative),
    date calculations, and even D&D-style dice rolls (e.g., 3d6).
    
    Example query: `sqrt((146.6 m)^2 + (230.3 m / 2)^2) to furlongs`
    
    Important Usage Notes:
    - Always group numbers and units together using parentheses, e.g., `(4 m) / (2 m)`.
    - For inches, use the full word 'inch' instead of 'in' to avoid conflicts with the unit conversion notation.
    - The result of the last successful calculation can be referenced using `_` or `ans`.
    - Supports various output formats (e.g., fractions, specific decimal places).
    
    For a comprehensive guide and advanced features, see the manual: `manual()`
    """

    try:
        result = subprocess.run(
            [FEND_COMMAND, "-e", q],
            capture_output=True,
            timeout=5,
            encoding="utf-8",
            text=True,
            check=True,
        )
        return result.stdout.strip()
    except Exception as e:
        return f"Error running fend: `{e}`\nThe MCP tool is incorrectly setup, additional calls will not work.\nCheck that fend is installed and is in the PATH (or hardcode FEND_COMMAND in the script)."


@mcp.resource(MANUAL_URI, mime_type="text/plain")
def manual_resource() -> str:
    """Get the fend manual."""
    script_path = dirname(abspath(__file__))
    manual_path = join(script_path, MANUAL_LOCAL_PATH)

    with open(manual_path, "r") as f:
        return f.read()


# Ugh the above resource doesn't seem to work with Jan, so adding this tool wrapper
@mcp.tool()
def manual() -> str:
    """Get the fend manual."""
    return manual_resource()


if __name__ == "__main__":
    mcp.run()