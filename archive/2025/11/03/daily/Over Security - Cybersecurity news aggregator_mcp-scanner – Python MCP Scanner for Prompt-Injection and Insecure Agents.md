---
title: mcp-scanner – Python MCP Scanner for Prompt-Injection and Insecure Agents
url: https://www.darknet.org.uk/2025/10/mcp-scanner-python-mcp-scanner-for-prompt-injection-and-insecure-agents/
source: Over Security - Cybersecurity news aggregator
date: 2025-11-03
fetch_date: 2025-11-04T03:11:28.983111
---

# mcp-scanner – Python MCP Scanner for Prompt-Injection and Insecure Agents

* [Skip to main content](#genesis-content)
* [Skip to primary sidebar](#genesis-sidebar-primary)
* [Skip to footer](#genesis-footer-widgets)

* [Home](https://www.darknet.org.uk/)
* [About Darknet](https://www.darknet.org.uk/about/)
* [Hacking Tools](https://www.darknet.org.uk/category/hacking-tools/)
* [Popular Posts](https://www.darknet.org.uk/popular-posts/)
* [Darknet Archives](https://www.darknet.org.uk/darknet-archives/)
* [Contact Darknet](https://www.darknet.org.uk/contact-darknet/)
  + [Advertise](https://www.darknet.org.uk/contact-darknet/advertise/)
  + [Submit a Tool](https://www.darknet.org.uk/contact-darknet/submit-a-tool/)

[![Darknet – Hacking Tools, Hacker News & Cyber Security](https://www.darknet.org.uk/wp-content/uploads/2022/12/cropped-darknet_2022_logo.png)](https://www.darknet.org.uk/)

Darknet - Hacking Tools, Hacker News & Cyber Security

Darknet is your best source for the latest hacking tools, hacker news, cyber security best practices, ethical hacking & pen-testing.

# mcp-scanner – Python MCP Scanner for Prompt-Injection and Insecure Agents

October 31, 2025

Views: 331

mcp-scanner is an open-source Python tool that scans Model Context Protocol (MCP) servers and agent tooling for prompt injection, jailbreaks, and insecure tool patterns. It uses deterministic YARA-style checks and a large language model (LLM) judge to classify risky prompts. The project also integrates with Cisco’s AI Defense Inspect API.

![mcp-scanner - Python MCP Scanner for Prompt-Injection and Insecure Agents](data:image/svg+xml...)![mcp-scanner - Python MCP Scanner for Prompt-Injection and Insecure Agents](https://www.darknet.org.uk/wp-content/uploads/2025/11/mcp-scanner-Python-MCP-Scanner-for-Prompt-Injection-and-Insecure-Agents-640x427.jpg)

## Overview

MCP endpoints expose a new attack surface: agent frameworks that consume untrusted prompt templates or tool descriptors. mcp-scanner audits these points automatically. It scans local codebases or live endpoints, flags weak prompt handling and open tool hooks, and ranks risk with an LLM judge. For red teams, it provides quick reconnaissance; for defenders, it enforces secure-prompt hygiene before release.

Unlike traditional web scanners, mcp-scanner understands agent semantics. You can extend findings by chaining it with proven recon and fuzzing tools already covered on Darknet, such as [Burp Suite](https://www.darknet.org.uk/2007/01/burp-proxy-burp-suite-attacking-web-applications/), [OWASP ZAP](https://www.darknet.org.uk/2015/05/owasp-zed-attack-proxy-integrated-penetration-testing-tool/), and techniques in the [fuzzing archive](https://www.darknet.org.uk/tag/fuzzing/).

## Features

* **Three scanning engines:** deterministic signature matching, an LLM-as-judge for contextual triage, and Cisco AI Defense Inspect API integration that enriches analysis.
* **Two operation modes:** a command-line scanner for ad hoc checks, or a REST API server for automation pipelines.
* **Authentication aware:** accepts explicit auth parameters and OAuth tokens to test protected MCP endpoints safely.
* **Custom rules:** extend or tune YARA-style signatures for your own engagement scope.
* **Structured reports:** outputs JSON and text summaries that feed straight into ticketing or continuous-monitoring systems.

## Installation

To install from Source:

git clone https://github.com/cisco-ai-defense/mcp-scanner
cd mcp-scanner
# Install with uv (recommended)
uv venv -p &lt;Python version less than or equal to 3.13&gt; /path/to/your/choice/of/venv/directory
source /path/to/your/choice/of/venv/directory/bin/activate
uv pip install .
# Or install in development mode
uv pip install -e .

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11 | git clone https://github.com/cisco-ai-defense/mcp-scanner  cd mcp-scanner  # Install with uv (recommended)    uv venv -p &lt;Python version less than or equal to 3.13&gt; /path/to/your/choice/of/venv/directory    source /path/to/your/choice/of/venv/directory/bin/activate    uv pip install .  # Or install in development mode  uv pip install -e . |

To install directly from PyPI:

uv venv -p &lt;Python version less than or equal to 3.13&gt; /path/to/your/choice/of/venv/directory
source /path/to/your/choice/of/venv/directory/bin/activate
uv pip install cisco-ai-mcp-scanner

|  |  |
| --- | --- |
| 1  2  3 | uv venv -p &lt;Python version less than or equal to 3.13&gt; /path/to/your/choice/of/venv/directory  source /path/to/your/choice/of/venv/directory/bin/activate  uv pip install cisco-ai-mcp-scanner |

## Environment Configuration

Set the required environment variables before running scans. These examples come from the official repository and show the typical configuration for Cisco AI Defense and LLM integrations:

# Cisco AI Defense API (optional)
export MCP\_SCANNER\_API\_KEY="your\_cisco\_api\_key"
export MCP\_SCANNER\_ENDPOINT="https://us.api.inspect.aidefense.security.cisco.com/api/v1"
# AWS Bedrock Claude with AWS credentials (profile)
export AWS\_PROFILE="your-profile"
export AWS\_REGION="us-east-1"
export MCP\_SCANNER\_LLM\_MODEL="bedrock/anthropic.claude-sonnet-4-5-20250929-v2:0" # Any AWS Bedrock supported model
# AWS Bedrock Claude with API key (Bearer token)
export MCP\_SCANNER\_LLM\_API\_KEY="bedrock-api-key-..." # Generated via Amazon Bedrock -> API Keys
export AWS\_REGION="us-east-1"
export MCP\_SCANNER\_LLM\_MODEL="bedrock/us.anthropic.claude-sonnet-4-5-20250929-v2:0" # Any AWS Bedrock supported model
# LLM Provider API Key (required for LLM analyzer)
export MCP\_SCANNER\_LLM\_API\_KEY="your\_llm\_api\_key" # OpenAI
# LLM Model Configuration (optional - defaults provided)
export MCP\_SCANNER\_LLM\_MODEL="gpt-4o" # Any LiteLLM-supported model
export MCP\_SCANNER\_LLM\_BASE\_URL="https://api.openai.com/v1" # Custom LLM endpoint
export MCP\_SCANNER\_LLM\_API\_VERSION="2024-02-01" # API version (if required)
# For Azure OpenAI (example)
export MCP\_SCANNER\_LLM\_BASE\_URL="https://your-resource.openai.azure.com/"
export MCP\_SCANNER\_LLM\_API\_VERSION="2024-02-01"
export MCP\_SCANNER\_LLM\_MODEL="azure/gpt-4"
# For Extended Thinking Models (longer timeout)
export MCP\_SCANNER\_LLM\_TIMEOUT=300

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29 | # Cisco AI Defense API (optional)  export MCP\_SCANNER\_API\_KEY="your\_cisco\_api\_key"  export MCP\_SCANNER\_ENDPOINT="https://us.api.inspect.aidefense.security.cisco.com/api/v1"    # AWS Bedrock Claude with AWS credentials (profile)  export AWS\_PROFILE="your-profile"  export AWS\_REGION="us-east-1"  export MCP\_SCANNER\_LLM\_MODEL="bedrock/anthropic.claude-sonnet-4-5-20250929-v2:0" # Any AWS Bedrock supported model    # AWS Bedrock Claude with API key (Bearer token)  export MCP\_SCANNER\_LLM\_API\_KEY="bedrock-api-key-..." # Generated via Amazon Bedrock -> API Keys  export AWS\_REGION="us-east-1"  export MCP\_SCANNER\_LLM\_MODEL="bedrock/us.anthropic.claude-sonnet-4-5-20250929-v2:0" # Any AWS Bedrock supported model    # LLM Provider API Key (required for LLM analyzer)  export MCP\_SCANNER\_LLM\_API\_KEY="your\_llm\_api\_key"  # OpenAI    # LLM Model Configuration (optional - defaults provided)  export MCP\_SCANNER\_LLM\_MODEL="gpt-4o"  # Any LiteLLM-supported model  export MCP\_SCANNER\_LLM\_BASE\_URL="https://api.openai.com/v1"  # Custom LLM endpoint  export MCP\_SCANNER\_LLM\_API\_VERSION="2024-02-01"  # API version (if required)    # For Azure OpenAI (example)  export MCP\_SCANNER\_LLM\_BASE\_URL="https://your-resource.openai.azure.com/"  export MCP\_SCANNER\_LLM\_API\_VERSION="2024-02-01"  export MCP\_SCANNER\_LLM\_MODEL="azure/gpt-4"    # For Extended Thinking Models (longer timeout)  export MCP\_SCANNER\_LLM\_TIMEOUT=300 |

Adjust these values to match your environment or local LLM endpoint before running `mcp-scan`. The tool supports OpenAI, Azure OpenAI, AWS Bedrock, and local backends such as Ollama or vLLM.

## Usage

mcp-scanner ...