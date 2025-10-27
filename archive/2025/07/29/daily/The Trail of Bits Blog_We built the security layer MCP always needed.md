---
title: We built the security layer MCP always needed
url: https://blog.trailofbits.com/2025/07/28/we-built-the-security-layer-mcp-always-needed/
source: The Trail of Bits Blog
date: 2025-07-29
fetch_date: 2025-10-06T23:52:18.016403
---

# We built the security layer MCP always needed

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# We built the security layer MCP always needed

Cliff Smith

July 28, 2025

[machine-learning](/categories/machine-learning/), [mcp](/categories/mcp/), [tool-release](/categories/tool-release/)

Page content

* [Defending the LLM’s context window](#defending-the-llms-context-window)
* [Designing mcp-context-protector for compatibility and reliability with a wrapper server](#designing-mcp-context-protector-for-compatibility-and-reliability-with-a-wrapper-server)
* [Wrappers versus SDK updates and the Extended Tool Definition Interface](#wrappers-versus-sdk-updates-and-the-extended-tool-definition-interface)
* [Security features of mcp-context-protector](#security-features-of-mcp-context-protector)
  + [Trust-on-first-use server pinning](#trust-on-first-use-server-pinning)
  + [LLM guardrail scanning of tool responses](#llm-guardrail-scanning-of-tool-responses)
  + [Sanitizing ANSI control sequences](#sanitizing-ansi-control-sequences)
* [Limitations on chain-of-thought auditing](#limitations-on-chain-of-thought-auditing)
* [Manual configuration review and alert fatigue](#manual-configuration-review-and-alert-fatigue)
* [Adopting mcp-context-protector in your organization](#adopting-mcp-context-protector-in-your-organization)

Today we’re announcing the beta release of [`mcp-context-protector`](https://github.com/trailofbits/mcp-context-protector), a security wrapper for LLM apps using the Model Context Protocol (MCP). It defends against the [line jumping attacks](https://blog.trailofbits.com/2025/04/21/jumping-the-line-how-mcp-servers-can-attack-you-before-you-ever-use-them/) documented earlier in this blog series, such as prompt injection via [tool descriptions](https://blog.trailofbits.com/2025/04/23/how-mcp-servers-can-steal-your-conversation-history/) and [ANSI terminal escape codes](https://blog.trailofbits.com/2025/04/29/deceiving-users-with-ansi-terminal-codes-in-mcp/), through features designed to help expose malicious server behavior:

* Trust-on-first-use pinning for server instructions and tool descriptions
* LLM guardrail integration to scan tool descriptions and server instructions for prompt injection payloads
* Optional sanitization of ANSI control characters

The [data exfiltration](https://blog.trailofbits.com/2025/04/23/how-mcp-servers-can-steal-your-conversation-history/) and [code execution attacks](https://blog.trailofbits.com/2025/04/21/jumping-the-line-how-mcp-servers-can-attack-you-before-you-ever-use-them/) from our previous posts must now contend with additional security layers, including more strongly enforced human-in-the-loop controls. `mcp-context-protector` is implemented as a wrapper that proxies tool calls and other operations to the downstream server, making it compatible with any MCP server and any MCP-compliant host app.

## Defending the LLM’s context window

In conducting a [line jumping](https://blog.trailofbits.com/2025/04/21/jumping-the-line-how-mcp-servers-can-attack-you-before-you-ever-use-them/) attack, an MCP server includes a prompt injection payload in a tool description, server instructions, or other fields that tell the model how to interact with the server. With this technique, attackers can manipulate the model’s behavior before any malicious tools have been invoked, bypassing the human-in-the-loop controls built into MCP. In other words, line jumping does not rely on getting the model to call a malicious tool; **it attacks the model’s context window directly**, even if the malicious server’s tools are never called.

This observation has an important implication for how we defend against these attacks. Security controls should be deployed at the trust boundary where the risk materializes, and in the attacks we’ve been examining, the risk exists between the MCP server’s descriptions and the model’s context window. Therefore, there should be a security control that makes it harder for malicious MCP servers to inject harmful text into the context window through tool descriptions.

## Designing mcp-context-protector for compatibility and reliability with a wrapper server

We built [`mcp-context-protector`](https://github.com/trailofbits/mcp-context-protector) as a wrapper that is installed directly into the LLM app and acts as a proxy between the app and the downstream server.

![Flowchart depicting mcp-context-protector’s architecture](/img/mcp4_figure_1.png)

Figure 1: mcp-context-protector architecture

This is our preferred solution to protecting an LLM’s context window. By sitting between the LLM and the downstream server, the wrapper can perform security checks on every single message before it enters the context window.

Other approaches, such as using an external code scanner, would not offer the same protection. A configuration scanner like the `inspect` mode of Invariant Labs’ [`mcp-scan`](https://github.com/invariantlabs-ai/mcp-scan/) might detect prompt injection attacks or other signs of malice in the first installed version of an MCP server, but it wouldn’t detect any that show up after a software update. Enforcing code scanning and manual approval for all updates would be a big undertaking, especially since MCP servers can be downloaded and updated through any package management tool. Another option is to rely on a commercially hosted server registry and trust that the registry’s review processes will ensure that no dangerous tools are available for download, but there is no standardized (or even conventional) process for how these registries review code or what attacks they look for.

With a security tool sitting between the LLM app and the untrusted MCP server, every communication can be checked for potential problems before any potentially dangerous content is presented to the model. In addition to being the most reliable security architecture, this approach also ensures universal compatibility. Since `mcp-context-protector` communicates over the same protocol as every MCP server, any app that uses MCP can use `mcp-context-protector` without modifications or extra plugins.

In this way, `mcp-context-protector` serves a similar purpose to `mcp-scan`’s `proxy` mode. One difference is that `mcp-scan`’s proxy requires the user to launch a separate process, whereas `mcp-context-protector` is “set it and forget it.” Once an MCP client is configured to connect to a server through the wrapper, `mcp-context-protector` will remain in place for good.

## Wrappers versus SDK updates and the Extended Tool Definition Interface

While we were building `mcp-context-protector`, an independent team of engineers were working on the Extended Tool Definition Interface (ETDI), a revision to the MCP specification and SDKs that address some of the same concerns as `mcp-context-protector`. But while their goals are quite similar, the two tools use vastly different methodologies to achieve those goals. Whereas `mcp-context-protector` is designed for universal compatibility and ease of installation, properly implementing ETDI requires the developers and distributors of LLM apps and MCP servers to update their workflows. For example, ETDI uses OAuth signatures to ensure the consistency and authenticity of server configurations, which requires key management infrastructure that is not required of MCP servers today.

We encourage you to read the [ETDI paper](https://arxiv.org/abs/2504.08623) and follow along with development of the [Python SDK’s ETDI implementation](https://github.com/modelcontextprotocol/python-sdk/pull/845). If widely adopted across the ecosystem, ETDI could represent a robust and sustainable solution to some of MCP’s security issues. For now, `mcp-context-protector` can provide similar security guarantees in a lightweight, universally compatible wrapper that does not require any changes to the MCP server or the LLM app.

## Security features of mcp-context-protec...