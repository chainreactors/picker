---
title: Automated Penetration Testing with Claude AI
url: https://www.hackingarticles.in/automating-penetration-testing-with-claude-ai/
source: Hacking Articles
date: 2026-06-13
fetch_date: 2026-06-14T06:27:26.918555
---

# Automated Penetration Testing with Claude AI

[Skip to content](#content)

# [Hacking Articles](https://www.hackingarticles.in/)

Raj Chandel’s Blog

Menu

* [Courses We Offer](https://www.hackingarticles.in/courses-we-offer/)
* [CTF Challenges](https://www.hackingarticles.in/ctf-challenges-walkthrough/)
* [Penetration Testing](https://www.hackingarticles.in/penetration-testing/)
* [Web Penetration Testing](https://www.hackingarticles.in/web-penetration-testing/)
* [Red Teaming](https://www.hackingarticles.in/red-teaming/)
* [Donate us](https://www.hackingarticles.in/donate-us/)

* [Home](https://www.hackingarticles.in/)
»* [AI](https://www.hackingarticles.in/category/ai/)
»* [Automated Penetration Testing with Claude AI](https://www.hackingarticles.in/automating-penetration-testing-with-claude-ai/)
»

[AI](https://www.hackingarticles.in/category/ai/)

# Automated Penetration Testing with Claude AI

[June 13, 2026June 13, 2026](https://www.hackingarticles.in/automating-penetration-testing-with-claude-ai/) by [raj](https://www.hackingarticles.in/author/admin/)

### Overview

This article demonstrates a complete, end-to-end penetration test driven almost entirely through natural language. By connecting **Claude Desktop** to a **Model Context Protocol (MCP)** server running on Kali Linux, we turn the AI assistant into an interactive offensive-security co-pilot that executes real Kali tooling on command. Across a multi-host lab, we move from a clean install to full compromise: configuring the integration, running reconnaissance and enumeration, exploiting a SQL injection flaw, popping a root shell through Samba, harvesting and cracking password hashes, taking over a vulnerable WordPress site, and finally recovering domain administrator credentials on a Windows Server 2019 domain controller. The walkthrough doubles as a practical look at where AI accelerates an assessment and, just as importantly, how the lab could have defended against every step.

### Table of Contents:

* **Introduction**
* **Phase 1: Building the MCP Kali Integration**
  + Installing the MCP Kali Server
  + Reviewing the Client Configuration
  + Installing Claude Desktop on Kali Linux
  + Connecting Claude Desktop to the MCP Server
  + Verifying the Integration
* **Phase 2: Reconnaissance and Enumeration**
  + Network Scanning with Nmap
  + Web Directory Enumeration
  + SMB Enumeration with enum4linux
  + SSH Credential Attack with Hydra
* **Phase 3: Exploitation**
  + SQL Injection with sqlmap
  + Port Scanning with Metasploit
  + Gaining Root Access via the Samba Vulnerability
* **Phase 4: Post-Exploitation and Credential Cracking**
  + Harvesting Credentials from /shadow
  + Cracking the Hashes with John the Ripper
* **Phase 5: Compromising the WordPress Target**
  + Assessing WordPress with WPScan
  + Exploiting the Reflex Gallery Plugin
  + Exploiting the Mail-Masta Plugin
  + Achieving WordPress Admin Access
  + Logging In to the Dashboard
  + Web Server Scanning with Nikto
* **Phase 6: Operational Tooling**
  + Checking the Integration’s Health
  + Reviewing the Built-in Command Reference
* **Phase 7: Pivoting to the Windows Domain Controller**
  + SMB Authentication with NetExec
* **Mitigation Strategies**
  + Patch and Retire End-of-Life Software
  + Eliminate Anonymous and Default Access
  + Enforce Strong Authentication
  + Secure Web Applications
  + Harden the Network and Monitor Continuously
* **Conclusion**

### Introduction

Artificial intelligence is reshaping offensive security. Traditionally, an AI assistant could only describe how to run a scan or craft an exploit; the operator still executed everything by hand. The Model Context Protocol (MCP) changes that. MCP is an open standard that defines how large language models discover and call external tools through a consistent, structured interface. Rather than pasting commands and copying output manually, the model talks to an MCP server that advertises a catalogue of capabilities, accepts structured requests, executes them, and returns machine- and human-readable results. Because the standard is uniform, any MCP-aware client can drive any MCP server without custom integration code.

In this engagement, the Kali Linux arsenal becomes that server. The MCP Kali Server wraps tools such as Nmap, Nikto, sqlmap, Hydra, Metasploit, John the Ripper, and NetExec, then exposes them to Claude Desktop running on the same host. The analyst states an objective in plain language — “run an Nmap scan,” “exploit the Samba vulnerability,” “dump the database” — and the model interprets it, selects the right tool, builds the correct command, executes it, reads the raw output, and reasons over the results in a single conversational loop. This collapses the gap between recommendation and execution, while high-impact actions surface a consent prompt that keeps the operator firmly in control.

The sections that follow document the complete workflow. We install the MCP Kali Server, deploy Claude Desktop on Kali, connect the two, and verify the tooling. We then carry out a full attack chain across the lab — reconnaissance, SMB enumeration, a Samba remote-code-execution exploit, password-hash cracking, SQL injection, an SSH credential attack, a WordPress compromise, and domain administrator access on a Windows Server 2019 domain controller — and close with the defensive measures that neutralise each technique. Perform every technique only inside an isolated lab you own or are explicitly authorised to test.

### Lab Environment

The entire engagement runs inside a private, authorised lab. The Kali Linux host serves as the attack platform, and several deliberately vulnerable virtual machines act as targets. The table below summarises the hosts referenced throughout the article.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiUGI7NyErPho_9hccjQ3Olpp0evhpTILgXaBJI1uKA73mF1jAFhmSNwrlCNTAyVof6k8HJrZfcUMIE6YnJij4nqaQH8EWETbvNapvXL11LQdfodaA69KSlq-8hG_2J704HjM-nsL2O0MMtBbGu1eRQ09uB7BJHmUHhHRmpsr6yFgnJudKicwiW1i1XJClD/s16000/0.png)

Before reproducing any technique shown here, ensure you hold explicit written authorisation for every in-scope host. Testing systems you do not own or lack permission to assess, is illegal.

## Phase 1: Building the MCP Kali Integration

### Installing the MCP Kali Server

We begin on the Kali host by installing the MCP Kali server package, which publishes the local security toolset over the MCP interface. The package manager confirms that mcp-kali-server is already present at its newest version, so the environment is ready to proceed.

```
sudo apt install mcp-kali-server
```

## ![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhpmT2JvAxzY4nhredTwHOqdGbB6tdz_uSL6UVEzvl4Obi7ACCqIbK1us-Du9IkH65pf7uQLEfRe6TexQnkPaHSZDMLfDLC9KTSa4ly6qowfNrtv4IoDw1hWmDX9uukaEC0GNNcY8K5g6Ro4-R7KOT13KWetiEABs4IrADzxWTxW2cbZlYeomWHaMYc1lqP/s16000/1.png)

### Reviewing the Client Configuration

The project README documents where each MCP client expects its configuration file and links to a ready-made template. macOS and Windows store the Claude Desktop configuration under their respective application-support paths.

### [**MCP Kali Server**](https://github.com/Wh0am123/MCP-Kali-Server)

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgh2Id-Z751kG-X6sXTEKNco5B1QBlLIlSv82mLHN9nubKajCjay7IuVYmcWcDxBShPn0lo7LWPWPweTn5gntkjnEqXj_uduAkYB-gETVdeCgXEJg73k4Uzlp2QoCnPNmhUczfKdl4LJS8IRkSIQ85eLLuxe2BImr9X7yi-dXyXMJirYID5mbEbTzJrlD2_/s16000/2.png)

Opening the template reveals the canonical client definition. It declares an mcpServers object that launches python3 against a client.py script and forwards traffic to the server over HTTP, with fields for a description, timeout, and an auto-approval allow-list.

## ![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEitxo53wazQKLL4nEqka5-xsTnzZIioCFrKiGofM1wEFKRdz22a3eE4PDXXtBmUc5IGXnCRHzE3LYcFjcQp6DBv4gYmN0ZUpfdqEATfuuoKtFSbYss81qCEuLiEsLSu7-yvFxIKdMcq8-4DMbReAa56ZAz5tZ5xevETeWsRtF-E14rtfI0j0vthcUpQ4awS/s...