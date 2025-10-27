---
title: Insecure credential storage plagues MCP
url: https://blog.trailofbits.com/2025/04/30/insecure-credential-storage-plagues-mcp/
source: The Trail of Bits Blog
date: 2025-05-01
fetch_date: 2025-10-06T22:25:26.228592
---

# Insecure credential storage plagues MCP

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Insecure credential storage plagues MCP

Keith Hoodlet

April 30, 2025

[machine-learning](/categories/machine-learning/), [MCP](/categories/mcp/), [vulnerabilities](/categories/vulnerabilities/)

Page content

* [Stealing long-term credentials stored by MCP servers](#stealing-long-term-credentials-stored-by-mcp-servers)
  + [Pathway 1: Insecure configuration files](#pathway-1-insecure-configuration-files)
  + [Pathway 2: Credentials leaked via chat logs](#pathway-2-credentials-leaked-via-chat-logs)
  + [Compounding the Risk: The Figma Example](#compounding-the-risk-the-figma-example)
* [The steps to safer credential handling](#the-steps-to-safer-credential-handling)

This fourth post in our series on Model Context Protocol (MCP) security examines a vulnerability distinct from the protocol-level weaknesses discussed in our previous posts: **many MCP environments store long-term API keys for third-party services in plaintext on the local filesystem, often with insecure, world-readable permissions.** Exploitation of this vulnerability could touch every system connected to your LLM app; the more powerful your MCP environment, the greater the risk of insecurely stored credentials.

This practice is widespread within the MCP ecosystem. We observed it in multiple MCP tools, from official servers connecting to [GitLab](https://github.com/modelcontextprotocol/servers/tree/main/src/gitlab), [Postgres](https://github.com/modelcontextprotocol/servers/tree/main/src/postgres), and [Google Maps](https://github.com/modelcontextprotocol/servers/tree/main/src/google-maps), to third-party tools like the [Figma connector](https://github.com/smithery-ai/mcp-figma/) and the [Superargs](https://github.com/supercorp-ai/superargs) wrapper. While these are only examples, they illustrate a concerning trend that leaves attackers one file disclosure vulnerability away from stealing your API keys and compromising the entirety of your data in the third-party service. There’s no need for complex exploits, and there are many different ways the attacker could read the API keys from your system:

* **Local malware:** User-level malware designed to steal information can scan predictable file paths (e.g., `~/Library/Application Support/`, `~/.config/`, or application logs) and exfiltrate discovered credentials.
* **Exploitation of other vulnerabilities:** Arbitrary file read vulnerabilities in *unrelated* software on the same system become direct pathways to stealing these plaintext secrets.
* **Multi-user systems:** On shared workstations or servers, other users with file system access could read credentials stored in world-readable files.
* **Cloud backups:** Automated backup tools may synchronize server configuration files to cloud storage, exposing them to the provider or even to other users if the backup storage system is misconfigured.

This post dissects the insecure ways MCP software handles credentials and the paths they provide attackers to your data. We also discuss the improved security practices that developers of both MCP servers and the third-party services they connect you to can apply to address these risks.

## Stealing long-term credentials stored by MCP servers

Because many MCP servers exist to connect an LLM to a third-party API, such as a knowledge management system or cloud infrastructure service, they often need credentials to read or modify data. To that end, MCP [integrated OAuth 2.1 in its March 2025 protocol revision](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization). If implemented correctly, OAuth’s token-based approach provides an easy and secure way for servers to obtain short-term credentials with a limited scope.

However, not every downstream service that users want to connect to their LLM supports OAuth, so many MCP tools require users to provide the server with API keys. These long-term credentials typically arrive at the MCP server through one of two pathways, both of which create vectors for credential theft:

### Pathway 1: Insecure configuration files

Most MCP servers obtain credentials via command-line arguments or environment variables, often sourced from configuration files managed by the host AI application. We observed this pattern with the official MCP servers for [Google Maps](https://github.com/modelcontextprotocol/servers/tree/main/src/google-maps), [Postgres](https://github.com/modelcontextprotocol/servers/tree/main/src/postgres), and [GitLab](https://github.com/modelcontextprotocol/servers/tree/main/src/gitlab).

The security risk emerges when the host application stores this configuration insecurely. For example, Claude Desktop creates a `claude_desktop_config.json` file in the user’s home directory. On macOS, we found this file has world-readable permissions:

```
$ ls -la ~/Library/Application\ Support/Claude\ Desktop/claude_desktop_config.json
-rw-r--r--  1 user  staff  2048 Apr 12 10:45 claude_desktop_config.json
```

This `-rw-r--r--` permission set allows **any process or user on the system** to read the file’s contents, including any plaintext API keys stored within, using standard file access operations. No special privileges are required.

### Pathway 2: Credentials leaked via chat logs

Another common pattern involves users inputting credentials directly into the AI chat interface, relying on the model to pass them to the appropriate MCP server. Supercorp’s [Superargs](https://github.com/supercorp-ai/superargs) wrapper explicitly facilitates this for servers that expect configuration information in arguments or environment variables.

This method presents two distinct risks. First, as detailed in our [previous post](https://blog.trailofbits.com/2025/04/23/how-mcp-servers-can-steal-your-conversation-history/), a malicious MCP server can simply steal the credentials directly from the conversation history. Second, the host AI application itself often logs the entire conversation history—including any embedded credentials—to local files for debugging or history features.

During our testing, we found applications like Cursor and Windsurf store these conversation logs with world-readable permissions:

```
$ ls -la ~/.cursor/logs/conversations/
-rw-r--r--  1 user  staff  15482 Apr 15 12:23 conversation_20240415.json
```

Similar to configuration files, these insecurely permissioned logs provide another easily accessible source of plaintext credentials for local attackers or malware.

### Compounding the Risk: The Figma Example

Some implementations expose credentials through both pathways simultaneously. The community-provided [MCP server for Figma](https://github.com/smithery-ai/mcp-figma/) allows users to set their API token via [a tool call](https://github.com/smithery-ai/mcp-figma/blob/main/src/index.ts#L467-L473). However, the server then [saves this credential](https://github.com/smithery-ai/mcp-figma/blob/main/src/utils/config.ts#L43C10-L43C11) to a configuration file in the user’s home directory using Node.js’s [`fs.writeFileSync`](https://nodejs.org/api/fs.html#fswritefilesyncfile-data-options) function. By default, this function creates files with `0666` permissions (`-rw-rw-rw-`), making the stored Figma token world-readable and, depending on the user’s umask setting, *world-writable* as well.

Writing to the configuration file enables attacks similar to [session fixation](https://owasp.org/www-community/attacks/Session_fixation), where the victim unknowingly logs into an attacker-controlled account. In the case of a design tool like Figma, the victim will likely save trade secrets or other private information in the account, immediately disclosing them to the attacker. If the downstream service is a bank or cryptocurrency exchange, the user could be tricked into depositing or transferring assets directly into the attacker’s accounts.

## The steps to sa...