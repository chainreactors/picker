---
title: The MCP AuthN/Z Nightmare
url: https://blog.doyensec.com/2026/03/05/mcp-nightmare.html
source: Over Security - Cybersecurity news aggregator
date: 2026-03-06
fetch_date: 2026-03-07T03:56:44.702697
---

# The MCP AuthN/Z Nightmare

[

](https://doyensec.com/img/home-video.mp4)

[![](/public/images/doyensec-logo.svg)](/index.html)

[![](/public/images/logo.svg)](/index.html)

#### ABOUT US

We are [**security engineers**](https://doyensec.com) who break bits and tell stories.

Visit us
[doyensec.com](https://doyensec.com)

Follow us
[@doyensec](https://twitter.com/doyensec)

Engage us
info@doyensec.com

#### Blog Archive

* 2026
* 2025
* 2024
* 2023
* 2022
* 2021
* 2020
* 2019
* 2018
* 2017

© 2026 [Doyensec LLC](https://doyensec.com) [![](/public/images/rss.png)](/atom.xml "RSS")

# The MCP AuthN/Z Nightmare

05 Mar 2026 - Posted by Francesco Lacerenza

![The MCP AuthN/Z Nightmare](../../../public/images/MCP-nightmare.png)

This article shares our perspective on the current state of authentication and authorization in enterprise-ready, remote MCP server deployments.

Before diving into that discussion, weâll first outline the most common attack vectors. Understanding these threats is essential to properly frame the security challenges that follow. If youâre already familiar with them, feel free to skip to the section [âEnterprise Authentication and Authorization: a Work in Progressâ](#enterprise-authentication-and-authorization-a-work-in-progress) below.

> Huge shoutout to [Teleport](https://goteleport.com/) for sponsoring this research. Thanks to their support, we have been able to conduct cutting-edge security research on this topic. Stay tuned for upcoming MCP security updates!

At this stage, introducing the **Model Context Protocol (MCP)** would be redundant since it has already been thoroughly covered in the recent surge of security blog posts.

For anyone who may have missed the conversation, hereâs a brief recap:

> MCP is a protocol used to connect AI models to: data, tools and prompts. It uses **JSON-RPC** messages for communication. Itâs a stateful connection where clients and servers negotiate capabilities.

A high-level architecture is provided below:

![](../../../public/images/MCP_basic.png)

References: [MCP Specification](https://modelcontextprotocol.io/specification/2025-11-25) and [MCP Architecture](https://modelcontextprotocol.io/specification/2025-11-25/architecture)

## MCP Attack Vectors

Several categories of vulnerabilities pertaining to MCP emerged in the wild. While it might not fit every bug you read about, as things are changing on a daily basis, a good starting point is the good and not-so-old [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/).

Below are the most relevant vulnerabilities we have encountered so far, organized by the malicious actor profile:

#### Malicious MCP Server

Rogue MCP servers could intentionally exploit clients with:

* **[Tool Poisoning](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)**: The server provides malicious tool definitions or modifies them after user approval. Sub-categories and variations of the attack:
  + *[Rug Pulls](https://invariantlabs.ai/blog/whatsapp-mcp-exploited)*: A server presents benign capabilities during initial `tools/list` call, then switches to malicious ones during execution or in subsequent MCP messages
  + *Tool Shadowing*: A malicious server injects tool descriptions that modify the agentâs behavior with respect to a trusted tool
  + *Schema Poisoning*: Corrupting interface definitions to mislead the model. The schema is used by MCP clients to validate the tool inputs and outputs and to let the model know what is required to interrogate them
* **[Prompt Injection via Tool Responses](https://owasp.org/www-project-mcp-top-10/2025/MCP06-2025%E2%80%93Intent-Flow-Subversion)**: The server returns malicious instructions embedded in MCP responses to normal actions, which the clientâs LLM then executes
* **[Data Exfiltration via Resources](https://owasp.org/www-project-mcp-top-10/2025/MCP06-2025%E2%80%93Intent-Flow-Subversion)**: Malicious servers exposing resources that leak sensitive client information etc.

It should be highlighted that the the listed attacks are exploitable by either local or remote MCP servers. Of course, the outcome varies drastrically in terms of achievable impacts.

#### Malicious MCP Client

Rogue MCP clients could intentionally exploit servers with:

* **[Command Injection](https://owasp.org/www-project-mcp-top-10/2025/MCP05-2025%E2%80%93Command-Injection%26Execution)**: Crafted MCP Message inputs sent to vulnerable MCP servers that do not properly sanitize - allowing arbitrary command execution (mostly in a old-fashioned way)
  + Examples: [`CVE-2025-53100`](https://github.com/RestDB/codehooks-mcp-server/security/advisories/GHSA-fhq6-jf5q-qxvq) (RestDBâs Codehooks.io MCP Server), [`CVE-2025-53818`](https://github.com/advisories/GHSA-6jx8-rcjx-vmwf) (GitHub Kanban MCP Server)
* **[Context Injection & Over-Sharing](https://owasp.org/www-project-mcp-top-10/2025/MCP10-2025%E2%80%93ContextInjection%26OverSharing)**: Servers that do not properly isolate context, allowing exfiltration of sensitive information from other users/sessions
* **[Prompt Injection](https://owasp.org/www-project-mcp-top-10/2025/MCP06-2025%E2%80%93Intent-Flow-Subversion)**: The MCP Server could receive malicious prompts from the client, which would then modify its behavior to execute the requested tasks

#### Other Malicious Actors

Beyond the traditional client-server factors, an MCP ecosystem could also be compromised by:

* **MCP Proxies/Gateways**: Intermediary systems (like MCP proxies) used for routing and authorization of MCP. These could alter passing MCP messages or simply be vulnerable to policy bypasses. You might be surprised by the number of [MCP Gateways out there](https://github.com/e2b-dev/awesome-mcp-gateways?tab=readme-ov-file)
* **Single-Sign-On (SSO) Intermediaries**: MCP servers using OAuth 2.0/2.1 for authorization rely on discovery endpoints (`.well-known/oauth-authorization-server`) and dynamic client registration. Malicious actors could exploit these intermediaries by injecting fake metadata, manipulating redirect URIs, or compromising the registration endpoint to obtain unauthorized client credentials (e.g., [`CVE-2025-4144`](https://github.com/cloudflare/workers-oauth-provider/pull/27) - a PKCE bypass in `workers-oauth-provider`, [`CVE-2025-4143`](https://github.com/cloudflare/workers-oauth-provider/pull/26) - improper `redirect_uri` validation)

## The Nightmare: New Actors, New Problems to Solve

Securing SSO remains an open challenge for the industry due to its intrinsic complexity. The past few years have highlighted this reality, with a steady stream of severe vulnerabilities affecting [OAuth2, OIDC](https://blog.doyensec.com/2025/01/30/oauth-common-vulnerabilities.html), SAML and [SCIM](https://blog.doyensec.com/2025/05/08/scim-hunting.html) implementations.

Yet, progress never stops and authentication & authorization in MCP are the new inevitable nightmare. Being a relatively new protocol, the standards for how clients and servers should establish trust are still evolving, leading to a fragmented ecosystem.

The specifications for AuthN/AuthZ are subject to continuous changes and extensions, as is common for newborn protocols. This instability means that todayâs âsecure and compliantâ implementation might be deprecated or insufficiently secure tomorrow.

> Just few of the latest Specification Enhancement Proposals (SEPs) in MCP

![Specification Enhancement Proposals (SEPs)](../../../public/images/seps.png)

Multiple significant issues have been emerging in the MCP SSO implementation, many as descendants of the common [OAuth2/OIDC vulnerabilities](https://blog.doyensec.com/2025/01/30/oauth-common-vulnerabilities.html), but also new ones.

We have seen browser-based clients or `open()` URL handlers exploited to launch arbitrary processes or redirect to malicious servers, showing the fragility of the MCP client-side implementation, often linked to automatic action executors.

Then, attacks against the...