---
title: r2ai v1.4.4
url: https://kitploit.com/en/posts/github-radareorg-r2ai-144
source: Kitploit
date: 2026-09-07
fetch_date: 2026-09-08T06:41:01.911312
---

# r2ai v1.4.4

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/50949/5b50cc31b918dbc0066c6a28dab7770ecace2d43775a62d99b1aa391e6b49b0e-display-v1.webp)

New releaseSep 7, 2026

# r2ai v1.4.4

Radare2 AI plugin using local or remote LLMs for decompilation, function explanation, vulnerability detection, renaming, and scripted reverse engineering.

Share

# R2AI - Augmented reversing with LLM for radare2

root@kitploit:~

```
         ╭─────────────────────────────────╮
         │ ,______  .______ .______  ,___  │
 ╭──╮    │ : __   \ \____  |:      \ : __| │
 │ _│_   │ |  \____|/  ____||  _,_  || : | │
 │ O O  <  |   :  \ \   .  ||   :   ||   | │
 │  │╷   │ |   |___\ \__:__||___|   ||   | │
 │  ││   │ |___|        :       |___||___| │
 │ ─╯│   ╰─────────────────────────────────╯
 ╰───╯
```

[![ci](https://github.com/radareorg/r2ai/actions/workflows/ci.yml/badge.svg)](https://github.com/radareorg/r2ai/actions/workflows/ci.yml)
[![radare2](https://img.shields.io/badge/radare2-6.0.4-green)](https://github.com/radareorg/radare2)

## Components

This repository contains two plugins for radare2:

* **r2ai** - native [AI plugin](https://github.com/radareorg/r2ai/blob/master/src/README.md) for radare2
* **decai** - r2js plugin with special [focus on decompilation](https://github.com/radareorg/r2ai/blob/master/decai/README.md)

If you are looking to use radare2 with other agents via MCP:

* **r2mcp** - the [official radare2 mcp](https://github.com/radare2/radare2-mcp)
* **r2copilot** - the mcp with focus on CTF [r2copilot](https://github.com/darallium/r2-copilot)

If you are looking for a radare2 focused autonomous agent:

* **r2agent** - automate radare2 workflows through autonomous agents. [r2agent](https://github.com/nitanmarcel/r2agent)

## Features

* Configure different roles and customize prompts
* Scriptable via r2pipe via the r2ai command
* Live with repl and batch mode from cli or r2 prompt
* Support Automatic (ReAct) mode to solve tasks using function calling
* Use local and remote language models (ollama, openai, grok, anthropic, ..)
* RAG markdown, code or textfiles using its native vector database
* Embed the output of an r2 command and resolve questions on the given data

## User defined Prompts

root@kitploit:~

```
[0x00000000]> r2ai -q
explain: Explain the current function -
devices: Find and explain devices used -
libs: Group imports by Libraries -
varnames: Better variable names -
autoname: Automatically suggest a better name for this function -
vulns: Find vulnerabilities or bugs in the current function -
signature: Suggest an improved function signature -
dlopen: List libraries loaded with dlopen - Some libraries are loaded
decompile: Augmented decompilation based on LLM -
[0x00000000]>
```

## Installation

The recommended way to install any of the r2ai components is via r2pm:

root@kitploit:~

```
$ r2pm -Uci r2ai
$ r2pm -Uci decai
```

## Using r2ai

* Adds the **r2ai** command to the radare2 shell: `r2 -qc r2ai`
* You can also run the wrapper in $PATH: `r2pm -r r2ai`

Drop your API keys in environment variables or use the configuration file:

root@kitploit:~

```
$ export ANTHROPIC_API_KEY=sk-ant-api03-CENSORED
$ export OPENAI_API_KEY=sk-proj-6rlSPS-zN1v...
```

Or edit the api keys file `~/.config/r2ai/apikeys.txt` run:

root@kitploit:~

```
$ r2ai -K
```

## Saving settings

You may customize and save your configuration settings using your OS's default settings file (e.g `~/.radare2rc` on Linux).
For example, the following configuration sets Claude 3.7 by default, with max output tokens to 64000.

root@kitploit:~

```
$ r2ai -E
```

then you can type the commands you want to run when the r2ai plugin is loaded:

root@kitploit:~

```
r2ai -e api=anthropic
r2ai -e model=claude-3-7-sonnet-20250219
r2ai -e max_tokens=64000
```

## Further Reading

* There's [a chapter](https://book.rada.re/plugins/r2ai.html) in the official r2book
* Cryptax on [lmstudio+gptoss](https://cryptax.medium.com/r2ai-with-lmstudio-and-gpt-oss-08efa5ea2476) blog post
* Malware analysis [with r2ai](https://arxiv.org/pdf/2504.07574) by Cryptax and Daniel Nakov
* Analysis of [Linux/Trigona ransomware](https://cryptax.medium.com/linux-trigona-analysis-with-r2ai-3e2bd1815e52), [Linux/Prometei botnet](https://cryptax.medium.com/reversing-a-prometei-botnet-binary-with-r2-and-ai-part-one-3cdb3dc6ffab) and [W32/SkyAI](https://cryptax.medium.com/w32-skyai-uses-ai-so-do-i-d33f04d63534with) with r2ai

## Videos

* [Solving a crackme](https://infosec.exchange/%40radareorg/111946255058894583)
* [De-obfuscation of malware Linux/Ladvix](https://asciinema.org/a/724126)
* [Analysis of the /fast option inside Linux/Trigona ransomware](https://asciinema.org/a/pBPEaJhp6cunWSKFpBUDTgPt4)

[Read more](/en/tools/github/radareorg/r2ai?expand=1)

## Categories

[Static Analysis](/en/categories/static-analysis)[Vulnerability Analysis](/en/categories/vulnerability-analysis)[Code Analysis](/en/categories/code-analysis)[Reverse Engineering](/en/categories/reverse-engineering)[Scripting & Automation](/en/categories/scripting-automation)[Malware Analysis](/en/categories/malware-analysis)[Binary Analysis](/en/categories/binary-analysis)[AI-Assisted Reversing](/en/categories/ai-assisted-reversing)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories