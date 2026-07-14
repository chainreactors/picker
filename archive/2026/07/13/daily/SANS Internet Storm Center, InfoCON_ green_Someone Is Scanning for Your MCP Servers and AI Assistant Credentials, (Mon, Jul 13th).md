---
title: Someone Is Scanning for Your MCP Servers and AI Assistant Credentials, (Mon, Jul 13th)
url: https://isc.sans.edu/diary/rss/33150
source: SANS Internet Storm Center, InfoCON: green
date: 2026-07-13
fetch_date: 2026-07-14T04:48:16.431047
---

# Someone Is Scanning for Your MCP Servers and AI Assistant Credentials, (Mon, Jul 13th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Manuel Humberto Santander Pelaez](/handler_list.html#manuel-humberto-santander-pelaez "Manuel Humberto Santander Pelaez")

Threat Level: [green](/infocon.html)

* [previous](/diary/33146)

Click HERE to learn more about classes Manuel Humberto is teaching for SANS

# [Someone Is Scanning for Your MCP Servers and AI Assistant Credentials](/forums/diary/Someone%2BIs%2BScanning%2Bfor%2BYour%2BMCP%2BServers%2Band%2BAI%2BAssistant%2BCredentials/33150/)

**Published**: 2026-07-13. **Last Updated**: 2026-07-13 04:22:02 UTC
**by** [Manuel Humberto Santander Pelaez](/handler_list.html#manuel-humberto-santander-pelaez) (Version: 1)

[0 comment(s)](/diary/Someone%2BIs%2BScanning%2Bfor%2BYour%2BMCP%2BServers%2Band%2BAI%2BAssistant%2BCredentials/33150/#comments)

# **The setup**

I pulled 14 days of Apache and ModSecurity logs from a single small web host. Nothing special about it. A handful of low-traffic virtual hosts. A WordPress site, a couple of custom application backends, a static devotional site. The kind of server that exists by the millions and that nobody would call a high-value target. Server IP and hostnames are anonymized throughout this diary.

The point of looking was not to find a breach. It was to see what the background radiation of internet scanning looks like in 2026. Most of it is exactly what you would expect. WordPress xmlrpc floods. Endless .env probing. Git config fishing. But mixed into the noise was a category of scanning I had not seen documented before. Someone is systematically looking for Model Context Protocol servers, AI assistant configuration files, and locally exposed LLM endpoints. On a server that runs none of those things.

# **The overall picture**

Figure 1 breaks down the reconnaissance categories that ModSecurity flagged over the two-week window. I split them into two groups. The classic cloud and application recon that every server sees, and the newer AI-agent recon that is the subject of this diary.

![Categories](https://isc.sans.edu/diaryimages/images/fig1cat.png)???????

Spring Boot Actuator scanning dominates by request volume. That is not new. The full set of actuator endpoints including /actuator/heapdump and /actuator/env gets hit hundreds of times from dozens of sources. The interesting part is the group below it. MCP handshakes, LLM API probes, AI assistant secret fishing, and MCP config files together account for roughly 200 requests. And the MCP protocol handshake category came from 49 distinct source IPs, more spread than any other category in the dataset. This is not one researcher. It is a broad, distributed scan.

# **The Part That Stood Out: A Real MCP Handshake**

Most scanning is dumb. A bot requests a path, checks the status code, moves on. The POST /mcp probes were different. Every one of them carried a valid JSON-RPC 2.0 body performing a Model Context Protocol initialize call.

POST /mcp HTTP/1.1
Content-Type: application/json

{"id":1,"jsonrpc":"2.0","method":"initialize",
 "params":{"capabilities":{},
  "clientInfo":{"name":"client","version":"0"},
  "protocolVersion":"2025-03-26"}}

This matters. The scanner is not blindly requesting a URL. It is speaking the protocol. It sends a correctly formed handshake with a real MCP protocol version and waits to see if something on the other end answers like an MCP server. If your server responds to that initialize call then the next steps are to enumerate the tools the server exposes, the data sources it connects to, and whatever it can be convinced to do. Figure 2 shows the flow.

![Flow](https://isc.sans.edu/diaryimages/images/fig2post.png)

For readers who have not deployed one yet: an MCP server is the bridge that lets an AI agent call tools and read data sources. It is the thing that gives a model access to your database, your file system, your ticketing system, your internal APIs. An exposed and unauthenticated MCP server is close to the worst case. It is a remote, machine-readable menu of everything an agent can touch, offered to anyone who completes the handshake. The scanners clearly know this and are looking for them at internet scale.

# **Fishing for AI Assistant Configs and Credentials**

Alongside the live-server handshakes, the scanners fished aggressively for configuration and credential files belonging to AI coding assistants. These are the files that tools like Claude and Cursor write to a project or home directory. When developers accidentally deploy them to a web root, they leak.

The paths requested were specific and current. Not guesses. Someone built this wordlist recently and from real knowledge of how these tools store their settings.

GET  /.claude/mcp.json
GET  /.cursor/mcp.json
GET  /.cursor/mcp\_config.json
GET  /.vscode/mcp.json
GET  /.mcp/config.json
GET  /.claude/settings.local.json
HEAD /.claude/.credentials.json
HEAD /.config/claude/.credentials.json

The use of HEAD for the credential files is a tell. HEAD returns headers without a body. The scanner is checking whether the file exists before spending bandwidth to download it. That is an efficiency optimization you build when you are scanning a very large number of hosts and expect most to be misses. It signals a mature, wide campaign rather than a one-off curiosity probe.

The same run also fished for cloud credential files across every major provider. Figure 3 shows the spread. Generic credentials.json, then GCP, AWS, and Azure specific variants, then Kubernetes and application-specific names. The AI assistant credentials sit inside this same wordlist, which tells you the tooling authors now treat AI assistant secrets as just another cloud credential worth harvesting.

# ![Credentials](https://isc.sans.edu/diaryimages/images/fig3credential.png) **Looking for Unauthenticated LLM Endpoints**

The third strand was probing for exposed LLM inference endpoints. Two signatures dominated.

* GET /v1/models is the OpenAI-compatible model-listing endpoint. Dozens of self-hosted inference servers expose it. If it answers without authentication then the host is running a model that anyone can query, which means free compute for the attacker and a potential pivot point.
* GET /api/tags is the Ollama endpoint that lists locally installed models. Ollama binds to localhost by default but is very commonly exposed to the network by accident. A response here is a strong signal of an unauthenticated local LLM.

Neither endpoint exists on the host I was looking at. Both were requested repeatedly from multiple sources. The scanners are casting a wide net for anyone who stood up a local model and forgot to put it behind authentication.

# **The Classic That Rode Along: Cloud Metadata SSRF**

Bundled with the AI-agent recon was a familiar technique that pairs naturally with it. SSRF attempts targeting the cloud metadata service to steal instance credentials.

GET /fetch?url=http://metadata.google.internal/...token
GET /fetch?uri=http://metadata.google.internal/...token
GET /fetch?path=http://metadata.google.internal/...token
GET /fetch?dest=http://metadata.google.internal/...token

The scanner rotates the parameter name across url, uri, path, and dest. It is looking for any proxy or fetch endpoint that will follow a supplied URL. The target is the GCP metadata endpoint that returns a service-account token. This is worth flagging in the AI context because agent and LLM tooling frequently includes fetch-style helpers that take a URL and retrieve it. That is exactly the kind of endpoint this probe is built to find. An MCP server or an agent tool that fetches arbitrary URLs is a ready-made SSRF primitive.

# **What to Check on Your Own Hosts**

Concrete things to look for in your own logs and infrastructure.

* Grep for the MCP handshake. Search access logs for POST /mcp and /sse. If you do not run an MCP server, any such request is pure recon and a useful indicator to block. If you do run one, co...