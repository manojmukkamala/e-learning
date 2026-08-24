# pip install -qU langchain langchain-ollama

import json
import urllib.error
import urllib.request
import shlex
import subprocess

from langchain.agents import create_agent
from langchain_ollama import ChatOllama
from langchain.tools import tool
from deepagents import create_deep_agent

from rich.markdown import Markdown
from rich.console import Console

########## model
model = ChatOllama(
    model="gemma4:31b",
    temperature=0.2,
    timeout=300,
    max_tokens=25000,
    validate_model_on_init=True,
    reasoning=True,
)

########## tools
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

@tool
def fetch_text_from_url(url: str) -> str:
    """Fetch the document from a URL.
    """
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (compatible; quickstart-research/1.0)"},
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            raw = resp.read()
    except urllib.error.URLError as e:
        return f"Fetch failed: {e}"
    text = raw.decode("utf-8", errors="replace")
    return text


@tool
def shell_access(
    command: str | list[str], timeout: float | None = None
) -> tuple[int, str, str]:
    """
    Execute a shell command and capture its output.

    Args:
        command: Command to run, either as a string (e.g. "ls -la") or a
            list of args (e.g. ["ls", "-la"]). String commands are parsed
            with shlex so they run without invoking a shell interpreter.
        timeout: Optional timeout in seconds. If exceeded, the command is
            killed and reported as a timeout rather than hanging forever.

    Returns:
        A tuple (return_code, stdout, stderr):
            - return_code: process exit code, or -1 if the command could
              not be launched/completed (check stderr for why).
            - stdout: captured standard output.
            - stderr: captured standard error, or a description of what
              went wrong if the command never ran.
    """
    if isinstance(command, str):
        command = shlex.split(command)

    try:
        result = subprocess.run(
            command, capture_output=True, text=True, timeout=timeout
        )
        return result.returncode, result.stdout, result.stderr
    except FileNotFoundError as e:
        return -1, "", f"Command not found: {e}"
    except subprocess.TimeoutExpired as e:
        return -1, e.stdout or "", f"Command timed out after {timeout}s"
    except Exception as e:
        return -1, "", str(e)

########## system prompt
SYSTEM_PROMPT = """You are a literary data assistant.

## Capabilities

- `fetch_text_from_url`: loads document text from a URL into the conversation.
"""

########## agent
agent = create_agent(
    model=model,
    tools=[get_weather, fetch_text_from_url, shell_access],
    system_prompt="You are a helpful assistant",
)

# result = agent.invoke(
#     {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]}
# )

# res = result["messages"][-1].content_blocks
# print(json.dumps(res))

result = agent.invoke(
    {"messages": [{"role": "user", "content": "Who is gautamiputra satakarni according to wikipedia?"}]}
)

# res = result["messages"][-1].content_blocks
# print(json.dumps(res))

# result = agent.invoke(
#     {"messages": [{"role": "user", "content": "Can you pull the list of categories available in transactsync using the api key: ``? If there are no results, simply return `No data available`. Here is this API spec for reference: https://transactsync-api.ourhomelab.com/openapi.json?"}]}
# )

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What can you do with shell?"}]}
)

res = result["messages"][-1].content_blocks
md = Markdown(res[1]["text"])

console = Console()
console.print(md)


########## deep agent

# deep_agent = create_deep_agent(
#     model=model,
#     tools=[shell_access],
#     system_prompt="You are a helpful assistant. Do not use sub-agents",
# )

# result = deep_agent.invoke(
#     {"messages": [{"role": "user", "content": "Can you run curl commands?"}]}
# )

# res = result["messages"][-1].content_blocks
# print(json.dumps(res))

# result = deep_agent.invoke(
#     {"messages": [{"role": "user", "content": "Who is gautamiputra satakarni according to wikipedia? Also include the list of tools you used to answer this question."}]}
# )

# res = result["messages"][-1].content_blocks
# print(json.dumps(res))

