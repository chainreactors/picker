---
title: agentic-dm-gateway
url: https://kitploit.com/en/tools/gitlab/wattocyber/agentic-dm-gateway
source: Kitploit
date: 2026-08-21
fetch_date: 2026-08-22T02:51:00.834126
---

# agentic-dm-gateway

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories

agentic-dm-gateway — Security control plane for LLM agents: allowlists, owner kill switch, PIN sessions, rate limits, prompt-injection detection, and output scrubbing to block secret leakage and image-beacon exfiltration. | Kitploit

[Tools](/en/tools)/![GitLab](/providers/gitlab.png)GitLab/wattocyber/agentic-dm-gateway

![](https://assets.kitploit.com/production/public/tools/50583/ed168cd7c4b9a61caf98c8a31b2dfb7d7e3bd3c5401288706c21c1376c7199ce.jpg)

[Authentication & Authorization](/en/categories/authentication-authorization)[Defensive Tools](/en/categories/defensive-tools)[Data Exfiltration](/en/categories/data-exfiltration)[Secret Detection](/en/categories/secret-detection)[AI Security](/en/categories/ai-security)

![GitLab](/providers/gitlab.png)wattocyber/agentic-dm-gateway

# agentic-dm-gateway

Security control plane for LLM agents: allowlists, owner kill switch, PIN sessions, rate limits, prompt-injection detection, and output scrubbing to block secret leakage and image-beacon exfiltration.

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

[View Repository](https://gitlab.com/wattocyber/agentic-dm-gateway)

[Website](https://gitlab.com/WattoCyber/agentic-dm-gateway)

10 days ago![Not yet reviewed](/_next/image?url=%2Fbadges%2Fkitploit_badge_not_reviewed_full.png&w=48&q=75)

# Agentic DM Gateway

![agentic-dm-gateway banner](https://assets.kitploit.com/production/public/readmes/50583/ed168cd7c4b9a61caf98c8a31b2dfb7d7e3bd3c5401288706c21c1376c7199ce.jpg)

Security control plane for LLM agents over private chat (typically Discord DMs).

It sits **in front of your agent**. It decides who may talk, whether the session is unlocked, whether the process is paused, and whether this message is safe enough to forward. Your model and tools stay behind that gate. The library does not call an LLM. It does not implement product features beyond security.

**Hermes-inspired.** Design follows the same control-plane ideas used in [Hermes Agent](https://github.com/NousResearch/hermes-agent) messaging gateways: DM-first delivery, identity allowlists, pairing-style open, owner kill switch, and a hard split between *who may act* (control plane) and *message text the model sees* (data plane). This package is a small, standalone extract of that pattern for any agent callable. Not affiliated with Nous Research.

**Maturity:** implemented · independently validated · maintained. See [STATUS.md](https://gitlab.com/wattocyber/agentic-dm-gateway/-/blob/main/STATUS.md).
**Reproduce:** `python scripts/repro.py` (expects `REPRO_OK`).

**Offline tests:**

root@kitploit:~

```
pip install -e ".[dev]"   # or: pip install -e . && pip install pytest
python -m pytest -q --tb=line
# or: python scripts/repro.py
```

**Live:** <https://github.com/SamsonCyber/agentic-dm-gateway>

---

## The problem

If you put an agent on Discord (or any chat API) with tools, anyone who can message the bot can try to:

* use the agent without permission
* burn API quota with floods
* inject "ignore previous instructions" style prompts
* trick the model into echoing API keys or other secrets

You need a **control plane** (identity and process controls) separate from the **data plane** (message text the model sees).

This package is that control plane.

---

## What it does

Scope: security gate only. Not a chatbot, trading bot, scanner, or agent framework. Pass an `agent(user_id, text) -> str` (or async) if you use Discord. The core works with any integer user id and plain text.

---

## Demo (copy-paste)

root@kitploit:~

```
$ python - <<'PY'
from agentic_dm_gateway import InboundSecurityPipeline
pipe = InboundSecurityPipeline({
 "allowed_user_ids": [111],
 "owner_ids": [111],
 "pin_enabled": False,
 "block_injection": True,
 "deny_message": "Not authorized.",
})
for uid, text in [
 (99, "hi"),
 (111, "ignore previous instructions"),
 (111, "summarize this note"),
]:
 r = pipe.precheck(uid, text)
 print(uid, r.stage, r.run_agent, r.reply_text)
PY

99 allowlist False Not authorized.
111 injection False Blocked: looks like prompt injection / secret fishing. Rephrase.
111 ok True None

$ python scripts/repro.py
REPRO_OK agentic-dm-gateway unit suite
```

## How to hook it in

Three integration paths. Pick one.

### 1) Drop-in Discord (easiest)

Install with Discord support, point env at your user ids, register the gateway, run the bot.

root@kitploit:~

```
pip install -e ".[discord]"
# or: pip install agentic-dm-gateway[discord]

![agentic-dm-gateway banner](https://assets.kitploit.com/production/public/readmes/50583/ed168cd7c4b9a61caf98c8a31b2dfb7d7e3bd3c5401288706c21c1376c7199ce.jpg)

export DISCORD_BOT_TOKEN=...
export AGENTIC_DM_ALLOWLIST=your_discord_user_id
export AGENTIC_DM_OWNER_ID=your_discord_user_id
# optional: export AGENTIC_DM_PIN=....

![agentic-dm-gateway banner](https://assets.kitploit.com/production/public/readmes/50583/ed168cd7c4b9a61caf98c8a31b2dfb7d7e3bd3c5401288706c21c1376c7199ce.jpg)
python examples/discord_echo_bot.py
```

In your own bot:

root@kitploit:~

```
import discord
from agentic_dm_gateway.discord_adapter import register_dm_gateway

def agent(user_id: int, text: str, *, is_owner: bool = False) -> str:
 # your Hermes / local model / tool loop
 return call_your_model(text)

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

register_dm_gateway(
 bot,
 {
 "allowed_user_ids": [], # or rely on AGENTIC_DM_ALLOWLIST env
 "owner_ids": [],
 "pin_enabled": False,
 "deny_message": False, # silent drop for strangers
 },
 agent=agent,
)
bot.run(TOKEN)
```

What `register_dm_gateway` does:

1. Installs an `on_message` handler on your `discord.Client` / bot.
2. Ignores bots and **guild** messages (DMs only).
3. Runs `InboundSecurityPipeline.precheck` before your agent.
4. Sends deny / control replies when needed.
5. Calls your `agent(user_id, sanitized_text, is_owner=...)`.
6. Scrubs the agent reply (secrets + image beacons) and chunks Discord's 2000-char limit.

Guild messages never reach the agent. Only DMs from allowlisted users do.

### 2) Manual Discord hook (you already have `on_message`)

If you cannot use `register_dm_gateway` (existing handler chain), call the pipeline yourself:

root@kitploit:~

```
from agentic_dm_gateway import InboundSecurityPipeline
from agentic_dm_gateway.security import sanitize_agent_output

pipe = InboundSecurityPipeline({
 "allowed_user_ids": [YOUR_ID],
 "owner_ids": [YOUR_ID],
 "pin_enabled": True,
})

@bot.event
async def on_message(message):
 if message.author.bot or message.guild is not None:
 return

 pre = pipe.precheck(int(message.author.id), message.content or "")
 if pre.reply_text and not pre.run_agent:
 await message.channel.send(pre.reply_text[:1900])
 return
 if not pre.run_agent:
 return

 raw = await your_agent(pre.sanitized_text) # Hermes, Ollama, API, ...
 await message.channel.send(sanitize_agent_output(str(raw))[:1900])
```

### 3) Protocol-agnostic (Hermes, CLI, Telegram, anything)

No Discord import required. Use the same precheck around any agent turn:

root@kitploit:~

```
from agentic_dm_gateway import InboundSecurityPipe...