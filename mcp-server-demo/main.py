from mcp.server.fastmcp import FastMCP
import dns.resolver

mcp = FastMCP("DNS check")


@mcp.tool("DNS Check")
def check_dns(domain: str, record: str) -> str:
    """Check DNS record"""
    result = dns.resolver.resolve(domain, record)
    output = []
    for val in result:
        output.append(f'{record} Record: {val.to_text()}')
    
    return '\n'.join(output)

@mcp.tool("Clean")
def clean_text(tekst: str) -> str:
    tekst_new = tekst.replace("*", "")
    """Clear tekst from markdown signs"""
    return tekst_new