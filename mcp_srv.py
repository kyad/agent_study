# https://qiita.com/tinymouse/items/2e22b655d8ba5fe6f3b3

import mcp

mcp = mcp.server.fastmcp.FastMCP("mcp-server-example")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


@mcp.tool()
def ask_information(word: str) -> str:
    """Get information about the given keyword."""
    match word:
        case "なごや個人開発者の集い":
            answer = "毎週日曜日に開催する定例オフライン開発会です。"
        case _:
            answer = "不明"
    return answer


if __name__ == "__main__":
    mcp.run(transport="stdio")
