"""Startup script for ``just blender``: open the Blender GUI with the
BlenderMCP server running, so Claude can drive the session and capture
images for blog posts.

Run by ``blender [file.blend] --python tools/launch_blender.py`` *without*
``--background``, so Blender continues into the GUI after this returns.
Nothing here touches the scene, the window layout, or the user's
preferences, and nothing here may abort startup: a missing BlenderMCP
install is reported and skipped.
"""

import os
import sys

import addon_utils
import bpy

#: Module names the BlenderMCP add-on is installed under. ``uvx
#: mcp-for-blender install-addon`` writes ``blender_mcp.py``; a manual install
#: of the upstream ``addon.py`` keeps its file stem.
MCP_ADDON_MODULES = (
    [os.environ["BLENDER_MCP_ADDON"]]
    if os.environ.get("BLENDER_MCP_ADDON")
    else ["blender_mcp", "addon"]
)

MCP_SETUP_COMMAND = "uvx mcp-for-blender install-addon"

#: The GUI is not up yet when this script runs, so the server start is
#: deferred by a timer rather than called inline.
SERVER_START_DELAY_SECONDS = 1.0


def log(message: str) -> None:
    """Print a tagged line that stands out in Blender's startup noise."""
    print(f"[just blender] {message}", file=sys.stderr)


def enable_mcp_addon() -> bool:
    """Enable the first BlenderMCP add-on found. Returns whether it is available."""
    for module in MCP_ADDON_MODULES:
        _enabled, loaded = addon_utils.check(module)
        if not loaded:
            addon_utils.enable(module, default_set=False)
        # bpy.ops creates arbitrary namespaces on access, even for absent add-ons.
        if "start_server" in dir(bpy.ops.blendermcp):
            log(f"BlenderMCP add-on enabled: {module}")
            return True

    log(f"WARNING: BlenderMCP add-on not found ({', '.join(MCP_ADDON_MODULES)})")
    log(f"         install it with `{MCP_SETUP_COMMAND}`")
    log("         (override the module name with BLENDER_MCP_ADDON=<name>)")
    return False


def start_mcp_server() -> None:
    """Start the BlenderMCP server. One-shot timer callback."""
    scene = bpy.context.scene
    if getattr(scene, "blendermcp_server_running", False):
        log(f"MCP server already running on port {scene.blendermcp_port}")
        return

    bpy.ops.blendermcp.start_server()
    log(f"MCP server listening on port {scene.blendermcp_port}")


if enable_mcp_addon():
    bpy.app.timers.register(start_mcp_server, first_interval=SERVER_START_DELAY_SECONDS)
