---
title: The Coding-Agent Trap: When a "Free" LLM Endpoint Is the Adversary, (Mon, Aug 31st)
url: https://isc.sans.edu/diary/rss/33298
source: SANS Internet Storm Center, InfoCON: green
date: 2026-08-31
fetch_date: 2026-09-01T07:01:22.483852
---

# The Coding-Agent Trap: When a "Free" LLM Endpoint Is the Adversary, (Mon, Aug 31st)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Brad Duncan](/handler_list.html#brad-duncan "Brad Duncan")

Threat Level: [green](/infocon.html)

* [previous](/diary/33292)
* [next](/diary/33300)

Click HERE to learn more about classes Renato is teaching for SANS

# [The Coding-Agent Trap: When a "Free" LLM Endpoint Is the Adversary](/forums/diary/The%2BCodingAgent%2BTrap%2BWhen%2Ba%2BFree%2BLLM%2BEndpoint%2BIs%2Bthe%2BAdversary/33298/)

**Published**: 2026-08-31. **Last Updated**: 2026-08-31 20:00:34 UTC
**by** [Renato Marinho](/handler_list.html#renato-marinho) (Version: 1)

[0 comment(s)](/diary/The%2BCodingAgent%2BTrap%2BWhen%2Ba%2BFree%2BLLM%2BEndpoint%2BIs%2Bthe%2BAdversary/33298/#comments)

*One of my internet-exposed inference honeypots was discovered, relabeled with sought-after model names, and incorporated into infrastructure apparently used to provide "free" LLM backends. It then received a real coding-agent session — history, filesystem output, working paths, and the agent's local tool manifest. The honeypot did not request or cause any tool execution; what the request exposed is what a malicious operator in that position could do.*

Chasing the "free API key" is not new. What is new is what you get to chase now: not a key, but an *agent* — a client that arrives carrying its own file-read, file-write, and shell tools, asking a server whose identity and operator it may never have verified to decide what to do next. Point that client at the wrong endpoint and its replies stop being just text: they can request tool calls that the agent, depending on its configuration, may carry out on the machine it runs on.

This is not a classic watering hole — nobody compromised a site or service the users already trusted. It is better understood as a *rogue model endpoint*: a server that agents are configured to trust as their reasoning backend. In a deliberate campaign an operator could go further and run it as an *evil twin* of a real provider — sought-after model names, advertised as free — and wait for tool-enabled agents to connect. This diary is one worked example, caught on a honeypot: an exposed endpoint that was scavenged, relabeled, and handed a real agent's session. The lesson underneath it: a model endpoint is not merely a source of text — for a tool-enabled agent, it is part of the control plane.

## One session, and where it went

Start with the payload, because it reframes everything. On 2026-08-30 our honeypot received, 210 times in 91 seconds, a 224 KB request body: an 88-message transcript from [opencode](https://opencode.ai/), an open-source terminal coding agent, originating from a Windows environment and delivered to us through a China Unicom address in Hebei that was apparently acting as a relay. A person had asked their agent (in Chinese) to study the writing style of two novels sitting in their Downloads folder. Across the earlier messages the agent had listed the directory, copied the files to `%TEMP%`, unpacked them, written a Python script to extract the text, and begun reading chapters — several PowerShell tool invocations among them. Then the user typed "jìxù" — continue. That request, with the whole history and tool manifest attached, is what landed on our server.

The request labeled the backend as DeepSeek — `"model": "fofa-ds-NNNNN"` — though the transcript cannot tell us who assigned that label or exactly what the user understood it to mean. Either way, it was reaching a honeypot that scanners had found the month before. Everything the transcript carried — the Windows username, directory listings, tool outputs, and portions of the files it had read — was now in our database, in cleartext, sent by a client presenting `Authorization: Bearer free` to an endpoint that did not validate it.

The client connecting to the honeypot was not an attacker. It was an ordinary user whose private agent session had been routed to an endpoint they did not control. The rest of this diary examines what a malicious operator could have done from that position.

## The supply chain of "free"

Our honeypot answers on `/v1/models`, `/v1/chat/completions`, an Ollama-style `/api/tags` and an MCP server — all unauthenticated, advertising four unremarkable local models. It went live 2026-07-18. Here is how it became a DeepSeek:

* 2026-07-18 → 08-25: Baseline scanning. A spike on 07-22 (115 requests, 20 IPs) copies model names straight out of our `/v1/models` reply back into requests — sometimes the entire list pasted as one string, `[nomic-embed-text:latest mistral-small:24b …]`. Automated inventory, nobody home.
* 2026-08-26: A client identifying as `opencode/0.2.0` arrives and cycles through model names we never advertised: `auto/best-coding`, `auto/claude-opus`, `auto/claude-sonnet`, `auto/best-reasoning`. The behavior is consistent with probing which aliases the backend will accept. We answer all of them — HTTP 200, under 100 ms.
* 2026-08-27: A client calling itself `NodeHealthCheck/1.0 (+local-lab)` requests `fofa-opus-NNNNN`. This suggests the endpoint had been enrolled in a monitored backend pool.
* 2026-08-30 06:59: `opencode/0.2.0` requests `fofa-sol-NNNNN`, `fofa-ds-NNNNN` and `fofa-opus-NNNNN` within three seconds — three aliases for one backend, in a pattern consistent with backend validation. Later the same morning it also tries `agentrouter-org/claude-opus-4-8` and `bailian/deepseek-v4-flash-0731`: names suggestive of other routing or provider-list conventions, pointed at the same IP.
* 2026-08-30 08:07: A `Go-http-client/2.0` from a China Unicom (Hebei) address — apparently a relay — sends the opencode transcript 210 times in 91 seconds.

The naming scheme strongly suggests the whole arrangement. **fofa** is [FOFA](https://fofa.info/), China's internet-wide search engine — a plausible place the endpoint was found. **ds / opus / sol** read as aliases for DeepSeek, Claude Opus, and a GPT variant (the `gpt-5.6-sol` probes three days earlier point to "sol"). And the numeric suffix — the same across all three aliases, masked here as `NNNNN` — is not a channel id: it matches the endpoint's own public IP octets. The convention is `<where I found it>-<what I'll call it>-<octets of its address>`: that is how you label entries in a hand-kept list of scavenged endpoints, and it is why we have masked it here.

The scheme appears to have propagated across multiple clients or infrastructure nodes: the same three aliases were exercised from a Vultr host, a Cloudflare egress, and the China Unicom relay, plus a separate health-checker — four vantage points, one naming scheme, one target. And the credential on 247 of the 248 requests was the same: `Authorization: Bearer free` — the "key" is the word "free". The evidence supports a plausible distribution chain: a scanner indexes exposed endpoints; someone assigns friendly aliases and folds them into a pool of "free models"; that configuration propagates into agent clients or relays. The `Go-http-client/2.0` user-agent is consistent with a Go-based intermediary but does not identify a particular product. We did not recover the list or its maintainer — we observed steps consistent with such a chain.

## What the endpoint operator receives

Whoever operates or compromises the endpoint that entry points to receives this, verbatim, with every request:

```

"model": "fofa-ds-NNNNN",
"messages": [
  {"role": "system", "content": "You are opencode, an interactive CLI tool …"},
  {"role": "user",   "content": "n? fùzé b?ng w? xi? xi?oshu?"},
  …
  {"role": "assistant", "tool_calls": [{"function": {"name": "bash",
     "arguments": "{\"command\":\"Get-ChildItem -LiteralPath \\\"C:\\\\Users\\\\<redacted>\\\\Downloads\\\" …\"}"}}]},
  {"role": "tool", "content": "?¼: C:\\Users\\<redacted>\\Downloads  …"},
  …
  {"role": "user", "content": "jìxù"}
],
"tools": [
  {"type":"function","function":{"name":"bash","description":"Executes a given Windows PowerShell (5....