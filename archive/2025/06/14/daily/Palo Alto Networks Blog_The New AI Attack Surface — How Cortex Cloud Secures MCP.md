---
title: The New AI Attack Surface — How Cortex Cloud Secures MCP
url: https://www.paloaltonetworks.com/blog/2025/06/cloud-security-model-context-protocol-mcp-security/
source: Palo Alto Networks Blog
date: 2025-06-14
fetch_date: 2025-10-06T22:56:51.082586
---

# The New AI Attack Surface — How Cortex Cloud Secures MCP

* [Blog](https://www.paloaltonetworks.com/blog)
* [Palo Alto Networks](https://www.paloaltonetworks.com/blog/corporate)
* [AI Security](https://www.paloaltonetworks.com/blog/category/ai-security/)
* The New AI Attack Surface...

# The New AI Attack Surface — How Cortex Cloud Secures MCP

Link copied

By [Ory Segal](/blog/author/ory-segal/ "Posts by Ory Segal"), [Aviv Sasson](/blog/author/aviv-sasson/ "Posts by Aviv Sasson") and [Elad Shuster](/blog/author/elad-shuster/ "Posts by Elad Shuster")

Jun 13, 2025

7 minutes

[AI Security](/blog/category/ai-security/)

[AI Security Posture Management](/blog/cloud-security/category/ai-security-posture-management/)

[AI](/blog/tag/ai/)

[Cortex Cloud](/blog/tag/cortex-cloud/)

[MCP Server](/blog/tag/mcp-server/)

[Real-Time Security](/blog/tag/real-time-security/)

[WAAS](/blog/tag/waas/)

With remarkable momentum behind its adoption, the Model Context Protocol (MCP) is quickly becoming the de facto interface for connecting large language models (LLMs) to tools, APIs, databases and other services. Think of it as the USB-C of AI development – an elegant, standardized bridge that enables dynamic interaction between AI models and external environments. Major AI platforms, like ChatGPT, Gemini and Claude, already rely on it. (MCP is in fact [Anthropic's creation](https://www.anthropic.com/news/model-context-protocol), a solution designed for Claude Desktop).

Like anything, though, as MCP adoption accelerates, so does the risk. Because MCP connects models to powerful systems and sensitive data in real time, it creates new attack surfaces that conventional security tools weren’t designed to handle.

To meet this challenge, we’ve built MCP Security to safeguard AI communications at their source.

## MCP — An Operational Framework

The Model Context Protocol follows a client-server architecture that defines how AI applications communicate with tools, services and data sources in real time. It’s not just a bridge; it’s an operational framework that allows LLMs to interact with external environments in structured, context-rich ways.

MCP deployments typically include the following components:

* **MCP Hosts –** Applications, such as Claude Desktop, IDEs or AI assistants, that initiate data access through MCP.
* **MCP Clients –** Components that manage and maintain persistent connections to servers.
* **MCP Servers –** Lightweight services that expose capabilities through the standardized protocol.
* **Local Data Sources –** Files, databases and services that MCP servers can access within the local environment.
* **Remote Services –** External APIs and internet-connected systems reachable through the protocol.

Unlike traditional APIs, MCP supports complex context structures. Applications can:

* Pass rich, structured information with each request.
* Expose live data and content to LLMs as “Resources.”
* Reuse prompt templates called “Prompts.”
* Enable models to take defined actions through “Tools.”
* Request completions through a mechanism called “Sampling.”

![The traditional approach to AI applications and the MCP approach to AI applications.](/blog/wp-content/uploads/2025/06/word-image-340593-1.png)

MCP creates a standardized bridge between AI application and external services.

MCP's architecture is designed for the kind of flexible, dynamic integrations that next-generation AI applications require. While adoption is still in early stages, the protocol's potential impact on how AI systems access external resources makes it worth security teams' attention.

## The Emerging MCP Attack Surface

MCP enables AI applications to access the same tools and data that human users rely on – email systems, customer databases, file shares and internal APIs. While this creates powerful capabilities, it also means that AI applications inherit the same access privileges as their users.

Consider common use cases. An AI assistant helping with customer support might need read access to CRM data, or a development copilot might access code repositories and deployment tools. These aren't necessarily “sensitive systems” by design, but they contain business-critical information that requires protection, which creates new security considerations. When AI models can dynamically access multiple systems through MCP, several risk categories emerge.

### Protocol Design Vulnerabilities

Because MCP is a relatively new protocol, implementations can vary in their security approaches. For example, some MCP servers might include sensitive session information directly in web addresses where it could be logged or cached. Others might use different authentication methods that don't consistently verify who is making requests.

Perhaps the most concerning aspect is how MCP servers don't always validate the data they receive before processing it. This means an attacker could potentially send malicious commands disguised as legitimate MCP requests – similar to how SQL injection attacks work against databases but targeting the AI communication layer.

### Centralized Credential Risk

MCP servers often store access tokens for multiple systems. A single compromise can grant attackers lateral access to a wide range of services.

### Tool Poisoning Attacks

Attackers can embed hidden prompts or instructions in tool metadata. Although invisible to users, LLMs may interpret these as commands, triggering data exfiltration or unauthorized actions.

### Multiserver Conflicts

In environments with multiple MCP servers, organizations risk prompt hijacking, tool name collisions and uncoordinated server behavior that introduces unpredictable vulnerabilities.

### Implementation Level Flaws

Poorly implemented MCP servers often contain command injection flaws, improperly evaluate user input, or lack isolation between processes. These issues can enable privilege escalation and lateral movement.

The bottom line? MCP changes how models interact with the broader environment, but also introduces a dynamic, high-risk surface. The security challenges are particularly concerning because MCP facilitates communication between powerful AI models and sensitive systems, potentially enabling sophisticated attack vectors that traditional security tools aren't designed to detect.

## MCP Security in Cortex Cloud WAAS

At Palo Alto Networks, we're committed to securing the technologies that drive innovation. Our new MCP Security capability in Cortex Cloud WAAS addresses the unique risks inherent to MCP communications. The feature provides two critical lines of defense.

### 1. Intelligent Protocol Validation

The WAAS protocol validation engine identifies and inspects MCP communications within general API traffic. It verifies structure against expected patterns, detects manipulation of protocol elements, and detects injection attempts aimed at protocol parsing. While MCP allows for implementation flexibility, the engine adapts to legitimate variations and enforces consistency across requests.

### 2. API-Based Attack Detection

WAAS also detects API-layer attacks targeting MCP endpoints. These include parameter tampering and other [Layer 7](/cyberpedia/what-is-layer-7) threats. Protections align with the OWASP API Security Top 10 to prevent misuse even when requests are well formed.

## Security Recommendations for MCP Builders

Teams adopting or building on MCP can reduce their risks by implementing these best practices:

* **Use Strong Access Controls** – Apply least-privilege to every MCP tool and server.
* **Protect Credentials** – Avoid hardcoding credentials, rotate keys regularly and isolate secrets.
* **Isolate Runtime Environments** – Run MCP servers in isolated containers or sandboxed environments to prevent lateral movement if a server is compromised.
* **Enable Detailed Logging** – Capture full MCP operations logs for anomaly detection.
* **Validate Server Identities** – Ensure connections go to trusted MCP implementations.
* **Require Confirmation for Sensitive Action...